import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile

class CreateNote:
    def __init__(self, type, amplitude, frequency, duration, starts):
        self.type = type
        self.amplitude = amplitude
        self.frequency = frequency
        self.duration = duration
        self.starts = starts

A4=CreateNote("A4", 1, 440, 1, 0)


x = np.linspace(A4.starts, A4.duration, int(44100/A4.duration))
y = A4.amplitude * np.sin( 2*np.pi*A4.frequency * x)
plt.plot(x, y)
plt.grid(True)
plt.ylabel('Amplitude')
plt.xlabel("Time (s)")
plt.show()


wavfile.write("A4.wav", 44100, y)


