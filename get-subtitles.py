#!/usr/bin/env python

'''
Python script to find and download the subs for an episode specified on the command line.
The resulting sub is put in the file <episode specified>.srt

Example usage and result:

$ ./getsubs.py Yonkers.Nine-Nine.S02E12.HDTV.x264-ASAP

sequentially does this (you simulate from the CLI with lynx and cp / mv commands):

http://subscene.com/subtitles/release?q=Yonkers.Nine-Nine.S02E12.HDTV.x264-ASAP
http://subscene.com//subtitles/Yonkers-nine-nine-second-season/english/1040295
http://subscene.com//subtitle/download?mac=zLLwimFFqqk-uHZbYA4GWcN7lDHHWIpZarWcT4l_j0QlKQyZTDzxeLsx3nG2KES40
Yonkers Nine-Nine - 02x12 - Beach House.ASAP.English.C.orig.Addic7ed.com.srt
Yonkers.Nine-Nine.S02E12.HDTV.x264-ASAP.srt
'''

language = 'english' #Lowercase!!!
''' Example languages, found for an actual episode:
albanian
arabic
brazillian-portuguese
english
farsi_persian
italian
romanian
swedish
vietnamese
'''

import urllib2
import urllib
import sys
episodename = sys.argv[1]	# first argument should be the episode we want the subtitles for
encodedepisodename = urllib.quote_plus(episodename)

base = 'https://subscene.com/'
fullurl = base + 'subtitles/release?q=' + encodedepisodename
print fullurl	# the search URL

headers = { 'User-Agent' : 'Mozilla/5.0' }


req = urllib2.Request(fullurl, None, headers)
data = urllib2.urlopen(req).read()

# Search that episode name:
### data = urllib2.urlopen(fullurl)
# parse the lines in the search results
found = False
for line in data.split('\n'):
    # grep -e '<a href="/subtitles/' | grep -vi "also try"
    # find the first line that contains '<a href="/subtitles/' with the correct language and not "also try":

    if line.find('<a href="/subtitles/')>=0 and line.find(language)>=0 and line.lower().find("also try")<0:
        found = line.rstrip().split('"')[1]
	# we expect the first hit is OK (or at least: the best hit / guess), so quit the for loop:
	break

if not found:
    print "No match found. Exiting"
    exit(1)


# We now get the details of that hit (which is a link to a ZIP file):
subsurl = base + found
print "suburl pointing to subs:", subsurl
req = urllib2.Request(subsurl, None, headers)
data = urllib2.urlopen(req).read()

subs = None	# in case nothing is retrieved
for line in data.split('\n'):
    # grep 'subtitle/download'
    #   18. http://subscene.com/subtitle/download?mac=nz2mvrLUGIrRLlkJEQKIM1bLF_YeiqKwsB62_ws6DQHyreLtvwFB5_Ifk9Arg3tr0
    if line.find('subtitle/download')>=0:
	subs = line.rstrip().split('"')[1]
	break

if not subs:
	print "Strange: no link to zip file found. Exiting"
	exit(1)

# Now get the zip file that the above URL is pointing to:
realsubsurl = base + subs
print "realsubsurl", realsubsurl
import shutil
subszipfile = "mysubs.zip"	# temp name

req = urllib2.Request(realsubsurl, None, headers)
req = urllib2.urlopen(req).read()



'''
myfile = open(subszipfile, "w")
myfile.write(req)
myfile.close()
'''

with open(subszipfile, "w") as outputzipfile:
    outputzipfile.write(req)


# Now unzip that downloaded zip file, which contains the subs we want:
import zipfile
fh = open(subszipfile, 'rb')
z = zipfile.ZipFile(fh)
for name in z.namelist():
    print "name in zip:", name
    z.extract(name)
    # Copy the unpacked subs file name to the name of the episode searched for
    # This is handy for VLC; it will automatically pick up the subs files
    extension = name.split('.')[-1]	# probably 'srt'
    newname = episodename + '.' + extension
    print "copy rename (based on input given) to:", newname
    try:
        shutil.copy(name,newname)
    except:
        print "Could not write to ", newname
        pass
fh.close()





