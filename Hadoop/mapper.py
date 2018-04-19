#PROTOTYPE MAP FUNCTION

#!/usr/bin/env python
import sys

for line in sys.stdin:
   
    line = line.strip()
    # split the line into words
    words = line.split()


    # Set up counter tuple
    #Assumes Lat is first line entry and Long is 2nd line entry
    lat=int(float(words[0]))
    Long=int(float(words[1]))
    if(lat>=24 and lat<=49 and Long>=-124 and Long<=-44): 
    	#latLong= lat, Long
    	#counterTup= latLong,1
    	print("%d,%d,1" %(lat, Long))
    else:
    	continue	