#!/usr/bin/bash

# This script is a utility script to help generate the signature of the
# Streaming API request using the API secret key

import hashlib
import hmac
import base64

sKey = input("API Secret Key: ")

signature = base64.b64.encode(hmac.new(sKey, digestmod=hashlib.sha256).digest())
print "Signature: %r" % signature
