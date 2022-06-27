import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
from note import *
from instrument import *
from sintetizador import *

instrument=Instrument("piano", "piano.txt")
print(instrument.armonics, instrument.modulations)
sintetizador=Sintetizador("queen.txt", instrument)

y=sintetizador.list_compose
x=sintetizador.x

plt.plot(x, y)
plt.grid(True)
plt.ylabel('Amplitude')
plt.xlabel("Time (s)")
plt.show()

wavfile.write("A4.wav", 44100, y)


