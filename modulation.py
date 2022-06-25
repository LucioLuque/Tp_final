import math

def moduled(name, t, t0):
    if name=='LINEAR':
        return LINEAR(t,t0)
    elif name=='INVLINEAR':
        return INVLINEAR(t,t0)
    elif name=='CONSTANT':
        return CONSTANT(t)
    



def CONSTANT(t):
    return 1

def LINEAR(t, t0):
    return t/t0

def INVLINEAR(t, t0):
    lineal = (1 - (t/t0))
    if lineal >= 0:
        return lineal 
    else:
        return 0 

def SIN(a, f):
    return (1 + a*(math.sin(f)))

def EXP(t, t0):
    return ((math.e)**((5*(t - t0))/(t0)))

def INVEXP(t,t0):
    return ((math.e)**((-5*t)/t0))

def QUARTCOS(t, t0):
    return math.cos(((math.pi)*t)/(2*t0))

def QUARTSIN(t, t0):
    return math.sin(((math.pi)*t)/(2*t0))

def HALFCOS(t, t0):
    return ((1 + math.cos(((math.pi)*t)/(2*t0)))/2)

def HALFSIN(t, t0):
    return ((1 + math.cos((math.pi)*((t/t0)-(1/2))))/2)

def LOG(t ,t0):
    return (math.log10(((9*t)/t0)+1))

def INVLOG(t, t0):
    if t < t0:
        return (math.log10(((-9*t)/t0)+10))
    else:
        return 0

def TRI(t, t0, t1, a1):
    if t < t1:
        return ((t*a1)/t1)
    elif t > t1:
        return (((t-t1)/(t1-t0))+a1)

def PULSE(t, t0, t1, a1):
    #completar
    return


