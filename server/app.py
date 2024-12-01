import os

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from make_music_harder import make_music_harder
from Tune2key import TUNE2KEY
from threading import Thread

app = Flask(__name__)

CORS(app)

TUNE2KEY_obj = TUNE2KEY()
SHEET_MUSIC_FOLDER='./resources/sheet'
AUDIO_FOLDER = './resources/mp3'

base_path = os.path.join(os.path.dirname(__file__), 'resources')

@app.route('/upload', methods=['POST'])
def transcribe():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    uploaded_file = request.files['file']
    if uploaded_file.filename == '':
        return jsonify({"error": "Empty file name"}), 400
    
    try:
        upload_file_path=os.path.join(base_path, 'upload', uploaded_file.filename)
        uploaded_file.save(upload_file_path)

        def process_file():
            TUNE2KEY_obj.upload_file(upload_file_path)

        thread = Thread(target=process_file)
        thread.daemon = True
        thread.start()
        return jsonify({"success": True}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500 
    
@app.route('/process/status/<name>', methods=['GET'])
def process_status(name):
    upload_file_path = os.path.join(base_path, 'upload', name)
    midi_file_path = os.path.join(base_path, 'midi', f'{name}.mid')
    sheet_file_path = os.path.join(base_path, 'sheet', f'{name}.pdf')
    mp3_file_path = os.path.join(base_path, 'mp3', f'{name}.mp3')
    
    status = {
    "midi": os.path.exists(midi_file_path),
    "sheet": os.path.exists(sheet_file_path),
    "mp3": os.path.exists(mp3_file_path)
    }

    if all(status.values()):
        return jsonify({"status": "done"}), 200
    elif os.path.exists(upload_file_path):
        return jsonify({"status": "processing"}), 200
    else:
        return jsonify({"status": "not_found"}), 404

@app.route('/music_sheet/<name>', methods=['GET'])
def music_sheet(name):
    return os.path.join(base_path, 'sheet', f'{name}.pdf')

@app.route('/audio/<name>', methods=['GET'])
def audio(name):
    return os.path.join(base_path, 'mp3', f'{name}.mp3')


@app.route('/make-harder', methods=['POST'])
def make_harder():
    # Get the parameters from the request
    difficulty_increase = float(request.form.get('difficulty_increase', 1.0))
    ornamentation = int(request.form.get('ornamentation', 0))
    midi_file = request.files['midi_file']

    # Save the uploaded MIDI file
    original_filename = midi_file.filename
    midi_path = os.path.join(os.path.dirname(__file__), 'resources', 'midi', original_filename)
    print(midi_path)
    midi_file.save(midi_path)

    # Call the function to make the music harder
    new_midi_filename = make_music_harder(
        difficulty_increase,
        ornamentation,
        './resources/midi/Victory.mid'
    )
# filename is the filename with ".pdf" ending

@app.route('/download/<filename>', methods=['GET'])
def download(filename):
    try:
        # Make sure the file exists
        if filename.lower().endswith('.pdf'):
            folder = SHEET_MUSIC_FOLDER
            mimetype = 'application/pdf'
        elif filename.lower().endswith('.mp3'):
            folder = AUDIO_FOLDER
            mimetype = 'audio/mpeg'
        file_path = os.path.join(folder, filename)
        print(file_path, 'file_path')
        if not os.path.exists(file_path):
            return jsonify({"error": "File not found"}), 404
        
        # Send the file to the client
        return send_from_directory(folder, filename, as_attachment=True, mimetype=mimetype)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":  
    app.run(debug=True)