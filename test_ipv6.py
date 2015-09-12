import socket
import logging
import sys

logger = logging.getLogger('')
logger.setLevel(logging.DEBUG)

# ugly hack:
class MyClass:
    def ipv6_test_host(self):
        return 'test-ipv6.sabnzbd.org'

cfg = MyClass()
print "test_host is", cfg.ipv6_test_host()


#######################################################


def test_ipv6():
    """ Check if external IPv6 addresses are reachable """
    try:
        info = socket.getaddrinfo(cfg.ipv6_test_host(), 80, socket.AF_INET6, socket.SOCK_STREAM, socket.IPPROTO_IP, socket.AI_CANONNAME)
    except:
        logging.debug('Test IPv6: Problem during IPv6 name lookup. Disabling IPv6. Reason: %s', sys.exc_info()[0] )
        return False

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



result = test_ipv6()
print "test_ipv6() is", result


