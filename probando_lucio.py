import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile


class ReadInstrument:
    def __init__(self, filename):
        self.filename=filename
    
    def read(self):
        armonicos={}
        module={}
        with open (self.filename, 'r') as f:
            l1=int(f.readline())
            for line in range(1,l1+1):
                line=f.readline().strip()
                line=line.split(' ')
                armonicos[int(line[0])]=float(line[1])

            for line in f:
                line=line.strip().split(' ')
                if len(line)==1:
                    module[line[0]]=[]
                else:
                    module[line[0]]=line[1]
        return armonicos, module


class Instrument:
    def __init__(self, name, filename):
        self.name = name
        self.readinstrument=ReadInstrument(filename)
        self.armonicos=None
        self.module=None
        self.read()


    def read(self):
        self.armonicos, self.module=self.readinstrument.read()


class CreateNote:
    def __init__(self, type, amplitude, frequency, duration, starts, instrument):
        self.type = type
        self.amplitude = amplitude
        self.frequency = frequency
        self.duration = duration
        self.starts = starts


        
        self.x=np.linspace(0, self.duration, 44100*self.duration)
        self.armonicos=instrument.armonicos
        self.senoidales=self.get_senoidales()
        self.final_note=self.sum_senoidales()
        self.module=instrument.module

    def get_senoidales(self):
        d=self.armonicos
        senoidales=[]
        for i in d:
            senoidales.append(d[i] * np.sin( (2*np.pi*i*self.frequency * self.x)))
        return (senoidales)

    def sum_senoidales(self):
        return sum(self.senoidales)




piano=Instrument("piano", "piano.txt")
print(piano.armonicos, piano.module)


