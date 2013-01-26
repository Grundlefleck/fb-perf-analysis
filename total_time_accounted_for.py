#! /usr/bin/env python

import sys
import operator
import datetime

def format_millis(millis):
  minutes, remainder = divmod(millis, 1000*60)
  seconds, remainder = divmod(remainder, 1000)
  return "%02d:%02d:%d" % (minutes, seconds, remainder)

inputFile = sys.argv[1]

input = open(inputFile, 'r')

totalTime = 0

for line in input:
  values = line.split(" ")
  
  if (len(values) != 2):
    continue
  
  time = int(values[1].rstrip())
  totalTime += time
  
 
print "{0} {1}".format(totalTime, format_millis(totalTime))
  