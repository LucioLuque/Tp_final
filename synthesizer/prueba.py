from synthesizer import Synthesizer
from datetime import datetime


instanteInicial = datetime.now()
s=Synthesizer(44100, "pais_de_la_libertad.txt", "piano.txt").create_wav()
instanteFinal = datetime.now()
print(instanteFinal - instanteInicial)


