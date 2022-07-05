from xylophone.client import XyloClient
from xylophone.xylo import XyloNote
import argparse

parser = argparse.ArgumentParser(description='Sending musical notes to an instrument')
parser.add_argument('-i', type=str, help='Music Sheet name')
parser.add_argument('-o', type=str, help='Instrument IP')
args = parser.parse_args()

def main():
    """
    This function is responsible for sending the different notes corresponding to the instrument "Metallophone".
    """
    notes = []
    with open (args.i, 'r') as f:
        for line in f:
            line=line.strip().split(' ')
            start_time=float(line[0])
            value = ''
            #Notes are raised and lowered in octaves to be compatible with the instrument
            if len(line[1]) == 2:
                if line[1][0] == 'F' or line[1][0] == 'E' or line[1][0] == 'D' or line[1][0] == 'C':
                    value = line[1][0] + '5'
                elif line[1] == 'C8':
                    value = 'C7'
                elif int(line[1][1]) < 4 and line[1][0] != 'C':
                    value = line[1][0] + '4'
                elif int(line[1][1]) > 6 and line[1][0] != 'C':
                    value = line[1][0] + '6'
                else:
                    value = line[1]
            elif len(line[1]) == 3:
                if line[1][0:2] == 'Eb' or line[1][0:2] == 'Db':
                    value = line[1][0] + line[1][1] + '5'
                elif line[1][0:2] == 'Fb':
                    if int(line[1][2]) <= 4:
                        value = line[1][0] + '4'
                    elif int(line[1][2]) >= 6:
                        value = line[1][0] + '6'
                elif line[1][0:3] == 'Cb4' or line[1][0:3] == 'Cb5':
                    value = 'Cb6'
                elif line[1][0:2] == 'Gb':
                    value = 'Gb6'
                elif int(line[1][2]) < 4:
                    value = line[1][0] + line[1][1] + '4'
                elif int(line[1][2]) > 6:
                    value = line[1][0] + line[1][1] + '6'
                else:
                    value = line[1]
            notes.append(XyloNote(value, start_time, 90))
    #Send the information to the instrument
    client = XyloClient(host=args.o, port=8080)
    client.load(notes)
    client.play()

if __name__ == '__main__':
    main()

