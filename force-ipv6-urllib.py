#--------------------
# do this once at program startup
#--------------------
import socket
origGetAddrInfo = socket.getaddrinfo

def getAddrInfoWrapperIPv6only(host, port, family=0, socktype=0, proto=0, flags=0):
    return origGetAddrInfo(host, port, socket.AF_INET6, socktype, proto, flags)

# replace the original socket.getaddrinfo by our version
socket.getaddrinfo = getAddrInfoWrapperIPv6only

#--------------------
import urllib2

print urllib2.urlopen("http://www.google.com/").read(100)

try:
	print urllib2.urlopen("http://test-ipv6.sabnzbd.org/").read(100)
except:
	print "no ipv6"


# back to normal getaddrinfo, so IPv4 and IPv6 lookup

socket.getaddrinfo = origGetAddrInfo

try:
	print urllib2.urlopen("http://www.python.org/").read(100)
except:
	print "no ipv6"

