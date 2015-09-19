#!/usr/bin/env python

# Python program to find fastest URL based on threading

import Queue
import threading
import urllib2

# called by each thread
def get_url(queue, url):
    try:
        result = urllib2.urlopen(url).read()
        queue.put((url, result))
    except:
        pass # just ignore the problem


theurls = ["http://yahoo.com/", "http://nu.nl/", "http://google.com/", "http://does.not.exist/" ]

myqueue = Queue.Queue()

for url in theurls:
    thisthread = threading.Thread(target=get_url, args = (myqueue,url))
    thisthread.daemon = True
    thisthread.start()

s = myqueue.get()	# only get one (and thus fastest) response. So: no join()

print "Fastest URL is", s[0], "with content ", s[1][:40]
