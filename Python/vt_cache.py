#!/usr/bin/python

import argparse

def usage():
    print 'usage: vt_cache.py '

def main(args):
    print args

if __name__ == "__main__":
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-a", "--first", help = 'help me', required = True)
    argParser.add_argument("-b", "--second", help = 'help me, too', required = False)
    main(argParser.parse_args())
