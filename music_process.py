import subprocess
from tools.PTranscription import PianoTranscription
from midi2audio import FluidSynth
import os

def generate_sheet_pdf(input_path:str, output_pdf:str) -> None:
    """Convert MIDI, MusicXML, MSCZ, or MSCX file to PDF of sheet music."""
    # Check if MuseScore is installed
    try:
        subprocess.run(['mscore', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError:
        raise EnvironmentError("MuseScore is not installed or not found in the system PATH, please install it fromhttps://musescore.org/en/download/musescore.dmg")
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


def midi2mp3(midi_path:str) -> None:
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
    fs.midi_to_audio(midi_path, f"{midi_path.split('.')[0]}/_generated.mp3")

def mp32sheet(mp3_path:str, midi_path:str, pdf_path:str) -> None:
    # Transcribe MP3 to MIDI
    mp32midi(mp3_path, midi_path)

    # Generate sheet music PDF
    generate_sheet_pdf(midi_path, pdf_path)

if __name__ == "__main__":

    file_name="Track_in_Time"

    mp3_path = f'resources/mp3/{file_name}.mp3'
    midi_path = f'resources/midi/{file_name}.mid'
    pdf_path = f'resources/sheet/{file_name}.pdf'

    # mp32sheet(mp3_path, midi_path, pdf_path)
    play_midi(midi_path)