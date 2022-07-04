import numpy as np
from notes import notes_mapping
from note import *
from read_files import *
from scipy.io import wavfile
class Synthesizer:
    def __init__(self, song_frequency, filename_partiture:str, filename_instrument:str):
        """
        Parameters
        ----------
        filename_partiture : str
            The name of the file containing the partiture
        filename_instrument : str
            The name of the file containing the instrument
        """
        self.song_frequency=song_frequency
        self.filename_partiture = filename_partiture
        self.filename_instrument = filename_instrument

    def read_partiture(self):
        """
        Returns a list of notes.
        Each note is a tuple of the form (start:float, name:str, duration:float).
        """
        return ReadPartiture(self.filename_partiture).read_partiture()

    def read_instrument(self):
        """
        Returns two dictionaries.
        The first dictionary contains the armonics of the instrument.
        The second dictionary contains the modulations of the instrument.
        """
        return ReadInstrument(self.filename_instrument).read()

    def get_frequency(self, name: str):
        """
        Get the frequency of a note using the name of the note as a key of the notes_mapping dictionary.
        See notes_mapping.py for the notes_mapping dictionary.
        
        Parameters
        ----------
        name : str
            The name of the note

        Returns
        -------
        float
            The frequency of the note
        """

        if type(name) != str:
            raise TypeError(f"{name} must be str")
        if name not in notes_mapping:
            raise KeyError(f"{name} is not a valid note")
        else:
            return notes_mapping[name]

    def get_max_duration(self, list_of_notes):
        """
        Returns the maximum duration of the notes in the list_of_notes.
        
        Parameters
        ----------
        list_of_notes : list
            The list of notes
            
        Returns
        -------
        float
            The maximum duration of the notes"""
        
        max_duration=max(list_of_notes, key=lambda x: x[0]+x[2])
        return max_duration[0]+max_duration[2]


    def attack_is_minor_than_duration(self, list_of_notes, attack, decay):
        """
        Checks if the attack is minor than the duration of each note plus the decay.
        If the attack is minor than the duration, raise a ValueError.

        Parameters
        ----------
        list_of_notes : list
            The list of notes
        attack : float
            The attack of the instrument
        decay : float
            The decay of the instrument
        
        Raises
        ------
        ValueError
            If the attack is minor than the duration of each note plus the decay
        """
        for i in list_of_notes:
            if (i[2]+decay)<attack:
                raise ValueError(f"The attack={attack} is greater than the duration of the note:{i[2]}+ decay:{decay}")
        return True
        
    
    def compose(self):
        """
        The main function to compose the song.
        Returns the song as a numpy array.
        Returns
        -------
        numpy.ndarray
            The song as a numpy array
        """
        list_of_notes=self.read_partiture()
        armonics, modulations=self.read_instrument()
        decay= modulations[2][1]
        self.attack_is_minor_than_duration(list_of_notes, modulations[0][1], decay)
        max_duration=self.get_max_duration(list_of_notes)
        song_duration=max_duration+decay+1
        song=np.empty(int(song_duration*self.song_frequency))

        for i in list_of_notes:
            starts, name, duration=i
            frequency=self.get_frequency(name)
            duration+=decay #add decay to the duration
            note=self.create_note(duration)
            armonic_note=self.create_armonic_note(frequency, duration, armonics, note)
            modulated_note=self.create_modulation( duration, modulations, armonic_note, note)
            
            start=int(starts*self.song_frequency)
            end=len(modulated_note) + start
            song[start:end]+=modulated_note #add the modulated note to the song

        song[song<-1]=-1 #set the song to -1 if it is less than -1
        song[song>1]=1 #set the song to 1 if it is greater than 1
        return song

    def create_note(self, duration):
        """
        Returns a note of the given duration.
        
        Parameters
        ----------
        duration : float
            The duration of the note
        
        Returns
        -------
        numpy.ndarray
            The note as a numpy array
        """
        return CreateArrayNote(self.song_frequency,duration).array_of_note()

    def create_armonic_note(self, frequency, duration, armonics, note): 
        """
        Returns the armonic note of the given frequency and duration.
        
        Parameters
        ----------
        frequency : float
            The frequency of the note
        duration : float
            The duration of the note
        armonics : dict
            The armonics of the instrument
        note : numpy.ndarray
            The note as a numpy array
        
        Returns
        -------
        numpy.ndarray
            The armonic note as a numpy array
        """
        return ArmonicNote(frequency, duration, armonics).get_armonic(note)

    def create_modulation(self, duration, modulations, armonic_note, note):
        """
        Returns the modulated note of the given duration.

        Parameters
        ----------
        duration : float
            The duration of the note
        modulations : dict
            The modulations of the instrument
        armonic_note : numpy.ndarray
            The armonic note as a numpy array
        note : numpy.ndarray
            The note as a numpy array
        
        Returns
        -------
        numpy.ndarray
            The modulated note as a numpy array
        """
        return ModulatedNote(self.song_frequency, duration, modulations).modulation(armonic_note, note)

    def create_wav(self):
        """
        Creates a wav file of the song. Uses the filename_partiture as the name of the file.
        """

        song=self.compose()
        song_name=self.filename_partiture.replace(".txt", ".wav")
        return wavfile.write(song_name, self.song_frequency,  song)