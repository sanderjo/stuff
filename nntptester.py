#!/usr/bin/env python

import nntplib
import sys
import socket

orig_timeout = socket.getdefaulttimeout()
socket.setdefaulttimeout(2.0)
print "Let's go"

if len(sys.argv) >= 2:
	newsserver = sys.argv[1]
else:
	newsserver = 'newszilla.xs4all.nl'
	print "No newsserver specified, so using ... ", newsserver

print "Newsserver is", newsserver

try:
	s = nntplib.NNTP(newsserver)
except:
	print "Setting up connection went wrong. Exiting."
	sys.exit(1)

print s.getwelcome()
print s.help()
print s.quit()
socket.setdefaulttimeout(orig_timeout)


