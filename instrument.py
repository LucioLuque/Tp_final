class ReadInstrument:
    def __init__(self, filename):
        self.filename=filename
    
    def read(self):
        armonics={}
        modulations={}
        with open (self.filename, 'r') as f:
            amount_armonics= int(f.readline())
            for line in range(1,amount_armonics+1):
                line=f.readline().strip()
                line=line.split(' ')
                armonics[int(line[0])]= float(line[1])

            for line in f:
                line=line.strip().split(' ')
                if len(line)==1:
                    modulations[line[0]]= []
                else:
                    modulations[line[0]]= line[1]
        return armonics, modulations

class Instrument:
    def __init__(self, name, filename):
        self.name = name
        self.readinstrument= ReadInstrument(filename)
        self.armonics= None
        self.modulations= None
        self.read()

    def read(self):
        self.armonics, self.modulations=self.readinstrument.read()