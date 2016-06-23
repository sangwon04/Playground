#!/usr/bin/python

import argparse, requests, re

def main(args):
    host = "internal-csapi01-b-720977126.us-west-1.elb.amazonaws.com:8080"
    curl = "http://%s/csapi/virustotal/vtresults/%s?maxAge=0" % (host, args.hash)
    lurl = "http://%s/csapi/virustotal/vtresults/%s" % (host, args.hash)

    if len(args.hash) != 64:
        print "\'%s\' is not a valid SHA256 hash." % args.hash
        return

    if args.action == 'clear':
        try:
            r = requests.get(curl)
            r = str(r.json())

            try:
                r = r.split("scan_date", 1)[1]
                r2 = r.split("\"positives\": ", 1)[1]
            except:
                if not r:
                    print "Hash \'%s\' was not found in the VT database." % args.hash
                else:
                    print "Error"
                return

            print 'Cleared %s from cache!' % args.hash
            print "\nANALYSIS DATE: %s" % r[4:23]
            print "POSITIVE HITS: %s\n" % r2[0:1]
            return
        except:
            return
    else:
        url = "http://%s/csapi/virustotal/vtresults/%s" % (host, args.hash)

        try:
            r = requests.get(lurl)
            r = str(r.json())

            try:
                r = r.split("scan_date", 1)[1]
                r2 = r.split("\"positives\": ", 1)[1]
            except:
                if not r:
                    print "Hash \'%s\' was not found in the VT database." % args.hash
                else:
                    print "Error"
                return

            print 'Looking up hash, %s, in cache...' % args.hash
            print "\nANALYSIS DATE: %s" % r[4:23]
            print "POSITIVE HITS: %s\n" % r2[0:1]
            return
        except:
            return

if __name__ == "__main__":
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-a", "--action", choices = ['clear', 'lookup'], help = 'Determines to either \
                           clear the cache or lookup the current cache', required = True)
    argParser.add_argument("-f", "--hash", help = 'This is the hash you wish to lookup', required = True)
    main(argParser.parse_args())
