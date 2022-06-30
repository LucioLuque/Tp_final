class ReadInstrument:
    def __init__(self, filename):
        self.filename=filename
    
    def read(self):
        armonics={}
        modulations={}
        
        with open (self.filename, 'r') as f:
            amount_armonics= int(f.readline())
            for line in range(1,amount_armonics+1):
                line=f.readline().strip().split(" ")
                armonics[int(line[0])]= float(line[1])

            module_lines=(f.readlines())
    
            attack=module_lines[0].strip().split(" ")
            sustained=(module_lines[1].strip())
            decay=(module_lines[2].strip().split(" "))

            modulations[attack[0]]=float(attack[1])
            modulations[sustained]=[]
            modulations[decay[0]]=float(decay[1])
            
        return armonics, modulations

class ReadPartiture:
    def __init__(self, filename_partiture):
        self.filename_partiture = filename_partiture
        
    def read_partiture(self):
        list_of_notes = []
        with open (self.filename_partiture, 'r') as f:
            
            for line in f:
                line=line.strip().split(' ')
                starts=float(line[0])
                type=line[1]
                duration=float(line[2])
                list_of_notes.append((starts, type, duration))
        return list_of_notes