"example of a synthesizer"
from synthesizer import *
from datetime import datetime

instanteInicial = datetime.now()
s=Synthesizer("BlackBird.txt", "piano.txt").create_wav("Black", 44100)

instanteFinal = datetime.now()
print(instanteFinal - instanteInicial)