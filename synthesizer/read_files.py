class ReadInstrument:
    def __init__(self, filename):
        """
        Parameters
        ----------
        filename : str
            The name of the file containing the instrument
        """

        self.filename=filename
    
    def read(self):
        """
        Reads the instrument file and returns a dictionary and a list.
        The dictionary contains the armonics of the instrument.
        The list contains the modulations of the instrument.
        """
        armonics={}
        modulations=[]
        with open (self.filename, 'r') as f:
            amount_armonics= int(f.readline())
            for line in range(0,amount_armonics):#read the armonics
                line=f.readline().strip().split(" ")
                armonics[int(line[0])]= float(line[1])

            module_lines=(f.readlines())#read the modulations
            for line in module_lines:
                l=[]
                line=line.strip().split(" ")
                for i in range(0,len(line)):
                    if i!=0:
                        l.append(float(line[i]))
                    else:
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
        self.filename_partiture = filename_partiture

    def attack_is_minor_than_duration(self, duration, attack):
        """
        Checks if the duration of each note is greater than the attack.
        Prints a warning if the duration is smaller than the attack.It wont be added to the list of notes.
        Returns True if the duration is greater than the attack.
 

        Parameters
        ----------
        duration : float
            The duration of the note
        attack : float
            The attack of the instrument
     
        Returns
        -------
        bool
            True if the duration is greater than the attack. False otherwise.

        """
        if (duration)<=attack:
            return False
        else:
            return True
        
    def read_partiture(self, attack, decay):
        """
        Reads the partiture file.
        It will check if the duration is greater than the attack. See attack_is_minor_than_duration.
        Will add the note to the list if the duration is greater than the attack.
        Will add the decay to the duration of the note.
        Each note is a tuple of the form (start:float, name:str, duration:float).
        
        Parameters
        ----------
        attack : float
            The attack of the instrument
        decay : float
            The decay of the instrument
        
        Returns
        -------
        list
            The list of notes

        """
        failed_notes=0
        list_of_notes = []
        with open (self.filename_partiture, 'r') as f:  
            for line in f:
                line=line.strip().split(' ')
                starts=float(line[0])
                type=line[1]
                duration=float(line[2])
                if self.attack_is_minor_than_duration(duration,attack): 
                    list_of_notes.append((starts, type, duration+decay)) # add decay to the duration
                else:
                    failed_notes+=1
            if failed_notes>0:
                print(f"Warning: There are {failed_notes} notes that are lower than the attack:{attack}, and there are not going to reproduce")

        return list_of_notes