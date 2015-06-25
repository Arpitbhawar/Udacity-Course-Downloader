import os
import pycurl
import sys


def progress(total, existing, upload_t, upload_d):
    try:
        frac = float(os.path.getsize(filename))/float(total)
    except:
        frac = 0
    sys.stdout.write("\r%s %3i%%" % (filename +" ", frac*100)  )

def test(debug_type, debug_msg):
    print "debug(%d): %s" % (debug_type, debug_msg)

def download(url):
	c = pycurl.Curl()
	c.setopt(pycurl.URL, url)
	c.setopt(pycurl.FOLLOWLOCATION, 1)
	c.setopt(pycurl.MAXREDIRS, 5)

	# Setup writing
	if os.path.exists(filename):
	    f = open(filename, "ab")
	    c.setopt(pycurl.RESUME_FROM, os.path.getsize(filename))
	else:
	    f = open(filename, "wb")
	try:
		c.setopt(pycurl.WRITEDATA, f)
		#c.setopt(pycurl.VERBOSE, 1)
		c.setopt(pycurl.DEBUGFUNCTION, test)
		c.setopt(pycurl.NOPROGRESS, 0)
		c.setopt(pycurl.PROGRESSFUNCTION, progress)
		c.perform()
	except:
		print("downloaded")

#url = "http://video.udacity-data.com/zip/cs212/Unit_7-subtitles.en.zip"
url="http://video.udacity-data.com/zip/cs212/Unit_1.zip"
filename = url.split("/")[-1].strip()

download(url)