#!/usr/bin/env python

import ssl
# Prints info about the OpenSSL in your python setup

print "OPENSSL_VERSION:", ssl.OPENSSL_VERSION
print "OPENSSL_VERSION_INFO:", ssl.OPENSSL_VERSION_INFO
print "PROTOCOL_SSLv23:", ssl.PROTOCOL_SSLv23
print "PROTOCOL_SSLv3:", ssl.PROTOCOL_SSLv3
print "PROTOCOL_TLSv1:", ssl.PROTOCOL_TLSv1
print "\nModule ssl:", dir(ssl)

