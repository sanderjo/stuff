import urllib2
import sys

try:
    url = sys.argv[1]
except:
    print "specify a URL as parameter"
    sys.exit(0)
print url


print "urlopen:"
try:
    page = urllib2.urlopen(url)
    print "looks good:", page.read()[:100]
except urllib2.HTTPError, e:
    print "HTTPError", e.code
except urllib2.URLError, e:
    print "URLError", e.args
except:
    print "Other error", sys.exc_info()[0]

print "Request, plain:"
try:
    req = urllib2.Request(url) 
    page = urllib2.urlopen(req).read()[:100]
    print "looks good:", page
except urllib2.HTTPError, e:
    print "HTTPError", e.code
except urllib2.URLError, e:
    print "URLError", e.args
except:
    print "Other error", sys.exc_info()[0]

print "Request, with User-Agent header:"
try:
    req = urllib2.Request(url, headers={'User-Agent' : "Some Browser Header"}) 
    page = urllib2.urlopen(req).read()[:100]
    print "looks good:", page
except urllib2.HTTPError, e:
    print "HTTPError", e.code
except urllib2.URLError, e:
    print "URLError", e.args
except:
    print "Other error", sys.exc_info()[0]
