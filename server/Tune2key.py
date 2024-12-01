import os
import shutil

from music_process import *

class TUNE2KEY:
    def __init__(self) -> None:
        self.resource_dir = os.path.join(os.path.dirname(__file__), 'resources')
        self.file_name = None
        
        self.midi_dir = None
        self.music_dir = None
        self.music_sheet_dir = None
        
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
        
        if ext=='.mp3':
            print('Get mp3 input file, start processing...')
            self.process_mp3(file_path)
        elif ext=='.mid':
            print('Get midi input file, start processing...')
            self.process_midi(file_path)
        elif ext=='.pdf':
            print('Get pdf input file, start processing...')
            self.process_pdf(file_path)
        else:
            print('Unsupported file type')
            raise ValueError(f"Unsupported file type: {ext}")
    
    def process_mp3(self, file_path:str) -> None:
        shutil.move(file_path, file_path.split('.')[0])
        mp32midi(file_path.split('.')[0], self.midi_dir)
        midi2mp3(self.midi_dir, self.music_dir)
        generate_sheet_pdf(self.midi_dir, self.music_sheet_dir)
        simplify_midi(self.midi_dir, self.music_sheet_simple_dir+".mid")
        generate_sheet_pdf(self.music_sheet_simple_dir+".mid", self.music_sheet_simple_dir+".pdf")
        midi2mp3(self.music_sheet_simple_dir+".mid", self.music_sheet_simple_dir+".mp3")
        os.remove(file_path.split('.')[0])
        
    def process_midi(self, file_path:str) -> None:
        shutil.copy(file_path, self.midi_dir)
        shutil.move(file_path, file_path.split('.')[0])
        midi2mp3(self.midi_dir)
        generate_sheet_pdf(self.midi_dir, self.music_sheet_dir)
        simplify_midi(self.midi_dir, self.music_sheet_simple_dir+".mid")
        generate_sheet_pdf(self.music_sheet_simple_dir+".mid", self.music_sheet_simple_dir+".pdf")
        midi2mp3(self.music_sheet_simple_dir+".mid", self.music_sheet_simple_dir+".mp3")
        os.remove(file_path.split('.')[0])
    
    def process_pdf(self):
        print('Unsupported pdf for now')
    
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