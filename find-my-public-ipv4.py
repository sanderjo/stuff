import random
import socket
import urllib2

# list of URLs that will give back the IPv4 address, in plain text, with not any extra at all
resolvelist= [
	'http://4.ifcfg.me/i',
	'http://api.ipify.org',
	'http://echoip.com/',
	'http://ifconfig.me/ip', 
	'http://ip4.telize.com/', 
	'http://ipecho.net/plain',
	'http://ipinfo.io/ip',
	'http://ipv4.icanhazip.com/',
	'http://ipv4.myexternalip.com/raw',
	'https://ipv4.wtfismyip.com/text',
	'http://v4.ident.me/',
	'http://wgetip.com/'
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
if public_ipv4: print "Found in loop", i+1, "via", resolvelist[i]
