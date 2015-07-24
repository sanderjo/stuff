#!/usr/bin/env python

# Tool to measure the connection speed to ALL addresses (IPv4 and IPv6) of a specified NNTP newsserver
# This is implementation of RFC 6555 / Happy Eyeballs, without using crafted SYN packets

import nntplib
import sys
import socket
import time

orig_timeout = socket.getdefaulttimeout()
socket.setdefaulttimeout(2.0)
print "Let's go"

shortesttime = 10000000
fastserver = None


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
        #print s.getwelcome()
        delay = 1000.0*(time.clock() - start)
        print "Welcome message took:", delay, "msec"
        if delay < shortesttime:
            shortesttime = delay
            fastserver = address
    except:
        print "Setting up connection went wrong. Exiting."
        pass

print "\nFastest server address:", fastserver
socket.setdefaulttimeout(orig_timeout)


