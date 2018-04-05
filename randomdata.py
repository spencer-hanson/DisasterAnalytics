import csv
import random
lat=24
longitude=-124

with open('eggs.csv', 'w', newline='') as csvfile:
	fieldnames = ['latitude', 'longitude','count']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	while(lat<=49):
		while(longitude<=-44):
			writer.writerow({'latitude': lat, 'longitude': longitude, 'count':random.randint(0,50000)})
			longitude=longitude+1
		lat=lat+1	