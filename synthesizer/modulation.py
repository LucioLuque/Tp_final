import numpy as np
def CONSTANT(t, tx):
    return 1

def LINEAR(t, tx):
    return t/tx

def INVLINEAR(t, tx):
    print(tx[0])
    lineal = (1 - (t/tx))
    lineal[lineal<0]=0
    return lineal

def SIN(t,tx):
    f=440
    a=0.1
    return (1 + a*(np.sin(f*t)))

def EXP(t, tx):
    return np.power(np.e,((5*(t - tx))/(tx)))

def INVEXP(t,tx):
    return np.power(np.e,((-5*t)/tx))

def QUARTCOS(t, tx):
    return np.cos(((np.pi)*t)/(2*tx))

def QUARTSIN(t, tx):
    return np.sin(((np.pi)*t)/(2*tx))

def HALFCOS(t, tx):
    return ((1 + np.cos(((np.pi)*t)/(2*tx)))/2)

def HALFSIN(t, tx):
    return ((1 + np.cos((np.pi)*((t/tx)-(1/2))))/2)

def LOG(t ,tx):
    return (np.log10(((9*t)/tx)+1))

def INVLOG(t, tx):
    invlog= (np.log10(((-9*t)/tx)+10))
    invlog[t>=tx]=0
    return invlog

def TRI(t, tx):
    t0=tx[0]
    t1=tx[1]
    a1=tx[2]
    tri=t
    tri[:int(t1*44100)]=(t[:int(t1*44100)]*a1)/t1
    tri[int(t1*44100):]=((t[int(t1*44100):]-t1)/(t1-t0))+a1
    return tri

def PULSES(t, tx):
    t0=tx[0]
    t1=tx[1]
    a1=tx[2]
    t2=(t/t0)-np.floor(t/t0)
    pulses=np.absolute(((1-a1)/t1)*(t2-t0-t1)) + a1
    pulses[pulses>1]=1
    return pulses

dic_funcs={'CONSTANT':CONSTANT, 'LINEAR':LINEAR, 'INVLINEAR':INVLINEAR, 'SIN':SIN, 'EXP':EXP, 'INVEXP':INVEXP, 'QUARTCOS':QUARTCOS, 'QUARTSIN':QUARTSIN, 'HALFCOS':HALFCOS, 'HALFSIN':HALFSIN, 'LOG':LOG, 'INVLOG':INVLOG, 'TRI':TRI, 'PULSES':PULSES}