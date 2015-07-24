#!/usr/bin/env python

# Tool to measure the connection speed to ALL addresses (IPv4 and IPv6) of a specified NNTP newsserver

import nntplib
import sys
import socket
import time

orig_timeout = socket.getdefaulttimeout()
socket.setdefaulttimeout(2.0)
print "Let's go"

if len(sys.argv) >= 2:
    newsserver = sys.argv[1]
else:
    newsserver = 'block.cheapnews.eu'
    print "No newsserver specified, so using ... ", newsserver

print "Newsserver is", newsserver

for i in socket.getaddrinfo(newsserver, 80, 0, 0, socket.IPPROTO_TCP):
    address = i[4][0]
    print "\nAddress is ", address
    start = time.clock()
    try:
        s = nntplib.NNTP(address)
    except:
        print "Setting up connection went wrong. Exiting."
        sys.exit(1)

    #print s.getwelcome()
    stop = time.clock()
    print "Welcome message took:", 1000*(stop-start), "msec"

socket.setdefaulttimeout(orig_timeout)


