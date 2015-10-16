import socket
import logging
import sys
import urllib2

logger = logging.getLogger('')
logger.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s')

# ugly hack:
class MyClass:
    def ipv6_test_host(self):
        return 'test-ipv6.sabnzbd.org'

cfg = MyClass()
print "test_host is", cfg.ipv6_test_host()


#######################################################


def test_ipv6():
    """ Check if external IPv6 addresses are reachable """
    logging.debug("Starting DNS lookup")
    try:
        info = socket.getaddrinfo(cfg.ipv6_test_host(), 80, socket.AF_INET6, socket.SOCK_STREAM, socket.IPPROTO_IP, socket.AI_CANONNAME)
    except:
        logging.debug('Test IPv6: Problem during IPv6 name lookup. Disabling IPv6. Reason: %s', sys.exc_info()[0] )
        return False
    logging.debug("Finished DNS lookup")

    logging.debug("Starting socket connect")

    try:
        af, socktype, proto, canonname, sa = info[0]
        sock = socket.socket(af, socktype, proto)
        sock.settimeout(6)
        sock.connect(sa[0:2])
        sock.close()
        logging.debug('Test IPv6: IPv6 test successful. Enabling IPv6')
        return True
    except socket.error:
        logging.debug('Test IPv6: Cannot reach IPv6 test host. Disabling IPv6')
        return False
    except:
        logging.debug('Test IPv6: Problem during IPv6 connect. Disabling IPv6. Reason: %s', sys.exc_info()[0])
        return False

#######################################################

def test_ipv6_urllib2(host):
    url = 'http://' + host + '/'
    try:
        f = urllib2.urlopen(url, timeout=2)
        result = f.read()[:20]
        logging.debug('Test IPv6: success with urrlib2. %s %s',  url,result )
    except:
        logging.debug('Test IPv6: Problem with urllib2. Disabling IPv6. Reason: %s', sys.exc_info()[0] )
        return False
    return True

# main:

result = test_ipv6()
print "test_ipv6() is", result
test_ipv6_urllib2('ipv6.google.com')	# only use IPv6-only web-enabled hosts!!!
test_ipv6_urllib2('[2a00:1450:400f:804::200e]')
test_ipv6_urllib2('ipv6.test-ipv6.com')





