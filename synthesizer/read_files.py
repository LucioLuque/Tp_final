class ReadInstrument:
    def __init__(self, filename):
        self.filename=filename
    
    def read(self):
        armonics={}
        modulations=[]
        
        with open (self.filename, 'r') as f:
            amount_armonics= int(f.readline())
            for line in range(0,amount_armonics):
                line=f.readline().strip().split(" ")
                armonics[int(line[0])]= float(line[1])

            module_lines=(f.readlines())
    
            attack=module_lines[0].strip().split(" ")
            sustained=(module_lines[1].strip().split(" "))
            decay=(module_lines[2].strip().split(" "))

            attack_list=[]
            for i in attack:
                if i!=attack[0]:
                    attack_list.append(float(i))
                else:
                    attack_list.append(attack[0])
            modulations.append((attack_list))
            sustained_list=[]
            for i in sustained:
                if i!=sustained[0]:
                    sustained_list.append(float(i))
                else:
                    sustained_list.append(sustained[0])
            modulations.append((sustained_list))
            decay_list=[]
            for i in decay:
                if i!=decay[0]:
                    decay_list.append(float(i))
                else:
                    decay_list.append(decay[0])
            modulations.append((decay_list))

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