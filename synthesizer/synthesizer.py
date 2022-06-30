import numpy as np
from modulation import *
from notes import *
from note import *
from instrument import *
from scipy.io import wavfile

class Synthesizer:
    def __init__(self, filename_partiture, filename_instrument):

        self.filename_partiture = filename_partiture
        self.filename_instrument = filename_instrument
        
    def read_partiture(self):
        return ReadPartiture(self.filename_partiture).read_partiture()

    def read_instrument(self):
        return ReadInstrument(self.filename_instrument).read()

    def get_frequency(self, type):
        return notes_mapping[type]
    
    def compose(self):
        list_of_notes=self.read_partiture()
        armonics, modulations=self.read_instrument()
        decay= list(modulations.values())[2]
        song_duration=float(list_of_notes[-1][0])+float(list_of_notes[-1][2])+decay
        song=np.empty(int(song_duration*44100))

        for i in list_of_notes:
            starts, type, duration=i
            frequency=self.get_frequency(type)
            duration+=decay
            note=self.create_note(duration)
            armonic_note=self.create_armonic_note(frequency, duration, armonics, note)
            modulated_note=self.create_modulation(duration, modulations, armonic_note, note)
            s=int(starts*44100)
            e=len(modulated_note) + s
            song[s:e]+=modulated_note

        return song

    def create_note(self, duration):
        return CreateArrayNote(duration).array_of_note()

    def create_armonic_note(self, frequency, duration, armonics, note):
        return ArmonicNote(frequency, duration, armonics).get_armonic(note)

    def create_modulation(self, duration, modulations, armonic_note, note):
        return ModulatedNote(duration, modulations).modulation(armonic_note, note)

    def create_wav(self):
        song=self.compose()
        return wavfile.write("New_song.wav", 44100, song)
