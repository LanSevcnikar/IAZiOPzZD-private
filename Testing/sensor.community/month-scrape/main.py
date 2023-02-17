# Types of sensors

# bme280  - Digital humidity, pressure and temperature sensor
# bmp180  - Digital pressure and temperature sensor
# bmp280  - Digital, barometric pressure sensor
# dht22   - Temperature and Humidity Sensor
# ds18b20 - Digital Thermometer
# hpm     - Particulate Matter Sensor (PM)
# htu21d  - relative humidity and temperature sensors
# laerm   - No idea, should not exist
# nextpm  - Particulate Matter Sensor
# pms1003 - Air Quality Sensor (AQ)
# pms3003 - Air Quality Sensor
# pms5003 - Air Quality Sensor
# pms6003 - Air Quality Sensor
# pms7003 - Air Quality Sensor
# ppd42ns - Air Quality Sensor
# radiation
# scd30   - CO2, Humidity, Temperature
# sds011  - Air Quality Sensor
# sht11   - Digital humidity and temperature sensor
# sht15   - Digital humidity and temperature sensor
# sht30   - Digital humidity and temperature sensor
# sht31   - Digital humidity and temperature sensor
# sht35   - Digital humidity and temperature sensor
# sht85   - Digital humidity and temperature sensor
# sps30   - PM and Air Quality Sensor
# ppd42ns - Dust Sensor (PM)

import os
from bs4 import BeautifulSoup
import requests

air_quality_sensors = ['pms1003', 'pms3003', 'pms5003',
                       'pms6003', 'pms7003', 'ppd42ns', 'sps30']
#I skipped sds011 because it is much too large (3.9 GB)

url = "https://archive.sensor.community/csv_per_month/"
months = ['2022-12']

#create a sensor class with an array of all meassurments, long, lat, sensor type, sensor id
class Sensor:
    def __init__(self, sensor_id, sensor_type, lat, long):
        print("Created sensor", sensor_id, sensor_type, lat, long)
        self.sensor_id = sensor_id
        self.sensor_type = sensor_type
        self.lat = float(lat)
        self.long = float(long)
        self.measurements = []

    def add_measurement(self, measurement):
        self.measurements.append(measurement)


def download_links(month):
    # get me all the links on this website
    links_request = requests.get(url+month)
    soup = BeautifulSoup(links_request.text, 'html.parser')
    links = soup.find_all('a')
    # print all the links
    for link in links:
        # check if the link contains the sensor type
        is_AQ_sensor = False
        for sensor in air_quality_sensors:
            if sensor in link['href']:
                is_AQ_sensor = True
                break
        if is_AQ_sensor:
            #check if folder called month exists, if not create it 
            if not os.path.exists(month):
                os.makedirs(month)
            #download the file into a folder called month
            print("Downloaded", link['href'])
            r = requests.get(url+month+'/'+link['href'])
            with open(month+'/'+link['href'], 'wb') as f:
                f.write(r.content)

def unzip_files(month):
    # unzip all the files in the folder
    for file in os.listdir(month):
        if file.endswith('.zip'):
            print("Unzipped",file)
            #unzip the file and delete it with a windows command
            os.system('powershell.exe -Command "Expand-Archive -Path '+month+'/'+file+' -DestinationPath '+month+'"')
            os.system('powershell.exe -Command "Remove-Item -Path '+month+'/'+file+'"')

def find_all_sensors(month):
    #loop through all files in the month folder and find all sensors
    sensors = []
    for file in os.listdir(month):
        #read the csv file and find all unique sensors
        if file.endswith('.csv'):
            print("Reading",file)
            with open(month+'/'+file, 'r') as f:
                is_first_line = True
                for line in f:
                    #skip the first line
                    if is_first_line:
                        is_first_line = False
                        continue
                    #split the line into an array
                    line = line.split(';')
                    #check if the sensor is already in the array
                    sensor_exists = False
                    for sensor in sensors:
                        if sensor.sensor_id == line[0]:
                            sensor_exists = True
                            break
                    #if not add it to the array
                    if not sensor_exists:
                        sensors.append(Sensor(line[0], line[1], line[3], line[4]))
    return sensors

def get_month(month, lat, long):
    # download_links(month)
    # unzip_files(month)
    sensors = find_all_sensors(month)
    #sort the sensors by how close they are to the lat and long
    sensors.sort(key=lambda x: (x.lat-lat)**2+(x.long-long)**2)
    #dump all sensors into a sensors.txt file with their id, type, lat, long
    with open('sensors.txt', 'w') as f:
        for sensor in sensors:
            f.write(sensor.sensor_id+';'+sensor.sensor_type+';'+str(sensor.lat)+';'+str(sensor.long)+'\n')
    sensors = sensors[:5]
    for sensor in sensors:
        print(sensor.sensor_id, sensor.sensor_type, sensor.lat, sensor.long)

month = months[0]
lat = 46.056946
long = 14.505751

get_month(month, lat, long)