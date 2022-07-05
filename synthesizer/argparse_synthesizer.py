import argparse
from synthesizer import Synthesizer
parser = argparse.ArgumentParser(description="Create a .wav file using a partiture and an instrument")
parser.add_argument("-p", type=str, help= "The Partiture")
parser.add_argument("-i", type=str, help="The Instrument")
parser.add_argument("-o", type=str, help="The name of the output file")
parser.add_argument("-f", type=int, help="The sample rate")

args = parser.parse_args()

Synthesizer(args.p, args.i).create_wav(args.o,args.f)