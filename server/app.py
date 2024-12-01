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
        print(music_sheet.transcribed_path)

        midi_path = transcribe_audio(audio_file_path)
        print(midi_path)


    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/make-harder', methods=['POST'])
def make_harder():
    # Get the parameters from the request
    difficulty_increase = float(request.form.get('difficulty_increase', 1.0))
    ornamentation = int(request.form.get('ornamentation', 0))
    midi_file = request.files['midi_file']

    # Save the uploaded MIDI file
    original_filename = midi_file.filename
    midi_path = os.path.join(MIDI_DIR, original_filename)
    midi_file.save(midi_path)

    # Call the function to make the music harder
    new_midi_filename = make_music_harder(
        difficulty_increase,
        ornamentation,
        midi_path
    )

    return f"New MIDI file created: {new_midi_filename}"



if __name__ == "__main__":  
    app.run(debug=True)