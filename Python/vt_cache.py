#!/usr/bin/python

import argparse

def main(args):
    print args

if __name__ == "__main__":
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-s", "--sha256", help = 'This is the SHA256 hash you wish to lookup', required = False)
    argParser.add_argument("-m", "--md5", help = 'This is the MD5 has you wish to lookup', required = False)
    main(argParser.parse_args())
