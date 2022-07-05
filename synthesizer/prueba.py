from synthesizer import Synthesizer
from datetime import datetime
import matplotlib.pyplot as plt


instanteInicial = datetime.now()
s=Synthesizer(44100, "queen.txt", "piano.txt").create_wav()
instanteFinal = datetime.now()
print(instanteFinal - instanteInicial)

