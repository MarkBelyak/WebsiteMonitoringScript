import BaseHTTPServer
import argparse
import datetime
import httplib
import sys
import time
import trafficstats
import urllib2
import random
from random import randint
from optparse import OptionParser

#option parser to add flags and defaults
parser = OptionParser()
parser.add_option("--url", "-u", type="string", default="http://localhost:8080")
parser.add_option("--rps", "-r", type="int", default="500")
parser.add_option("--jitter", "-j", type="float", default=".1")

(options,args) = parser.parse_args(sys.argv)

#store input from user
url = options.url
rps = options.rps
jitter = options.jitter

#calculate the actual rps using jitter
lower = rps * (1.0  - jitter)
upper = rps * (1.0 + jitter)
actual_rps = random.uniform(lower,upper)

#record start time and period to make sure I do the correct number per second
time_time = time.time
start = time_time()
period = 1.0 / actual_rps
check = True;
while True:
	
	#recalculate rps every second
	lower = rps * (1.0  - jitter)
	upper = rps * (1.0 + jitter)
	actual_rps = random.uniform(lower,upper)
	period = 1.0 / actual_rps

	#create random number to make so I hit every type of error
	randomize = randint(0, 2)
	if (time_time() - start) > period:
		start+= period
		
		try:
			if (randomize == 0):
				check = False
				#open 500 error
				urllib2.urlopen(url+ "/fail")	
		except:
			pass
		try:
			if (randomize == 1):
				if (check):
					check = False
					#open 404 error
					urllib2.urlopen(url+ "/404")
					
		except:
			pass
		if (check):
			#open regular website
			urllib2.urlopen(url)
		check = True
