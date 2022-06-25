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
            cant_armonicos=int(f.readline())
            for line in range(1,cant_armonicos+1):
                line=f.readline().strip()
                line=line.split(' ')
                armonics[int(line[0])]=float(line[1])

            for line in f:
                line=line.strip().split(' ')
                if len(line)==1:
                    modulations[line[0]]=[]
                else:
                    modulations[line[0]]=line[1]
        return armonics, modulations


class Instrument:
    def __init__(self, name, filename):
        self.name = name
        self.readinstrument=ReadInstrument(filename)
        self.armonics=None
        self.modulations=None
        self.read()

    def read(self):
        self.armonics, self.modulations=self.readinstrument.read()

class CreateNote:
    def __init__(self, type, amplitude, frequency, duration, starts, instrument):
        self.type = type
        self.amplitude = amplitude
        self.frequency = frequency
        self.duration = duration
        self.starts = starts
        
        self.x=np.linspace(0, self.duration,int(44100*self.duration))
        self.instrument=instrument
        self.armonic_note=self.get_armonics()
        #self.final_note=self.sum_senoidales()
        self.modulated_note=None
        
        

    def get_armonics(self):
        d=self.instrument.armonics
        armonics=[]
        for i in d:
            armonics.append(d[i] * np.sin(( (2*np.pi*i*self.frequency * self.x))))
        return sum(armonics)

    #def sum_senoidales(self):
        #return sum(self.senoidales)
        
    def divide_modulation(self):
        modulation=instrument.modulations
        values=list(modulation.values())
        print(modulation.values())
        first_time=float(values[0])
        second_time=self.duration-float(values[2])
        print(first_time,second_time)
        return modulation, first_time, second_time
    
    def module_note(self):
        modulation, first_time, second_time= self.divide_modulation()
        keys=list(modulation.keys())
        
        m=np.zeros(int(44100*self.duration))
        a=np.zeros(int(44100*self.duration))
        for idx,ti in enumerate(self.x):
            if ti<=first_time:
                m[idx]=moduled(keys[0], ti, first_time)
                
            elif ti<=second_time:
                m[idx]=moduled(keys[1],ti, second_time)
               
            else:
                m[idx]=moduled(keys[2],ti-second_time,self.duration-second_time)
                
        a=m*self.armonic_note
        return a




instrument=Instrument("piano", "piano.txt")
print(instrument.armonics, instrument.modulations)



Note=CreateNote("A4", 1, 440, 0.1, 0, instrument)
x=Note.x
y=Note.module_note()


plt.plot(x, y)
plt.grid(True)
plt.ylabel('Amplitude')
plt.xlabel("Time (s)")
plt.show()
