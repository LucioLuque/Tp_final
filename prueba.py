import matplotlib.pyplot as plt
from scipy.io import wavfile
from note import *
from instrument import *
from sintetizador import *
from note import *


#instrument=Instrument("piano", "piano.txt")
instanteInicial = datetime.now()

sintetizador=Sintetizador("queen.txt", "piano.txt")

instanteFinal = datetime.now()
tiempo = instanteFinal - instanteInicial
print(tiempo)


y=sintetizador.list_compose
x=sintetizador.x

plt.plot(x, y)
plt.grid(True)
plt.ylabel('Amplitude')
plt.xlabel("Time (s)")
plt.show()

wavfile.write("A4.wav", 44100, y)


