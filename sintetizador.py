import numpy as np
from modulation import *
from notes import *
from note import *
from instrument import *
from datetime import datetime
class ReadPartiture:
    def __init__(self, filename_partiture):
        self.filename_partiture = filename_partiture
        
    def read_partiture(self):
        list_of_notes = []
        with open (self.filename_partiture, 'r') as f:
            
            for line in f:
                line=line.strip().split(' ')
                starts=float(line[0])
                type=line[1]
                duration=float(line[2])
                list_of_notes.append((starts, type, duration))
        return list_of_notes

class Sintetizador:
    def __init__(self, filename_partiture, filename_instrument):

        self.filename_partiture = filename_partiture
        self.instrument = Instrument(filename_instrument)
        self.list_of_notes = []
        self.last=None
        self.list_compose=None
        self.x=None
        self.decay=None
        self.read_partiture()
        self.compose()
        
    def read_partiture(self):
        self.list_of_notes= ReadPartiture(self.filename_partiture).read_partiture()
    
    def compose(self):

        self.decay= list(self.instrument.modulations.values())[2]
      
        song_duration=float(self.list_of_notes[-1][0])+float(self.list_of_notes[-1][2])+self.decay
        composed_list=np.zeros(int(song_duration*44100))
        
        for i in self.list_of_notes:
            starts, type, duration=i
            frequency=notes_mapping[type]
            
            duration+=self.decay
            #instanteInicial = datetime.now()

            note=self.create_note(type, frequency, duration, starts, self.instrument)
            #instanteFinal = datetime.now()
            #tiempo = instanteFinal - instanteInicial
            #print(tiempo)
            
            s=int(starts*44100)
           
            e=len(note) + s
            
            empty_composition=np.zeros(int(song_duration*44100))
            empty_composition[s:e]=note
            #instanteInicial = datetime.now()
            composed_list[s:e]=composed_list[s:e] + empty_composition[s:e]
            
            #instanteFinal = datetime.now()
            #tiempo = instanteFinal - instanteInicial # Devuelve un objeto timedelta
            #print(tiempo)
            
        self.list_compose=composed_list

        self.x=np.linspace(0, song_duration, len(composed_list))

    def create_note(self, type,frequency, duration, starts, instrument):
        note=CreateNote(type, frequency, duration, starts, instrument)
        return note.change_note()