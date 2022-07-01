import argparse
parser = argparse.ArgumentParser(description="Aca iria la descripcion del programa")
parser.add_argument("Instrument", type=str, help="the instrument used")
parser.add_argument("Partiture", type=str, help= "the partiture")
args = parser.parse_args()

with open(args.Instrument,'r') as f:
    print(f.readlines())

with open(args.Partiture,'r') as p:
    print(p.readline()) 