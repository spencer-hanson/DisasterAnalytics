#PROTOTYPE REDUCER FUNCTION

#!/usr/bin/env python
import sys
from operator import itemgetter

current_coord = None
current_count = 0


# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    line=line.strip('(')
    line=line.strip(')')
     # parse the input we got from mapper.py
    lat, Long, count = line.split(',')
    Long=Long.strip(')')
    coordinates=(lat,Long)

    try:
    	count = int(count)
    except ValueError:
    	continue


    if current_coord == coordinates:
    	current_count += count
    else:
    	    	# write result to STDOUT
    	if current_coord:
    		print (current_coord, current_count)
    	current_count = count
    	current_coord = coordinates
    	
#output last word
if current_coord == coordinates:
	print ( current_coord, current_count)
    
