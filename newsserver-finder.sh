lynx --dump http://www.reddit.com/r/usenet/wiki/providers | grep http | awk -F/ '{ print $3 }' | sort -u | grep -e "\."  | awk -F\. '{ print $(NF-1) "."  $NF }' | awk '{ print "news." $1 ; print "reader." $1 }' | awk '{ print "host  " $1 }'   | /bin/sh > newsreaders.txt

cat newsreaders.txt | grep -e  "^news\." -e "^reader\." | awk '{ print "python nntptester.py " $1 }'  | sort -u | /bin/sh | grep -B1 -e "^200"  | grep "Newsserver is"


lynx --dump http://www.reddit.com/r/usenet/wiki/providers | grep http | awk -F/ '{ print $3 }' | sort -u | grep -e "\."  | awk -F\. '{ print $(NF-1) "."  $NF }' | awk '{ print "sslreader." $1 }' | awk '{ print "host  " $1 }'   | /bin/sh > newsreaders-sslreader.txt

cat newsreaders-sslreader.txt | grep -e "^sslreader\." | awk '{ print "python nntptester.py " $1 }'  | sort -u | /bin/sh | grep -B1 -e "^200"  | grep "Newsserver is"
