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

groupedTimings = {}

for line in input:
  values = line.split(" ")
  
  if (len(values) != 2):
    continue
  
  name = values[0]
  time = int(values[1].rstrip())
  
  if (name not in groupedTimings):
    groupedTimings[name] = time
  else:
    groupedTimings[name] += time
  
  
for item in sorted(groupedTimings.items(), key=operator.itemgetter(1), reverse=True):
  print "{0} {1} {2}".format(item[0], item[1], format_millis(item[1]))
  