import random
import socket
import urllib2

# list of URLs that will give back the IPv4 address, in plain text, with not any extra at all
resolvelist= [
	'http://api.ipify.org',
	'http://ip4.telize.com/', 
	'http://ifconfig.me/ip', 
	'http://wgetip.com/',
	'http://v4.ident.me/',
	'http://4.ifcfg.me/i',
	'http://ipv4.myexternalip.com/raw',
	'http://ipinfo.io/ip',
	'http://ipv4.icanhazip.com/',
	'http://ipecho.net/plain',
	'http://echoip.com/',
	'https://ipv4.wtfismyip.com/text'
    ]

random.shuffle(resolvelist)	# each randomize the order of the list

maxurls = 3
public_ipv4 = None
for i in range(0,maxurls):
	try:
		f = urllib2.urlopen(resolvelist[i], timeout=2)    # timeout 2 seconds, in case website is not accessible
		public_ipv4 = f.read().rstrip()
 		try:
			socket.inet_pton(socket.AF_INET, public_ipv4)
			# Yes, an IPv4 address!
			break	# we're done
		except:
			pass # continue 
	except:
		pass

print public_ipv4
if public_ipv4: print "Found in loop", i+1
