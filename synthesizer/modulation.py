import numpy as np
def CONSTANT():
    return 1

def LINEAR(t, t0):
    return t/t0

def INVLINEAR(t, t0):

    lineal = (1 - (t/t0))
    lineal[lineal<0]=0
    return lineal

def SIN(t,t0):
    f=440
    a=0.1
    return (1 + a*(np.sin(f*t)))

def EXP(t, t0):
    return np.power(np.e,((5*(t - t0))/(t0)))

def INVEXP(t,t0):
    return np.power(np.e,((-5*t)/t0))

def QUARTCOS(t, t0):
    return np.cos(((np.pi)*t)/(2*t0))

def QUARTSIN(t, t0):
    return np.sin(((np.pi)*t)/(2*t0))

def HALFCOS(t, t0):
    return ((1 + np.cos(((np.pi)*t)/(2*t0)))/2)

def HALFSIN(t, t0):
    return ((1 + np.cos((np.pi)*((t/t0)-(1/2))))/2)

def LOG(t ,t0):
    return (np.log10(((9*t)/t0)+1))

def INVLOG(t, t0):
    invlog= (np.log10(((-9*t)/t0)+10))
    invlog[t>=t0]=0
    return invlog

def TRI(t, t0, t1, a1):
    tri=t
    tri1=(t*a1)/t1
    tri2=((t-t1)/(t1-t0))+a1
    tri[:t1]=tri1
    tri[t1:]=tri2
    return tri

def PULSES(t, t0, t1, a1):
    t2= (t/t0)-np.floor(t/t0)
    pulses=np.absolute(((1-a1)/t1)*(t2-t0-t1)) + a1
    pulses[pulses>1]=1
    return pulses

dic_funcs={'CONSTANT':CONSTANT, 'LINEAR':LINEAR, 'INVLINEAR':INVLINEAR, 'SIN':SIN, 'EXP':EXP, 'INVEXP':INVEXP, 'QUARTCOS':QUARTCOS, 'QUARTSIN':QUARTSIN, 'HALFCOS':HALFCOS, 'HALFSIN':HALFSIN, 'LOG':LOG, 'INVLOG':INVLOG, 'TRI':TRI, 'PULSES':PULSES}