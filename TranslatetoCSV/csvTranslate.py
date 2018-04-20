import csv
import sys

with open('testFinalData.csv', 'w', newline='') as csvfile:
	fieldnames = ['latitude', 'longitude','count']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	
	#mapTest --> CHANGE ME
	with open('mapTest.txt') as oldFile:
		#content = oldFile.readlines()
		for line in oldFile:
			line=line.strip('\n')
			line=line.strip('(')
			line=line.strip(')')
			lat,Long,count=line.split(',')
			writer.writerow({'latitude': lat, 'longitude': Long, 'count':count})



	

