import BaseHTTPServer
import argparse
import datetime
import httplib
import sys
import time
import subprocess
import urllib2
import trafficstats
from optparse import OptionParser

#option parser to add flags and defaults
parser = OptionParser()
parser.add_option("--url", "-u", type="string", default="http://localhost:8080")
parser.add_option("--interval", "-i", type="int", default="10")

(options,args) = parser.parse_args(sys.argv)

#store input from user
url = options.url
interval = options.interval
	
#open output file to write to
f = open('output.txt', 'w')

#infinate loops
while True:
	#open webstats page
	webStats = urllib2.urlopen(url + "/stats")
	
	#get html from stats page
	webStatsRaw = webStats.read()

	#split outputs into array by newline
	outputs = webStatsRaw.split("\n")
	
	#delete the last line
	del outputs[-1]
	
	#loop through, split by colon to get only values
	for var in outputs:
		outputs = var.split(":")
		f.write(outputs[1].strip()+"\t")

	#write a new line to file
	f.write("\n")

	#sleep for however long user wants
	time.sleep(interval)

