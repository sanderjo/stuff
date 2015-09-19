#!/usr/bin/env python

# Python implementation of RFC 6555 / Happy Eyeballs: find the quickest IPv4/IPv6 connection
# See https://tools.ietf.org/html/rfc6555


import socket
import ssl
import Queue
import threading
import urllib2


# called by each thread
def do_socket_connect(queue, ip, PORT, SSL, DEBUG):
    # connect to the ip, and put into the queue the result
    #print "Input is", ip, PORT, SSL, DEBUG
    try:
	    # CREATE SOCKET
	    if ip.find(':')>=0 : 
		s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
	    if ip.find('.')>=0 :
		s = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)

	    s.settimeout(5)
	    if not SSL:
		# Connect
		s.connect((ip, PORT))
		# ... and close
		s.close()
	    else:
		# WRAP SOCKET
		wrappedSocket = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1)    
		# CONNECT
		wrappedSocket.connect((address, PORT))
		# CLOSE SOCKET CONNECTION
		wrappedSocket.close()
	    queue.put((ip, "OK"))
    except:
	queue.put((ip, "NOT OK"))
	pass	


def happyeyeballs(HOST, **kwargs):
    try:
        PORT=kwargs['port']
    except:
        PORT=80
    try:
        SSL=kwargs['ssl']
    except:
        SSL=False
    try:
        DEBUG=kwargs['debug']
    except:
        DEBUG=False

    try:
	ipaddresses = []
	allinfo = socket.getaddrinfo(HOST, 80, 0, 0, socket.IPPROTO_TCP)
	for i in allinfo:
	    address = i[4][0]
	    ipaddresses.append(address)
	print ipaddresses

	myqueue = Queue.Queue()

	for ip in ipaddresses:
	    thisthread = threading.Thread(target=do_socket_connect, args = (myqueue,ip, PORT, SSL, DEBUG))
	    thisthread.daemon = True
	    thisthread.start()

	result = None
        for i in range(len(ipaddresses)):
		s = myqueue.get()	# only get a response
		if s[1]=="OK":
			#print "Found"
			result = s[0]
			break

        #print "Quickest", result
	return result
    except:
        return "Error - None"




if __name__ == '__main__':
    print happyeyeballs('www.google.com')
    print happyeyeballs('newszilla.xs4all.nl', port=119)
    print happyeyeballs('www.google.com', port=443, ssl=True)
    print happyeyeballs('www.google.com', port=80, ssl=False)
    print happyeyeballs('block.cheapnews.eu', port=119)
    print happyeyeballs('block.cheapnews.eu', port=443, ssl=True)
    print happyeyeballs('block.cheapnews.eu', port=443, ssl=True, debug=True)
    print happyeyeballs('newszilla.xs4all.nl', port=119)
    print happyeyeballs('does.not.resolve', port=443, ssl=True, debug=True)    
    print happyeyeballs('216.58.211.164')

