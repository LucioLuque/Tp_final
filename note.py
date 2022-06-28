import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
from modulation import *

class ModulatedNote:
    def __init__(self, duration, instrument):
        self.instrument= instrument
        self.duration= duration

    def divide_modulation(self):
        modulation= self.instrument.modulations
        values= list(modulation.values())
        first_time= values[0]
        second_time= self.duration-values[2]
        
        return modulation, first_time, second_time
    
    def modulation(self, armonic_note, x):
        
        modulation, first_time, second_time= self.divide_modulation()
        keys= list(modulation.keys())
        func=ModulationFunctions()
        
        m= np.zeros(int(44100*(self.duration)))
        
        

        m[:int(44100*first_time)]=func.moduled(keys[0], x[:int(44100*first_time)], first_time)
        m[int(44100*first_time):int(44100*second_time)]=func.moduled(keys[1], x[int(44100*first_time):int(44100*second_time)], second_time)
        m[int(44100*second_time):]=func.moduled(keys[2], x[int(44100*second_time):]-second_time, self.duration-second_time)
        
        a=m*armonic_note
        
        return a
        

    def change_note(self, armonic_note, x):
        return self.modulation(armonic_note, x)

class ArmonicNote:
    def __init__(self, frequency, duration, instrument):
        self.frequency= frequency
        self.duration= duration
        self.instrument= instrument
        self.modulated_note= ModulatedNote(self.duration, self.instrument)

    def get_armonic(self, x):
        d=self.instrument.armonics
        armonics=np.zeros(len(x))
        for i in d:
            armonics+=(d[i] * np.sin(( (2*np.pi*i*self.frequency * x))))
    
        return armonics
        

    def change_note(self, x):
        armonic_note=self.get_armonic(x)
        return self.modulated_note.change_note(armonic_note, x)

class CreateNote:
    def __init__(self, type, frequency, duration, starts, instrument):
        self.type = type
        self.frequency = frequency
        self.duration = duration
        self.starts = starts
        self.instrument= instrument
        
        self.x=np.linspace(0, self.duration,int(44100*self.duration))

        self.armonic_note=ArmonicNote(self.frequency, self.duration ,self.instrument)
        
    def change_note(self):
        return self.armonic_note.change_note(self.x)

