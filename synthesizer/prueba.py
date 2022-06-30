from synthesizer import Synthesizer
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

instanteInicial = datetime.now()
s=Synthesizer("queen.txt", "piano.txt")
#s=Synthesizer("queen.txt", "piano.txt").compose()
#x=np.arange(0, len(s), 1)
#plt.plot(x, s)
#plt.show()


#sintetizador=Synthesizer("queen.txt", "piano.txt").create_wav()


instanteFinal = datetime.now()
print(instanteFinal - instanteInicial)
