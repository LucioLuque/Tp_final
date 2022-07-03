from function import *
from note import *
import numpy as np
from instrument import *






class Sintetizador:
    def __init__(self, filename_partiture, instrument):
        self.filename_partiture = filename_partiture
        self.instrument = instrument
        self.list_compose=None
        self.x=None
        self.read_partiture()
        
        
        


    def read_partiture(self):
        number=0
#type, amplitude, frequency, duration, starts, instrument
        with open (self.filename_partiture, 'r') as f:
            lines=f.readlines()
            last=(lines[-1].strip().split(' '))
            song_duration=float(last[0])+float(last[2])
            lista_vacia=np.zeros(int(song_duration*44100))
            composed_list=lista_vacia
            y=[]
            
            
            
            for line in lines:
                number=1
                empty_composition=np.zeros(int(song_duration*44100))
                line=line.strip().split(' ')
                starts=float(line[0])
                type=line[1]
                duration=float(line[2])
                note=self.create_note(type, duration, starts, self.instrument)
                s=int(starts*44100)
                #e=int(((starts)+(duration))*44100)
                e=len(note) + s
                empty_composition[s:e]=note

                composed_list=sum([composed_list, empty_composition])
                
                
                
            self.list_compose=composed_list
            #self.list_compose=composed_list
            self.x=np.linspace(0, song_duration, len(composed_list))
            print(number)

            

           

    def create_note(self, type, duration, starts, instrument):
        frequency=function(type)
        note=CreateNote(type, frequency, duration, starts, instrument)
        return note.change_note()

    def get_partiture(self):
        return self.partiture