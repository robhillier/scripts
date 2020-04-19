import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('infile',nargs='?', type=argparse.FileType('r'),default=sys.stdin)
parser.add_argument('infile2',nargs='?', type=argparse.FileType('r'))
args = parser.parse_args()


setDifference = set(args.infile.read().splitlines()).difference(args.infile2.read().splitlines())


for item in setDifference:
    print "%s" % item 
