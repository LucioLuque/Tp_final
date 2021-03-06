import numpy as np
from modulation import *

class ModulatedNote:
    def __init__(self, song_frequency: int, duration: float, modulations:list):
        """
        Parameters
        ----------
        duration : float
            The duration of the note
        modulations : dict
            The modulations of the instrument. See the read_files.py module.
        """
        
        if ((type(song_frequency) != int) or (type(duration) != float) or (type(modulations) != list)):
            print(song_frequency, duration, modulations)
            raise TypeError

        self.song_frequency= song_frequency
        self.duration= duration
        self.modulations= modulations

    def divide_modulation(self):
        """
        Divides the modulations in the modulations dictionary in three lists:
        attack, sustained, decay.
        """
        modulation= self.modulations
        if modulation[0][0]=="TRI":
            first_time=[modulation[0][1], modulation[0][2], modulation[0][3]]
        else:
            first_time= [modulation[0][1]]
        
        second_time= [self.duration-modulation[2][1]]
        
        return modulation, first_time, second_time
    
    def modulation(self, armonic_note: np.ndarray, array_of_note: np.ndarray) -> np.ndarray:
        """
        Returns the modulated note.

        
        Parameters
        ----------
        armonic_note : numpy.ndarray
            The armonic note as a numpy array
        array_of_note : numpy.ndarray
            The note as a numpy array
        
        Returns
        -------
        numpy.ndarray
            The modulated note as a numpy array
        """
        if (type(armonic_note) != np.ndarray or type(array_of_note) != np.ndarray):
            raise TypeError
        modulation, first_time, second_time= self.divide_modulation()
        keys= [modulation[0][0], modulation[1][0], modulation[2][0]]
        

        m= np.empty(int(self.song_frequency*(self.duration)))
        slice1=int(self.song_frequency*first_time[0])
        slice2=int(self.song_frequency*second_time[0])
 
        m[:slice1]=dic_funcs[keys[0]](array_of_note[:slice1], first_time)

        if modulation[1][0]=="PULSES":
            arg=[modulation[1][1],modulation[1][2],modulation[1][3]]
            m[slice1:slice2]=dic_funcs[keys[1]](array_of_note[slice1:slice2]-first_time[0],arg)
        else:
            m[slice1:slice2]=dic_funcs[keys[1]](array_of_note[slice1:slice2]-first_time[0],second_time)
        m[slice2:]=m[slice2-1]*dic_funcs[keys[2]](array_of_note[slice2:]-second_time[0], [self.duration-second_time[0]])

        modulated_note=0.02*m*armonic_note

        return modulated_note

class ArmonicNote:
    def __init__(self, frequency:int, duration:float, armonics:dict):
        """
        Parameters
        ----------
        frequency : float
            The frequency of the note
        duration : float
            The duration of the note
        armonics : dict
            The armonics of the instrument. See the read_files.py module.
        """
        if ((type(frequency) != float) 
        or (type(duration) != float) 
        or (type(armonics) != dict)):
            raise TypeError

        self.frequency= frequency
        self.duration= duration
        self.armonics= armonics

    def get_armonic(self, note:np.ndarray)->np.ndarray:
        """
        Returns the armonic note.
        
        Parameters
        ----------
        note : numpy.ndarray
            The note as a numpy array
        Returns
        -------
        numpy.ndarray
            The armonic note as a numpy array
        """

        if type(note) != np.ndarray:
            raise TypeError

        d=self.armonics
        armonics=np.zeros(len(note))
        for i in d:
            armonics+=(d[i] * np.sin(( (2*np.pi*i*self.frequency * note))))
        return armonics
        
class CreateArrayNote:
    def __init__(self, song_frequency:int, duration:float):
        """
        Parameters
        ----------
        duration : float
            The duration of the note
        """
        if type(song_frequency) != int or type(duration) != float:
            raise TypeError
         

        self.song_frequency= song_frequency
        self.duration = duration

    def array_of_note(self):
        """
        Returns the array of the note.

        Returns
        -------
        numpy.ndarray
            The array of the note as a numpy array
        """
        return np.linspace(0, self.duration,int(self.song_frequency*self.duration))
