import math

def CONSTANT(t):
    return 1

def LINEAR(t, to):
    return t/to

def INVLINEAR(t, to):
    lineal = 1 - (t/to)
    if lineal >= 0:
        return lineal 
    else:
        return 0 

def SIN(a, f):
    return (1 + a*(math.sin(f)))

def EXP(t, to):
    return ((math.e)**((5*(t - to))/(to)))

def INVEXP(t,to):
    return ((math.e)**((-5*t)/to))

def QUARTCOS(t, to):
    return math.cos(((math.pi)*t)/(2*to))

def QUARTSIN(t, to):
    return math.sin(((math.pi)*t)/(2*to))

def HALFCOS(t, to):
    return ((1 + math.cos(((math.pi)*t)/(2*to)))/2)

def HALFSIN(t, to):
    return ((1 + math.cos((math.pi)*((t/to)-(1/2))))/2)

def LOG(t ,to):
    return (math.log10(((9*t)/to)+1))

def INVLOG(t, to):
    if t < to:
        return (math.log10(((-9*t)/to)+10))
    else:
        return 0

def TRI(t, to, t1, a1):
    if t < t1:
        return ((t*a1)/t1)
    elif t > t1:
        return (((t-t1)/(t1-to))+a1)

def PULSE(t, to, t1, a1):
    #completar
    return


