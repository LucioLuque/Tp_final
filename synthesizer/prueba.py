from synthesizer import Synthesizer
from datetime import datetime
import matplotlib.pyplot as plt


instanteInicial = datetime.now()
s=Synthesizer("BlackBird.txt", "piano.txt").create_wav()
instanteFinal = datetime.now()
print(instanteFinal - instanteInicial)

#sintetizador=Synthesizer("queen.txt", "piano.txt").create_wav()

