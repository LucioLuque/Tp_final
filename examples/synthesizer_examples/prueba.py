from synthesizer import *
from datetime import datetime


instanteInicial = datetime.now()

sintetizador=Synthesizer("queen.txt", "piano.txt").create_wav()

instanteFinal = datetime.now()
print(instanteFinal - instanteInicial)
