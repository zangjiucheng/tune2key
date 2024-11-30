from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from music_midi import transcribe_audio
from music_sheet import MUSIC_SHEET
import os


app = Flask(__name__)

CORS(app)


@app.route('/transcribe', methods=['POST'])
def transcribe():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    uploaded_file = request.files['file']
    if uploaded_file.filename == '':
        return jsonify({"error": "Empty file name"}), 400
    
    try:
        audio_dir=os.path.join(os.path.dirname(__file__), 'resources', 'audios')
        audio_file_path=os.path.join(audio_dir, uploaded_file.filename)
        uploaded_file.save(audio_file_path)

        # create music_sheet class
        music_sheet = MUSIC_SHEET(audio_file_path)
        
        midi_path = transcribe_audio(audio_file_path)
        print(midi_path)


    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

if __name__ == "__main__":  
    app.run(debug=True)