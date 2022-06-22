import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
from modulation import *
class Instrument:
    def __init__(self, name, filename):
        self.name = name
        self.filename = filename
        self.armonicos, self.module=self.get_parameters()

    def get_parameters(self):
        d={}
        m={}
        with open (self.filename, 'r') as f:
            l1=int(f.readline())
            for line in range(1,l1+1):
                line=f.readline().strip()
                line=line.split(' ')
                d[int(line[0])]=float(line[1])

            for line in f:
                line=line.strip().split(' ')
                if len(line)==1:
                    m[line[0]]=[]
                else:
                    m[line[0]]=line[1]
        return d, m

class CreateNote:
    def __init__(self, type, amplitude, frequency, duration, starts, instrument):
        self.type = type
        self.amplitude = amplitude
        self.frequency = frequency
        self.duration = duration
        self.starts = starts
        self.x=np.linspace(0, self.duration,int(44100*self.duration))
        self.armonicos=instrument.armonicos
        self.senoidales=self.get_senoidales()
        self.final_note=self.sum_senoidales()
        self.module=instrument.module

    def get_senoidales(self):
        d=self.armonicos
        senoidales=[]
        for i in d:
            senoidales.append(d[i] * np.sin(( (2*np.pi*i*self.frequency * self.x))))
        return senoidales

    def sum_senoidales(self):
        return sum(self.senoidales)
        
    def module_note(self):
        d=self.module
        print(d.values())
        first_time=float(list(d.values())[0])
        second_time=self.duration-float(list(d.values())[2])
        print(first_time,second_time)
        m=np.zeros(int(44100*self.duration))
        a=np.zeros(int(44100*self.duration))
        for idx,ti in enumerate(self.x):
            if ti<=first_time:
                m[idx]=moduled(list(d.keys())[0], ti, first_time)
                
            elif ti<=second_time:
                m[idx]=moduled(list(d.keys())[1],ti, second_time)
               
            else:
                m[idx]=moduled(list(d.keys())[2],ti-second_time,self.duration-second_time)
                
        a=m*self.final_note
        return a
        
piano=Instrument("piano", "piano.txt")
A4=CreateNote("A4", 1, 440, 2, 0, piano)

x=A4.x
#y=A4.final_note
y=A4.module_note()

plt.plot(x, y)
plt.grid(True)
plt.ylabel('Amplitude')
plt.xlabel("Time (s)")
plt.show()

wavfile.write("A4.wav", 44100, y)


