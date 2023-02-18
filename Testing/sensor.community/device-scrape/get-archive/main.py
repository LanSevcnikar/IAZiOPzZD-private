import os
import pandas as pd
import requests


number_of_sensors = 1
starting_date = '2022-12-18'
ending_date = '2022-12-19'

sensors = []

# read the first 5 lines from ../get-sensors/sensors.txt
with open('../get-sensors/sensors.txt', 'r') as f:
    sensors_temp = f.readlines()[:number_of_sensors]
    for sensor in sensors_temp:
        sensors.append(sensor.strip().split(';'))

print(sensors)

# create folders for each of the sensors
for sensor in sensors:
    if not os.path.exists("data/" + sensor[1] + '-' + sensor[0]):
        os.makedirs("data/" + sensor[1] + '-' + sensor[0])

#loop through all the dates between starting_date and ending_date
#and download the data for each sensor
for date_full in pd.date_range(starting_date, ending_date):
    date_short = date_full.strftime('%Y-%m-%d')
    base_url = 'https://archive.sensor.community/'
    for sensor in sensors:
        url = base_url + date_short + '/' + date_short + '_' + sensor[1] + '_sensor_' + sensor[0] + '.csv'
        url = url.lower()
        #try downaloding the cvs file from the url, if it does not work, continue
        #then save it to the folder of the sensor
        print(url)
        try:
            request = requests.get(url)
            with open("data/" + sensor[1] + '-' + sensor[0] + '/' + date_short + '_' + sensor[1] + '_sensor_' + sensor[0] + '.csv', 'wb') as f:
                f.write(request.content)
        except:
            print('Could not download ' + url)
            continue
            


# https://archive.sensor.community/2022-12-18/2022-12-18_DHT22_sensor_64689.csv
# https://archive.sensor.community/2022-12-18/2022-12-18_dht22_sensor_64689.csv