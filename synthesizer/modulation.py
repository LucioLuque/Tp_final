import numpy as np

def CONSTANT(t, tx):
    """
    Returns a constant array of the note.
    """
    if type(t) != np.ndarray or type(tx) != list:
        raise TypeError

    return 1

def LINEAR(t, tx):
    """
    Returns a linear array of the note.

    Parameters
    ----------
    t : ndarray
        The time array
    tx : list
        The times of the note. if used for attack its the time the attack ends, etc.
    
    returns: ndarray
        The linear array of the note.
    
    """

    if type(t) != np.ndarray or type(tx) != list:
        raise TypeError

    return t/tx[0]

def INVLINEAR(t, tx):
    """
    Returns a linear array of the note.

    Parameters
    ----------
    t : ndarray
        The time array
    tx : list
        The times of the note. if used for attack its the time the attack ends, etc.
    
    returns: ndarray
        The invlinear array of the note.
    """

    if type(t) != np.ndarray or type(tx) != list:
        raise TypeError

    lineal = (1 - (t/tx[0]))
    lineal[lineal<=0]=0
    return lineal

def SIN(t,tx):
    """
    Returns a sinusoidal array of the note. f = frequency, a=amplitude.
    
    Parameters
    ----------
    t : ndarray
        The time array
    tx : list
        The times of the note. if used for attack its the time the attack ends, etc.
    
    returns: ndarray
        The sinusoidal array of the note.
    """

    if type(t) != np.ndarray or type(tx) != list:
        raise TypeError
    f=440
    a=0.1
    return (1+ a*(np.sin(f*t)))

def EXP(t, tx):
    """
    Returns a exponential array of the note.
    
    Parameters
    ----------
    t : ndarray
        The time array
    tx : list
        The times of the note. if used for attack its the time the attack ends, etc.
    
    returns: ndarray
        The exponential array of the note.
    """
    if type(t) != np.ndarray or type(tx) != list:
        raise TypeError
    return np.power(np.e,((5*(t - tx[0]))/(tx[0])))

def INVEXP(t,tx):
    """
    Returns a inverse exponential array of the note.
    Parameters
    ----------
    t : ndarray
        The time array
    tx : list
        The times of the note. if used for attack its the time the attack ends, etc.
    
    returns: ndarray
        The inverse exponential array of the note.
    """
    if type(t) != np.ndarray or type(tx) != list:
        raise TypeError
    return np.power(np.e,((-5*t)/tx[0]))

def QUARTCOS(t, tx):
    """
    Returns a cosinusoidal array of the note. f = frequency, a=amplitude.

    Parameters
    ----------
    t : ndarray
        The time array
    tx : list
        The times of the note. if used for attack its the time the attack ends, etc.
    
    returns: ndarray
        The cosinusoidal array of the note.
    """
    if type(t) != np.ndarray or type(tx) != list:
        raise TypeError
    return np.cos(((np.pi)*t)/(2*tx[0]))

def QUARTSIN(t, tx):
    """
    Returns a quadratic sinusoidal array of the note. 

    Parameters
    ----------
    t : ndarray
        The time array
    tx : list
        The times of the note. if used for attack its the time the attack ends, etc.
    
    returns: ndarray
        The quadratic sinusoidal array of the note.
    """
    if type(t) != np.ndarray or type(tx) != list:
        raise TypeError
    return np.sin(((np.pi)*t)/(2*tx[0]))

def HALFCOS(t, tx):
    """
    Returns a cosinusoidal array of the note. f = frequency, a=amplitude.

    Parameters
    ----------
    t : ndarray
        The time array
    tx : list
        The times of the note. if used for attack its the time the attack ends, etc.
    
    returns: ndarray
        The cosinusoidal array of the note.
    """
    if type(t) != np.ndarray or type(tx) != list:
        raise TypeError
    return ((1 + np.cos(((np.pi)*t)/(tx[0])))/2)

def HALFSIN(t, tx):
    """
    Returns a  half sinusoidal array of the note.

    Parameters
    ----------
    t : ndarray
        The time array
    tx : list
        The times of the note. if used for attack its the time the attack ends, etc.
    
    returns: ndarray
        The half sinusoidal array of the note.
    """
    if type(t) != np.ndarray or type(tx) != list:
        raise TypeError
    return (1 + np.sin((np.pi)*((t/tx[0])-(1/2))))/2


def LOG(t ,tx):
    """
    Returns a logarithmic array of the note.
        
    Parameters
    ----------
    t : ndarray
        The time array
    tx : list
        The times of the note. if used for attack its the time the attack ends, etc.
    
    returns: ndarray
        The logarithmic array of the note.
    """

    if type(t) != np.ndarray or type(tx) != list:
        raise TypeError
    return (np.log10(((9*t)/tx[0])+1))

def INVLOG(t, tx):
    """
    Returns a inverse logarithmic array of the note.
        
    Parameters
    ----------
    t : ndarray
        The time array
    tx : list
        The times of the note. if used for attack its the time the attack ends, etc.
    
    returns: ndarray
        The inverse logarithmic array of the note.
    """

    if type(t) != np.ndarray or type(tx) != list:
        raise TypeError
    invlog=np.zeros(len(t))
    invlog[t<tx]= (np.log10(((-9*t[t<tx])/tx[0])+10))
    invlog[t>=tx[0]]=0
    return invlog


def TRI(t, tx):
    """
    Returns a tri array of the note.
            
    Parameters
    ----------
    t : ndarray
        The time array
    tx : list
        The times of the note. if used for attack its the time the attack ends, etc.
    
    returns: ndarray
        The tri array of the note.
    """

    if type(t) != np.ndarray or type(tx) != list:
        raise TypeError
    t0,t1,a1=tx
    tri=t
    tri[:int(t1*44100)]=((tri[:int(t1*44100)])*a1)/t1
    tri[int(t1*44100):]=(((tri[int(t1*44100):])-t1)/(t0-t1))+a1

    tri[tri>1]=1
    return tri

def PULSES(t, tx):
    """
    Returns a pulses array of the note.
                
        Parameters
        ----------
        t : ndarray
            The time array
        tx : list
            The times of the note. if used for attack its the time the attack ends, etc.
        
        returns: ndarray
            The pulses array of the note.
        """
    if type(t) != np.ndarray or type(tx) != list:
        raise TypeError
    t0,t1,a1=tx
    t2=(t/t0)-np.floor(t/t0)
    pulses=np.clip(abs( ( (1-a1) / t1 ) * (t2-t0+t1) ) + a1,None,1)
    return pulses

dic_funcs={'CONSTANT':CONSTANT, 'LINEAR':LINEAR, 'INVLINEAR':INVLINEAR, 'SIN':SIN, 'EXP':EXP, 'INVEXP':INVEXP, 'QUARTCOS':QUARTCOS, 'QUARTSIN':QUARTSIN, 'HALFCOS':HALFCOS, 'HALFSIN':HALFSIN, 'LOG':LOG, 'INVLOG':INVLOG, 'TRI':TRI, 'PULSES':PULSES}
