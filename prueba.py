import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
from note import *
from instrument import *

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

wavfile.write("A4.wav", 44100, y)


