from piano_transcription_inference import PianoTranscription, sample_rate, load_audio
import os

resource_path = 'resources'

file = 'PERFECT.mp3'
file_path = os.path.join(resource_path, file)

# Load audio
(audio, _) = load_audio(file_path, sr=sample_rate, mono=True)

# Transcriptor
transcriptor = PianoTranscription(device='cpu')    # 'cuda' | 'cpu' | 'mps'

# Transcribe and write out to MIDI file
transcribed_dict = transcriptor.transcribe(audio, file.split('.')[0] + '.mid')