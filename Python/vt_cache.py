#!/usr/bin/python

import argparse
import sys

def main(args):
    if args.action == 'clear':
        print 'Clearing cache for %s' % args.hash
        sys.exit()
    else:
        print 'Looking up hash, %s, in cache...' % args.hash
        sys.exit()

if __name__ == "__main__":
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-a", "--action", choices = ['clear', 'lookup'], help = 'Determines to either \
                           clear the cache or lookup the current cache', required = True)
    argParser.add_argument("-f", "--hash", help = 'This is the hash you wish to lookup', required = True)
    main(argParser.parse_args())
