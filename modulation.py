import numpy as np

from datetime import datetime

class ModulationFunctions:
    def __init__(self):
        pass

    def moduled(self, name, t, t0, a1=None):
        if name=='LINEAR':
            return self.LINEAR(t,t0)
        elif name=='INVLINEAR':
            return self.INVLINEAR(t,t0)
        elif name=='CONSTANT':
            return self.CONSTANT(t) 
        elif name=='SIN':
            return self.SIN(t) 
        elif name=='EXP':
            return self.EXP(t,t0)
        elif name=='INVEXP':
            return self.INVEXP(t,t0)
        elif name=='QUARTCOS':
            return self.QUARTCOS(t) 
        elif name=='QUARTSIN':
            return self.QUARTSIN(t) 
        elif name=='HALCOS':
            return self.HALFCOS(t,t0)
        elif name=='HALFSIN':
            return self.HALFSIN(t,t0)
        elif name=='LOG':
            return self.LOG(t) 
        elif name=='INVLOG':
            return self.INVLOG(t) 
        elif name=='TRI':
            return self.TRI(t,t0,a1)
        elif name=='PULSES':
            return self.PULSES(t,t0,a1)
        

    def CONSTANT(self):
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

    def SIN(self, t):
        f=440
        a=0.1
        return (1 + a*(np.sin(f*t)))

    def EXP(self,t, t0):
        return np.power(np.e,((5*(t - t0))/(t0)))

    def INVEXP(self,t,t0):
        return np.power(np.e,((-5*t)/t0))

    def QUARTCOS(self,t, t0):
        return np.cos(((np.pi)*t)/(2*t0))

    def QUARTSIN(self,t, t0):
        return np.sin(((np.pi)*t)/(2*t0))

    def HALFCOS(self,t, t0):
        return ((1 + np.cos(((np.pi)*t)/(2*t0)))/2)

    def HALFSIN(self,t, t0):
        return ((1 + np.cos((np.pi)*((t/t0)-(1/2))))/2)

    def LOG(self,t ,t0):
        return (np.log10(((9*t)/t0)+1))

    def INVLOG(self,t, t0):
        return (np.log10(((-9*t)/t0)+10))
        
        '''
        if t < t0:
            return (np.log10(((-9*t)/t0)+10))
        else:
            return 0
        '''

    def TRI(self,t, t0, t1, a1):
        if t < t1:
            return ((t*a1)/t1)
        elif t > t1:
            return (((t-t1)/(t1-t0))+a1)

    def PULSES(self,t, t0, t1, a1):
        t2= (t/t0) -np.floor(t/t0)
        return np.min(abs(((1-a1)/t1)*(t2-t0-t1))+a1)#comparar con 1

