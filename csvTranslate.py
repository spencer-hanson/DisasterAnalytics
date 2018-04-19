import csv
import sys

with open('testFinalData.csv', 'w', newline='') as csvfile:
	fieldnames = ['latitude', 'longitude','count']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	
	with open('mapTest.txt') as oldFile:
		#content = oldFile.readlines()
		for line in oldFile:
			line=line.strip('\n')
			lat,Long,count=line.split(',')
			writer.writerow({'latitude': lat, 'longitude': Long, 'count':count})



	

