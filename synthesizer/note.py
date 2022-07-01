
import numpy as np
from modulation import *
from matplotlib import pyplot as plt
class ModulatedNote:
    def __init__(self, duration, modulations):
        self.duration= duration
        self.modulations= modulations

    def divide_modulation(self):
        modulation= self.modulations
        first_time= modulation[0][1]
        second_time= self.duration-modulation[2][1]
        return modulation, first_time, second_time
    
    def modulation(self, armonic_note, array_of_note):
        
        modulation, first_time, second_time= self.divide_modulation()
        keys= [modulation[0][0], modulation[1], modulation[2][0]]
        func=ModulationFunctions()

        m= np.empty(int(44100*(self.duration)))
        m[:int(44100*first_time)]=func.moduled(keys[0], array_of_note[:int(44100*first_time)], first_time)
        m[int(44100*first_time):int(44100*second_time)]=m[int(44100*first_time)-1]*func.moduled(keys[1], array_of_note[int(44100*first_time):int(44100*second_time)], second_time)
        m[int(44100*second_time):]=m[int(44100*second_time)-1]*func.moduled(keys[2], array_of_note[int(44100*second_time):]-second_time, self.duration-second_time)

        a=m*armonic_note
        x=array_of_note
        plt.plot(x, a)
        plt.show()
        return a

class ArmonicNote:
    def __init__(self, frequency, duration, armonics):
        self.frequency= frequency
        self.duration= duration
        self.armonics=armonics

    def get_armonic(self, note):
        d=self.armonics
        armonics=np.zeros(len(note))
        for i in d:
            armonics+=(d[i] * np.sin(( (2*np.pi*i*self.frequency * note))))
        return armonics
        
class CreateArrayNote:
    def __init__(self, duration):
        self.duration = duration

    def array_of_note(self):
        return np.linspace(0, self.duration,int(44100*self.duration))

