import os

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS

from Tune2key import TUNE2KEY

app = Flask(__name__)

CORS(app)

TUNE2KEY_obj = TUNE2KEY()

base_path = os.path.join(os.path.dirname(__file__), 'resources')

@app.route('/transcribe', methods=['POST'])
def transcribe():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    uploaded_file = request.files['file']
    if uploaded_file.filename == '':
        return jsonify({"error": "Empty file name"}), 400
    
    try:
        upload_file_path=os.path.join(base_path, 'upload', uploaded_file.filename)
        uploaded_file.save(upload_file_path)

        TUNE2KEY_obj.upload_file(upload_file_path)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/music_sheet/<name>', methods=['GET'])
def music_sheet(name):
    return os.path.join(base_path, 'sheet', f'{name}.pdf')

@app.route('/audio/<name>', methods=['GET'])
def audio(name):
    return os.path.join(base_path, 'audio', f'{name}.mp3')

if __name__ == "__main__":  
    app.run(debug=True)