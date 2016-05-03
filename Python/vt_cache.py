#!/usr/bin/python

import argparse
import sys
import requests

def main(args):
    if args.action == 'clear':
        r = requests.get('https://api.github.com/sangwon04/%s/max-age=0' % args.hash)
        print 'Clearing cache for %s' % args.hash
        print r.json()
        sys.exit()
    else:
        r = requests.get('https://api.github.com/sangwon04/%s' % args.hash)
        print 'Looking up hash, %s, in cache...' % args.hash
        print r.json()
        sys.exit()

if __name__ == "__main__":
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-a", "--action", choices = ['clear', 'lookup'], help = 'Determines to either \
                           clear the cache or lookup the current cache', required = True)
    argParser.add_argument("-f", "--hash", help = 'This is the hash you wish to lookup', required = True)
    main(argParser.parse_args())
