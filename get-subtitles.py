#!/usr/bin/env python

'''
Python script to find and download the subs for an episode specified on the command line.
The resulting sub is put in the file <episode specified>.srt

Example usage and result:

$ ./getsubs.py Yonkers.Nine-Nine.S02E12.HDTV.x264-ASAP
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

base = 'http://subscene.com/'
fullurl = base + 'subtitles/release?q=' + encodedepisodename
print fullurl	# the search URL

# Search that episode name:
data = urllib2.urlopen(fullurl)
# parse the lines in the search results
found = False
for line in data:
    # grep -e '<a href="/subtitles/' | grep -vi "also try"
    # find the first line that contains '<a href="/subtitles/' with the correct language and not "also try":
    if line.find('<a href="/subtitles/')>=0 and line.find(language)>=0 and line.lower().find("also try")<0:
        found = line.rstrip().split('"')[1]
	# we expect the first hit is OK, so quit the for loop:
	break

if not found:
    print "No match found. Exiting"
    exit(1)


# We now get the details of that hit (which is a link to a ZIP file):
subsurl = base + found
print subsurl
data = urllib2.urlopen(subsurl)
for line in data:
    # grep 'subtitle/download'
    #   18. http://subscene.com/subtitle/download?mac=nz2mvrLUGIrRLlkJEQKIM1bLF_YeiqKwsB62_ws6DQHyreLtvwFB5_Ifk9Arg3tr0
    if line.find('subtitle/download')>=0:
	subs = line.rstrip().split('"')[1]
	break

# Now get the zip file that the above URL is pointing to:
realsubsurl = base + subs
print realsubsurl
import shutil
subszipfile = "mysubs.zip"	# temp name
req = urllib2.urlopen(realsubsurl)
with open(subszipfile, 'wb') as fp:
    shutil.copyfileobj(req, fp)

# Now unzip that downloaded zip file, which contains the subs in it:
import zipfile
fh = open(subszipfile, 'rb')
z = zipfile.ZipFile(fh)
for name in z.namelist():
    print name
    z.extract(name)
    # Copy the unpacked subs file name to the name of the episode searched for
    # This is handy for VLC; it will automatically pick up the subs files
    extension = name.split('.')[-1]	# probably 'srt'
    newname = episodename + '.' + extension
    print newname
    try:
        shutil.copy(name,newname)
    except:
        print "Could not write to ", newname
        pass
fh.close()





