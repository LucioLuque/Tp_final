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

class Instrument:
    def __init__(self, filename):
        self.readinstrument= ReadInstrument(filename)
        self.armonics= None
        self.modulations= None
        self.read()

    def read(self):
        self.armonics, self.modulations=self.readinstrument.read()