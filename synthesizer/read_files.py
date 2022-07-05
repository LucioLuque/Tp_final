from useful_func import *


class ReadInstrument:
    def __init__(self, filename):
        """
        Parameters
        ----------
        filename : str
            The name of the file containing the instrument
        """
        if type(filename) != str:
            raise TypeError
        self.filename=filename
    
    def read(self):
        """
        Reads the instrument file and returns two dictionaries.
        The first dictionary contains the armonics of the instrument.
        The second dictionary contains the modulations of the instrument.
        """
        armonics={}
        modulations=[]
        with open (self.filename, 'r') as f:
            amount_armonics= f.readline().strip()
            if amount_armonics.isnumeric() == False:
                raise TypeError 
            amount_armonics= int(amount_armonics)
            for line in range(0,amount_armonics):#read the armonics
                line=f.readline().strip().split(" ")
                if len(line) < 2:
                    raise ValueError
                else:
                    if (isfloat(line[0]) or isfloat(line[1])) ==False:
                        raise TypeError
                armonics[int(line[0])]= float(line[1])

            module_lines=(f.readlines())#read the modulations
            if len(module_lines) < 3:
                raise ValueError
            for line in module_lines:
                l=[]
                line=line.strip().split(" ")
                for i in range(0,len(line)):
                    if i!=0:
                        if isfloat(line[i]) == False:
                            raise ValueError
                        l.append(float(line[i]))
                    else:
                        if line[i].isalpha() == False:
                            raise ValueError
                        l.append((line[i]))
                modulations.append(l)
        return armonics,modulations

class ReadPartiture:
    def __init__(self, filename_partiture):
        """
        Parameters
        ----------
        filename_partiture : str
            The name of the file containing the partiture
        """
        if type(filename_partiture) != str:
            raise TypeError
        self.filename_partiture = filename_partiture
    def attack_is_minor_than_duration(self, note, attack):
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
        
        if (note[2])<attack:
            return False
        return True
    def read_partiture(self, attack, decay):
        """
        Reds the partiture file and returns a list of notes.
        Each note is a tuple of the form (start:float, name:str, duration:float).
        """
        list_of_notes = []
        failed_notes=0
        with open (self.filename_partiture, 'r') as f:  
            for line in f:
                line=line.strip().split(' ')
                starts=float(line[0])
                type=line[1]
                duration=float(line[2])
                if self.attack_is_minor_than_duration((starts,type,duration), attack):
                    list_of_notes.append((starts, type, duration+decay))
                else:
                    failed_notes+=1
            if failed_notes!=0:
                print(f"Warning: There are {failed_notes} notes that are lower than the attack: {attack}, they are not going to reproduce.")
        if len(list_of_notes)==0:
            raise ValueError(f"All the notes are lower than the attack: {attack}")
       
        return list_of_notes