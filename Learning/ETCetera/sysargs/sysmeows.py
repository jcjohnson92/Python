import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument('-n', help="number of times to meow", type=int)
parser.add_argument('-s', help="speak of times to meow", type=str)

args = parser.parse_args()

for _ in range(int(args.n)):
    print(args.s)