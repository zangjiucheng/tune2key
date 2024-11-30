import numpy as np
import matplotlib.pyplot as plt
from mido import MidiFile

class MidiVisualizer:
    def __init__(self, midi_path):
        self.midi = MidiFile(midi_path)
        self.ticks_per_beat = self.midi.ticks_per_beat
        self.tempo = 500000  # Default tempo (microseconds per beat)

    def get_piano_roll(self):
        # Calculate total ticks
        total_ticks = sum(msg.time for track in self.midi.tracks for msg in track)
        # Initialize piano roll array
        piano_roll = np.zeros((128, total_ticks), dtype=bool)
        current_tick = 0

        for track in self.midi.tracks:
            for msg in track:
                current_tick += msg.time
                if msg.type == 'note_on' and msg.velocity > 0:
                    piano_roll[msg.note, current_tick] = True

        return piano_roll

    def plot_piano_roll(self):
        piano_roll = self.get_piano_roll()
        plt.imshow(piano_roll, aspect='auto', cmap='gray_r', origin='lower')
        plt.xlabel('Time (ticks)')
        plt.ylabel('MIDI Note Number')
        plt.title('Piano Roll')
        plt.show()

if __name__ == "__main__":
    midi_path = 'test.mid'
    visualizer = MidiVisualizer(midi_path)
    visualizer.plot_piano_roll()