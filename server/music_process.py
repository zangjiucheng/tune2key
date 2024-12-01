import os
import subprocess

from midi2audio import FluidSynth
from music21 import converter, stream, note, chord, meter, key

from tools.PTranscription import PianoTranscription

def simplify_midi(midi_dir:str, simple_midi_dir:str) -> None:
    """
    Simplify a MIDI file by converting chords to single notes and quantizing rhythms.
    """
    # Load the MIDI file
    midi_file = converter.parse(midi_dir)

    # Analyze the original key (optional)
    original_key = midi_file.analyze('key')
    print(f"Original Key: {original_key}")

    # Create a new stream for the simplified piece
    simplified_stream = stream.Stream()

    # Simplify the score
    for element in midi_file.flat:
        if isinstance(element, chord.Chord):
            # Keep only the top note of the chord
            top_note = max(element.notes, key=lambda n: n.pitch.midi)
            simplified_note = note.Note(top_note.pitch)
            simplified_note.duration = element.duration
            simplified_note.offset = element.offset
            simplified_stream.insert(simplified_note.offset, simplified_note)
        elif isinstance(element, note.Note):
            # Simplify rhythm by quantizing note durations
            simple_note = note.Note(element.pitch)
            simple_note.duration.quarterLength = round(element.duration.quarterLength * 2) / 2  # Round to nearest half beat
            simple_note.offset = element.offset
            simplified_stream.insert(simple_note.offset, simple_note)
        elif isinstance(element, meter.TimeSignature):
            # Change to a simple time signature (optional)
            simplified_stream.insert(0, meter.TimeSignature('4/4'))
        elif isinstance(element, key.KeySignature):
            # Change to C major/A minor (optional)
            simplified_stream.insert(0, key.KeySignature(0))
        else:
            # Insert other elements without changes
            simplified_stream.insert(element.offset, element)

    # Quantize rhythms to simplify them further
    simplified_stream = simplified_stream.quantize(
        quarterLengthDivisors=[0.25, 0.5, 1.0],  # Allowable note durations (16th, 8th, quarter notes)
        inPlace=False
    )

    # Optionally transpose the piece to C major/A minor
    # Uncomment the following lines if you wish to transpose
    # interval_to_c = original_key.relative.transposePitchFromC()
    # transposed_stream = simplified_stream.transpose(interval_to_c)
    # simplified_stream = transposed_stream

    # Export the simplified MIDI file
    simplified_stream.write('midi', fp=simple_midi_dir)

    # Optionally export the sheet music as a PDF
    # Ensure that MuseScore or another MusicXML reader is installed and set up with music21
    # simplified_stream.write('musicxml.pdf', fp='simplified_piano_piece.pdf')

    print("Simplified MIDI file has been generated.")


def generate_sheet_pdf(input_path:str, output_pdf:str) -> None:
    """Convert MIDI, MusicXML, MSCZ, or MSCX file to PDF of sheet music."""
    # Check if MuseScore is installed
    try:
        subprocess.run(['mscore', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError:
        raise EnvironmentError("MuseScore is not installed or not found in the system PATH, please install it from https://musescore.org/en/download/musescore.dmg")
    try:
        process = subprocess.Popen(['mscore', input_path, '-o', output_pdf], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if process.returncode != 0:
            print(stdout.decode('utf-8'))
            print(stderr.decode('utf-8'))
            raise RuntimeError(f"Failed to generate PDF: {stderr.decode('utf-8')}")
    except (subprocess.CalledProcessError,RuntimeError) as e:
        raise RuntimeError(f"Failed to generate PDF: {e}")

def mp32midi(mp3_path:str, midi_path:str) -> None:
    """Use AI to transcribe MP3 to MIDI file.

    Args:
        mp3_path (str): mp3 file path
        midi_path (str): midi file path
    """
    # Transcriptor
    transcriptor = PianoTranscription(device='cpu')    # 'cuda' | 'cpu' | 'mps'

    # Transcribe and write out to MIDI file
    transcriptor.transcribe(mp3_path, midi_path)
    
def play_midi(midi_path:str) -> None:
    """ Play MIDI file and convert to WAV file.

    Args:
        midi_path (str): midi file path

    Raises:
        FileNotFoundError: if MIDI file not found
    """
    # Play MIDI
    if not os.path.exists(midi_path):
        raise FileNotFoundError(f"MIDI file not found: {midi_path}")
    
    soundfont_path = 'resources/GeneralUser-GS.sf2'
    
    if not os.path.isfile(soundfont_path):
        print(f"Soundfont file not found: {soundfont_path}, cannot convert MIDI to MP3.")
        return
    
    fs = FluidSynth(sound_font=soundfont_path)
    fs.play_midi(midi_path)


def midi2mp3(midi_path:str, mp3_path:str) -> None:
    """ Convert MIDI to MP3 file.

    Args:
        midi_path (str): midi file path
    """
    # Convert MIDI to audio
    soundfont_path = 'resources/GeneralUser-GS.sf2'
    if not os.path.isfile(soundfont_path):
        print(f"Soundfont file not found: {soundfont_path}, cannot convert MIDI to MP3.")
        return
    fs = FluidSynth(sound_font=soundfont_path)
    fs.midi_to_audio(midi_path, mp3_path)

def transcribe_audio(mp3_path:str, midi_path:str, pdf_path:str) -> None:
    # Transcribe MP3 to MIDI
    mp32midi(mp3_path, midi_path)

    # Generate sheet music PDF
    generate_sheet_pdf(midi_path, pdf_path)

if __name__ == "__main__":

    file_name="Track_in_Time"

    mp3_path = f'resources/mp3/{file_name}.mp3'
    midi_path = f'resources/midi/{file_name}.mid'
    pdf_path = f'resources/sheet/{file_name}.pdf'

    # transcribe_audio(mp3_path, midi_path, pdf_path)
    play_midi(midi_path)
    # midi2mp3(midi_path, mp3_path)