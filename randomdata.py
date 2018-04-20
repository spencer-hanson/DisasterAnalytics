import csv
import random
lat=24
longitude=-124

with open('eggs.csv', 'w', newline='') as csvfile:
	fieldnames = ['latitude', 'longitude','1990', '2000']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	while(lat<=49):
		while(longitude<=-70):
			writer.writerow({'latitude': lat, 'longitude': longitude, '1990':random.randint(0,500), '2000':random.randint(0,500)})
			longitude=longitude+1
		longitude=-124
		lat=lat+1	