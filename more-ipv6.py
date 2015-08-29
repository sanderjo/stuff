import urllib
import urllib2

import socket
print "timeout", socket.getdefaulttimeout()
socket.setdefaulttimeout(2) # timeout in seconds 
print "timeout", socket.getdefaulttimeout()


def test_ipv6(host):
    """ Check if external IPv6 addresses are reachable """
    # Use google.com to test IPv6 access
    try:
	# only ask for AF_INET6 address: AAAA / IPv6
        info = socket.getaddrinfo(host, 80, socket.AF_INET6, socket.SOCK_STREAM,
                                  socket.IPPROTO_IP, socket.AI_CANONNAME)
    except:
        return "Resolve problem"

    try:
        af, socktype, proto, canonname, sa = info[0]
        sock = socket.socket(af, socktype, proto)
        sock.settimeout(2)
        sock.connect(sa[0:2])
        sock.close()
        return True
    except:
        return "Socket problem"

def checkIPv6(fqdn):
	try:
		socket.inet_pton(socket.AF_INET6, fqdn)
		# yes, a litteral IPv6 address, to put brackets around it
		url = "http://[" + fqdn + "]/"
	except:
		url = "http://" + fqdn + "/"
	#print "\n\nNow checking:", url
	'''
	f = urllib.urlopen(url)
	print "Good:", f.read()[:100]
	'''

	try:
		f = urllib.urlopen(url)
		print "urllib Good: ", fqdn #f.read()[:100]
	except:
		print "urllib No connection", fqdn

	try:
		f = urllib2.urlopen(url, timeout=2)
		print "urllib2 Good: ", fqdn #f.read()[:100]
	except:
		print "urllib2 No connection", fqdn

	print "test_ipv6 ", fqdn, test_ipv6(fqdn)

for i in range(10):
	print test_ipv6("test-ipv6.sabnzbd.org"), 
print "\n"

checkIPv6("ipv6.google.com")
print "\n"
checkIPv6("test-ipv6.sabnzbd.org")
print "\n"
checkIPv6("2400:cb00:2048:1::6812:29d7")	# note the surrounding [ and ] !
print "\n"
checkIPv6("2400:cb00:2048:1::6812:1")
print "\n"


