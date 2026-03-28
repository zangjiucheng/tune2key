import os
import shutil

try:
    from .music_process import *
except ImportError:
    from music_process import *

class ProgressTracker:
    def __init__(self):
        self.pointer = 0
        self.total_segments = 0

    def track_progress(self, pointer, total_segments):
        self.pointer = pointer
        self.total_segments = total_segments
        print(f"Processing segment {pointer}/{total_segments}")

class TUNE2KEY:
    def __init__(self) -> None:
        self.resource_dir = os.path.join(os.path.dirname(__file__), 'resources')
        self._ensure_resource_dirs()
        self.file_name = None
        
        self.midi_dir = None
        self.music_dir = None
        self.music_sheet_dir = None
        
        self.tracker = ProgressTracker()

    def _ensure_resource_dirs(self) -> None:
        required_dirs = ['upload', 'midi', 'sheet', 'mp3', 'simple_sheet', 'harder_sheet']
        for folder in required_dirs:
            os.makedirs(os.path.join(self.resource_dir, folder), exist_ok=True)
        
    def upload_file(self, file_path:str) -> None:
        self.file_name = os.path.basename(file_path).split('.')[0]

        self.midi_dir = os.path.join(self.resource_dir, 'midi', f'{self.file_name}.mid')
        self.music_dir = os.path.join(self.resource_dir, 'mp3', f'{self.file_name}.mp3')
        self.music_sheet_dir = os.path.join(self.resource_dir, 'sheet', f'{self.file_name}.pdf')
        self.music_sheet_simple_dir = os.path.join(self.resource_dir, 'simple_sheet', f'{self.file_name}_simple')
        
        self.load_file_type(file_path) 
        
    def load_file_type(self, file_path:str) -> None:
        _, ext = os.path.splitext(file_path)
        ext = ext.lower()
        
        if ext in {'.mp3', '.opus'}:
            print(f'Get {ext} input file, start processing...')
            self.process_audio(file_path)
        elif ext=='.mid':
            print('Get midi input file, start processing...')
            self.process_midi(file_path)
        elif ext=='.pdf':
            print('Get pdf input file, start processing...')
            self.process_pdf(file_path)
        else:
            print('Unsupported file type')
            raise ValueError(f"Unsupported file type: {ext}")
    
    def process_audio(self, file_path:str) -> None:
        mp32midi(file_path, self.midi_dir, self.tracker.track_progress)
        midi2mp3(self.midi_dir, self.music_dir)
        generate_sheet_pdf(self.midi_dir, self.music_sheet_dir)
        simplify_midi(self.midi_dir, self.music_sheet_simple_dir+".mid")
        generate_sheet_pdf(self.music_sheet_simple_dir+".mid", self.music_sheet_simple_dir+".pdf")
        midi2mp3(self.music_sheet_simple_dir+".mid", self.music_sheet_simple_dir+".mp3")
        os.remove(file_path)

    # Backward compatibility alias.
    def process_mp3(self, file_path:str) -> None:
        self.process_audio(file_path)
        
    def process_midi(self, file_path:str) -> None:
        shutil.copy(file_path, self.midi_dir)
        midi2mp3(self.midi_dir, self.music_dir)
        generate_sheet_pdf(self.midi_dir, self.music_sheet_dir)
        simplify_midi(self.midi_dir, self.music_sheet_simple_dir+".mid")
        generate_sheet_pdf(self.music_sheet_simple_dir+".mid", self.music_sheet_simple_dir+".pdf")
        midi2mp3(self.music_sheet_simple_dir+".mid", self.music_sheet_simple_dir+".mp3")
        os.remove(file_path)
    
    def process_pdf(self, file_path:str) -> None:
        raise NotImplementedError(f"PDF input is not supported yet: {file_path}")
    
    def clean(self):
        if self.music_dir:
            os.remove(self.music_dir)
        if self.midi_dir:
            os.remove(self.midi_dir)
        if self.music_sheet_dir:
            os.remove(self.music_sheet_dir)
        if self.music_sheet_simple_dir+".mid":
            os.remove(self.music_sheet_simple_dir+".mid")
        if self.music_sheet_simple_dir+".pdf":
            os.remove(self.music_sheet_simple_dir+".pdf")
        if self.music_sheet_simple_dir+".mp3":
            os.remove(self.music_sheet_simple_dir+".mp3")