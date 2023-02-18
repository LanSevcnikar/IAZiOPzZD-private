import requests
import json
# Ljubljana
lat = 46.056946
lon = 14.505751

# all sensors
all_sensors_json = requests.get(
    "https://maps.sensor.community/data/v1/data.json")
all_sensors = all_sensors_json.json()

# sort the sensors by how close they are to the lat and long
all_sensors.sort(key=lambda x: (float(
    x["location"]["latitude"])-lat)**2+(float(x["location"]["longitude"])-lon)**2)
# dump all sensors into a file
with open('sensors.txt', 'w') as f:
    for sensor in all_sensors:
        f.write(str(sensor["sensor"]["id"])+';'+str(sensor["sensor"]["sensor_type"]["name"])+';' +
                str(sensor["location"]["latitude"])+';'+str(sensor["location"]["longitude"])+'\n')
