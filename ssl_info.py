#!/usr/bin/env python

import ssl
# Prints info about the OpenSSL in your python setup

print "OPENSSL_VERSION:", ssl.OPENSSL_VERSION
print "OPENSSL_VERSION_INFO:", ssl.OPENSSL_VERSION_INFO

print "\nProtocols found:"
for i in dir(ssl):
    #print i
    if i.find('PROTOCOL_') == 0:
        print i

print "\nDetails:"
#print "PROTOCOL_SSLv23:", ssl.PROTOCOL_SSLv23
#print "PROTOCOL_SSLv3:", ssl.PROTOCOL_SSLv3
#print "PROTOCOL_TLSv1:", ssl.PROTOCOL_TLSv1

try:
    print "PROTOCOL_SSLv23:", ssl.PROTOCOL_SSLv23
except:
    print "No PROTOCOL_SSLv23"

try:
    print "PROTOCOL_SSLv3:", ssl.PROTOCOL_SSLv3
except:
    print "No PROTOCOL_SSLv3"
        
try:
    print "PROTOCOL_TLSv1:", ssl.PROTOCOL_TLSv1
except:
    print "No TLSv1"        


try:
    print "PROTOCOL_TLSv1_1:", ssl.PROTOCOL_TLSv1_1
except:
    print "No TLSv1_1"

try:
    print "PROTOCOL_TLSv1_2:", ssl.PROTOCOL_TLSv1_2
except:
    print "No TLSv1_2"


#print "\nModule ssl:", dir(ssl)


