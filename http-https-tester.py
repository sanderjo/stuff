#!/usr/bin/env python

import urllib2
import sys
import ssl

print "Python version", sys.version

urllist= [
        'http://www.google.com/',
        'https://www.google.com/',
        'http://api.nzbgeek.info/api?t=get&id=xxx&apikey=yy',
        'https://api.nzbgeek.info/api?t=get&id=xxx&apikey=yy',
        'https://api.oznzb.com/api?t=search&q=linux&apikey=5a83asomethingwrong',
        'https://tv.eurosport.nl/',
        'http://does.not.exist/',
	'https://nzbindex.nl/',
	'https://raw.githubusercontent.com/'
    ]


for url in urllist:
        try:
                f = urllib2.urlopen(url, timeout=4)    # timeout 4 seconds, in case website is not accessible
                result = f.read()[:100].replace('\n', ' ').replace('\r', '')
                print "URL ", url, "OK, with result", result
	except urllib2.URLError as e:
                print "URL ", url, "not OK, with error ",  sys.exc_info()[0], "with reason", e  
		pass
	except ssl.CertificateError as e:
                print "URL ", url, "not OK, with error ",  sys.exc_info()[0], "with reason", e 
		pass
	except Exception as e:
                print "URL ", url, "not OK, with error ",  sys.exc_info()[0], "with reason", e 
		pass

print "Finished"
