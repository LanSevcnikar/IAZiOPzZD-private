import json
import math

# funcction to calculate the distance betweent wo lat and long points in km
def distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295
    a = 0.5 - math.cos((lat2 - lat1) * p)/2 + math.cos(lat1 * p) * math.cos(lat2 * p) * (1 - math.cos((lon2 - lon1) * p)) / 2
    return 12742 * math.asin(math.sqrt(a))

sensors = []

with open('./sensor_community/data.json') as f:
    data = json.load(f)
    for location in data:
        id = location['id']
        location_id = location['location']['id']
        try:
            location_latitude = float(location['location']['latitude'])
        except:
            location_latitude = 0
        try:
            location_longitude = float(location['location']['longitude'])
        except:
            location_longitude = 0
        try:
            location_altitude = float(location['location']['altitude'])
        except:
            location_altitude = 0
        location_country = location['location']['country']
        location_indoor = location['location']['indoor']
        sensor_id = location['sensor']['id']
        sensor_pin = location['sensor']['pin']
        sensor_sensor_type_id = location['sensor']['sensor_type']['id']
        sensor_sensor_type_name = location['sensor']['sensor_type']['name']

        # distance between the sensor and Ljubljana
        dist = distance(location_latitude, location_longitude, 46.056946, 14.505751)

        sensors.append({
            'id': id,
            'location_id': location_id,
            'location_latitude': location_latitude,
            'location_longitude': location_longitude,
            'location_altitude': location_altitude,
            'location_country': location_country,
            'location_indoor': location_indoor,
            'sensor_id': sensor_id,
            'sensor_pin': sensor_pin,
            'sensor_sensor_type_id': sensor_sensor_type_id,
            'sensor_sensor_type_name': sensor_sensor_type_name,
            'distance': dist
        })
        
# sort the sensors by distance
sensors.sort(key=lambda x: x['distance'])

# remove all sensors with a distance greater than 250km
sensors = [x for x in sensors if x['distance'] < 250]

# print the number of sensors
print(len(sensors))

# dump all the sensors into a json file
with open('sensors.json', 'w') as f:
    json.dump(sensors, f, indent=4)