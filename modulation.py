import math
import numpy as np

from datetime import datetime

class ModulationFunctions:
    def __init__(self):
        pass

    def moduled(self, name, t, t0):
        if name=='LINEAR':
            return self.LINEAR(t,t0)
        elif name=='INVLINEAR':
            return self.INVLINEAR(t,t0)
        elif name=='CONSTANT':
            return self.CONSTANT(t) 

    def CONSTANT(self, t):
        return 1

    def LINEAR(self,t, t0):
        return t/t0

    def INVLINEAR(self,t, t0):
        


        lineal = (1 - (t/t0))
        for idx, i in enumerate(lineal):
            if i <0:
                lineal[idx:]=0
                # al final de la partida
                
                break

        return lineal

    def SIN(self,a, f):
        return (1 + a*(math.sin(f)))

    def EXP(self,t, t0):
        return ((math.e)**((5*(t - t0))/(t0)))

    def INVEXP(self,t,t0):
        return ((math.e)**((-5*t)/t0))

    def QUARTCOS(self,t, t0):
        return math.cos(((math.pi)*t)/(2*t0))

    def QUARTSIN(self,t, t0):
        return math.sin(((math.pi)*t)/(2*t0))

    def HALFCOS(self,t, t0):
        return ((1 + math.cos(((math.pi)*t)/(2*t0)))/2)

    def HALFSIN(self,t, t0):
        return ((1 + math.cos((math.pi)*((t/t0)-(1/2))))/2)

    def LOG(self,t ,t0):
        return (math.log10(((9*t)/t0)+1))

    def INVLOG(self,t, t0):
        if t < t0:
            return (math.log10(((-9*t)/t0)+10))
        else:
            return 0

    def TRI(self,t, t0, t1, a1):
        if t < t1:
            return ((t*a1)/t1)
        elif t > t1:
            return (((t-t1)/(t1-t0))+a1)

    def PULSES(self,t, t0, t1, a1):
        t2= (t/t0) -abs(t/t0)
        return np.min(abs(((1-a1)/t1)*(t2-t0-t1))+a1)

