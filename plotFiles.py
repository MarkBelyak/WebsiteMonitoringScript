import os
import glob
import time
import sys

#open output files
outputFile = open('output.txt', 'r')
hitOutput = open('200output.txt', 'w')
missingOutput = open('404output.txt', 'w')
failOutput = open('500output.txt', 'w')

#create variables to store current and past outputs
failCurrent = 0
failPast = 0

hitCurrent = 0
hitPast = 0

missingCurrent = 0
missingPast = 0

#variables for iterations
i = 0
x = 0


for line in outputFile:
	
	#every line is 10 seconds, so 6 of them is 1 minute which is why I do this line
	if (i % 6 == 0):

		#doesn't do subtraction for first linr
		if (i == 0):
			#split by tab, then store each output in correct variable
			output = line.split("\t")
			failCurrent = int(output[1])
			hitCurrent = int(output[2])
			missingCurrent = int(output[3])	
			
			#assign current variables to past
			failPast = failCurrent
			hitPast = hitCurrent
			missingPast = missingCurrent
		else:
			x += 1
			
			#split by tab, then store each output in correct variable
			output = line.split("\t")
			failCurrent = int(output[1])
			hitCurrent = int(output[2])
			missingCurrent = int(output[3])
	
			#do subtraction, then assign current variables to past
			failOutput.write(str(x) + "\t" + str((failCurrent - failPast)/60) + "\n")
			failPast = failCurrent
			hitOutput.write(str(x) + "\t"+ str((hitCurrent - hitPast)/60)+ "\n")
			hitPast = hitCurrent	
			missingOutput.write(str(x) + "\t"+ str((missingCurrent - missingPast)/60)+ "\n")
			missingPast = missingCurrent	


	i += 1
