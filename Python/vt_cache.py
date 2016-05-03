#!/usr/bin/python

import argparse
import requests
import re

def main(args):
    host = "internal-csapi01-b-720977126.us-west-1.elb.amazonaws.com:8080"

    if args.action == 'clear':
        url = "http://%s/csapi/virustotal/vtresults/%s?maxAge=0" % (host, args.hash)

        try:
            r = requests.get(url)
            r = str(r.json()).split("scan_date", 1)[1]
            print 'Cleared %s from cache!\n' % args.hash
            print "==================================\nANALYSIS DATE: %s\n==================================\n" % r[4:23]
            return
        except:
            if len(args.hash) != 64:
                print "\'%s\' is not a valid SHA256 hash." % args.hash
            return
    else:
        url = "http://%s/csapi/virustotal/vtresults/%s" % (host, args.hash)

        try:
            r = requests.get(url)
            r = str(r.json()).split("scan_date", 1)[1]
            print 'Looking up hash, %s, in cache...\n' % args.hash
            print "==================================\nANALYSIS DATE: %s\n==================================\n" % r[4:23]
            return
        except:
            if len(args.hash) != 64:
                print "\'%s\' is not a valid SHA256 hash." % args.hash
            return

if __name__ == "__main__":
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-a", "--action", choices = ['clear', 'lookup'], help = 'Determines to either \
                           clear the cache or lookup the current cache', required = True)
    argParser.add_argument("-f", "--hash", help = 'This is the hash you wish to lookup', required = True)
    main(argParser.parse_args())
