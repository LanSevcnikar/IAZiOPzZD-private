from geopy.geocoders import Nominatim
import csv

geolocator = Nominatim(user_agent="city_coords")

with open('city_coords.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # skip header row
    for row in csv_reader:
        city = row[0]
        lat = row[1]
        long = row[2]
        location = geolocator.reverse(f"{lat}, {long}")
        print(f"{location.raw['address']['country']} hosts {city}")
