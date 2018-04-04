#PROTOTYPE MAP FUNCTION

#!/usr/bin/env python
import sys

for line in sys.stdin:
   
    line = line.strip()
    # split the line into words
    words = line.split()


    # Set up counter tuple
    #Assumes Lat is first line entry and Long is 2nd line entry
    latLong= words[0], words[1]
    counterTup= latLong,1
    print(counterTup)