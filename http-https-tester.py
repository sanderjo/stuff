import urllib2
import sys

print "Python version", sys.version

urllist= [
        'http://www.google.com/',
        'https://www.google.com/',
        'http://api.nzbgeek.info/api?t=get&id=xxx&apikey=yy',
        'https://api.nzbgeek.info/api?t=get&id=xxx&apikey=yy',
        'https://tv.eurosport.nl/',
        'http://does.not.exist/'
    ]


for url in urllist:
        try:
                f = urllib2.urlopen(url, timeout=4)    # timeout 4 seconds, in case website is not accessible
                result = f.read()[:100]
                print "URL ", url, "OK, with result", result
        except:
                print "URL ", url, "not OK, with error ",  sys.exc_info()[0]
		pass

print "Finished"
