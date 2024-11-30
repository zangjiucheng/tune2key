from piano_transcription_inference import PianoTranscription, sample_rate, load_audio
import os

def transcribe_audio(input_audio_path, output_directory='./resources/mid/'):
    """
    Transcribes a piano audio file into a MIDI file.

    Args:
        input_audio_path (str): Path to the input audio file.
        output_directory (str): Directory to save the output MIDI file.

    Returns:
        str: Path to the generated MIDI file.
    """
    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)
    print(input_audio_path, 'input_audio_path')

    # Load the audio
    (audio, _) = load_audio(input_audio_path, sr=sample_rate, mono=True)
    
    print('doing transcribe')
    # Transcriptor
    transcriptor = PianoTranscription(device='cpu')  # 'cuda' | 'cpu' | 'mps'

    # Determine output MIDI file path
    file_name = os.path.basename(input_audio_path).split('.')[0]  # Get the base name without extension
    output_midi_path = os.path.join(output_directory, f"{file_name}.mid")

    # Transcribe and save the MIDI file
    transcribed_dict = transcriptor.transcribe(audio, output_midi_path)

    return output_midi_path
