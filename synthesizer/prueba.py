from synthesizer import Synthesizer
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

instanteInicial = datetime.now()
s=Synthesizer("queen.txt", "piano.txt").create_wav()
instanteFinal = datetime.now()
print(instanteFinal - instanteInicial)

#sintetizador=Synthesizer("queen.txt", "piano.txt").create_wav()

