#!/usr/bin/bash

# This script is a utility script to help generate the signature of the
# Streaming API request using the API secret key

import hashlib
import hmac
import base64
import email.utils
import requests
import logging

# Grab the UUID
# uuid = bytes(raw_input('UUID: '))
uuid = 'cff6e27c-bf01-42ba-a4aa-94abcbf81501'
uuid.encode('utf-8')

# Grab the API key
#sKey = bytes(raw_input('API Secret Key: '))
sKey = 'NmUzZTU5ZjctNGM2NC00ZDI1LWEzYjctMTBlNmNlOTAyNjNm'
sKey.encode('utf-8')

# Sign the request w/ API key
method = 'GET'
content_md5 = base64.b64encode(hashlib.md5("").digest())
date = email.utils.formatdate(localtime=False, usegmt=True)
path = "firehose.crowdstrike.com/sensors/entities/datafeed/v1"
query_string = "?appId=joseph"
requestString = "\n".join([method, content_md5, date, path, query_string])
signature = base64.b64encode(hmac.new(sKey, requestString, hashlib.sha256).digest())
print requestString + '\n'
print "Signature: %r\n\n" % signature

# These two lines enable debugging at httplib level (requests->urllib3->http.client)
# You will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
# The only thing missing will be the response.body which is not logged.
try:
    import http.client as http_client
except ImportError:
    # Python 2
    import httplib as http_client
http_client.HTTPConnection.debuglevel = 1

# You must initialize logging, otherwise you'll not see debug output.
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

# Send the Request
headers = {'X-CS-Date': date, 'Authorization': '%s %s:%s:customers' % ('cs-hmac', uuid, signature) }
r = requests.get('https://' + path + query_string, headers = headers)
print r.status_code
