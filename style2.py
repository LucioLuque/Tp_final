import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
from modulation import *

class ReadInstrument:
    def __init__(self, filename):
        self.filename=filename
    
    def read(self):
        armonics={}
        modulations={}
        with open (self.filename, 'r') as f:
            amount_armonics= int(f.readline())
            for line in range(1,amount_armonics+1):
                line=f.readline().strip()
                line=line.split(' ')
                armonics[int(line[0])]= float(line[1])

            for line in f:
                line=line.strip().split(' ')
                if len(line)==1:
                    modulations[line[0]]= []
                else:
                    modulations[line[0]]= line[1]
        return armonics, modulations

class Instrument:
    def __init__(self, name, filename):
        self.name = name
        self.readinstrument= ReadInstrument(filename)
        self.armonics= None
        self.modulations= None
        self.read()

    def read(self):
        self.armonics, self.modulations=self.readinstrument.read()

class ModulatedNote:
    def __init__(self, duration, instrument):
        self.instrument= instrument
        self.duration= duration

    def divide_modulation(self):
        modulation= instrument.modulations
        values= list(modulation.values())
        #print(modulation.values())
        first_time= float(values[0])
        second_time= self.duration-float(values[2])
        #print(first_time,second_time)
        return modulation, first_time, second_time
    
    def modulation(self, armonic_note, x):
        modulation, first_time, second_time= self.divide_modulation()
        keys= list(modulation.keys())
        
        m= np.zeros(int(44100*self.duration))
        a= np.zeros(int(44100*self.duration))
        for idx,ti in enumerate(x):
            if ti<=first_time:
                m[idx]= moduled(keys[0], ti, first_time)
                
            elif ti<=second_time:
                m[idx]= moduled(keys[1],ti, second_time)
               
            else:
                m[idx]= moduled(keys[2],ti-second_time,self.duration-second_time)
                
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
        armonics=[]
        for i in d:
            armonics.append(d[i] * np.sin(( (2*np.pi*i*self.frequency * x))))
        return sum(armonics)

    def change_note(self, x):
        armonic_note=self.get_armonic(x)
        return self.modulated_note.change_note(armonic_note, x)

class CreateNote:
    def __init__(self, type, amplitude, frequency, duration, starts, instrument):
        self.type = type
        self.amplitude = amplitude
        self.frequency = frequency
        self.duration = duration
        self.starts = starts
        self.instrument= instrument

        self.x=np.linspace(0, self.duration,int(44100*self.duration))

        self.armonic_note=ArmonicNote(self.frequency, self.duration ,self.instrument)
        
    def change_note(self):
        return self.armonic_note.change_note(self.x)

instrument=Instrument("piano", "piano.txt")
print(instrument.armonics, instrument.modulations)

Note=CreateNote("A4", 1, 440, 0.1, 0, instrument)
x=Note.x
y=Note.change_note()

plt.plot(x, y)
plt.grid(True)
plt.ylabel('Amplitude')
plt.xlabel("Time (s)")
plt.show()