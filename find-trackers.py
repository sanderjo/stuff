#!/usr/bin/env python

'''
Analysis of trackers in a .torrent file: IPv6 or not

Example usage:

$ python find-trackers.py some-torrent.torrent 
Analysis of the trackers of torrent file some-torrent.torrent
open.demonii.com 2a05:dfc0:1ee4::deee:20
open.demonii.com 2a05:dfc0:1ee4::deee:20
tracker.publicbt.com no IPv6
tracker.openbittorrent.com no IPv6
tracker.istole.it no IPv6
torcache.net no IPv6

$ python find-trackers.py ubuntu-15.04-desktop-amd64.iso.torrent
Analysis of the trackers of torrent file ubuntu-15.04-desktop-amd64.iso.torrent
torrent.ubuntu.com no IPv6
torrent.ubuntu.com no IPv6
ipv6.torrent.ubuntu.com 2001:7b8:3:37::21:3


'''

import sys
import socket

def get_ipv6(host, port=0):
	import socket
	# search only for the wanted v6 addresses
	try:
		result = socket.getaddrinfo(host, port, socket.AF_INET6)[0][4][0]
	except:
		result = None
	return result

####### MAIN #############


try:
	torrentfile = sys.argv[1]
except:
	print "Specify the torrent file as an parameter"
	sys.exit(0)

with open(torrentfile, 'r') as f:
	splitje = f.readline().split('/')
	if splitje[0].find('d8:announce') < 0:
		print "The file" + torrentfile + "does not look like a torrent file"
	else:
		print "Analysis of the trackers of torrent file", torrentfile
		index=0
		while True:
			if splitje[index].find('creation date')>=0:
				# we're past the trackers, so get out of loop:
				break

			# inspect the snippet; it might contain something like 'ipv6.torrent.ubuntu.com:6969'
			part=splitje[index].split(':')[0]
			if part.find('.')>=0:
				# yes, there's is a dot ',', so it might be a FQDN
				ipv6 = get_ipv6(part)
				if ipv6:
					print part, ipv6
				else:
					print part, "no IPv6"
			index+=1

 

