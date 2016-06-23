#!/usr/bin/bash

# This script is a utility script to help generate the signature of the
# Streaming API request using the API secret key

import hashlib
import hmac
import base64
import email.utils

# uuid = raw_input('UUID: ')
# uuid.encode('utf-8')
sKey = raw_input('API Secret Key: ')
sKey.encode('utf-8')
method = 'GET'
content_md5 = base64.b64encode(hashlib.md5("").digest())
date = email.utils.formatdate(localtime=False, usegmt=True)
path = "firehose.crowdstrike.com/sensors/entities/datafeed/v1"
query_string = "?appId=joseph"

requestString = "\n".join([method, content_md5, date, path, query_string])
signature = base64.b64encode(hmac.new(sKey, requestString, hashlib.sha256).digest())
print "Signature: %r" % signature

# string_to_sign = "\n".join([method, content_md5, date, path, query_string])
# dig = hmac.new(auth.api_key, string_to_sign, hashlib.sha256).digest()
# return base64.b64encode(dig).decode()
