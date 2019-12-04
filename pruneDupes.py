import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('infile',nargs='?', type=argparse.FileType('r'),default=sys.stdin)
args = parser.parse_args()


infilelines = set(args.infile.read().splitlines())

for notDupe in infilelines:
    print "%s" % notDupe 
