# define a function that takes in city name, lat, lon, start date, end date, radious and will return some data that it will scrape from s.c
# import dependencies

import requests
import json
import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim
import os
from multiprocessing import Pool
from multiprocessing import freeze_support


# define a function that takes two pairs of lat and long and cals the distance in km


def distance(lat1, lon1, lat2, lon2):
    R = 6373.0
    lat1 = float(lat1)
    lon1 = float(lon1)
    lat2 = float(lat2)
    lon2 = float(lon2)

    lat1 = np.radians(lat1)
    lon1 = np.radians(lon1)
    lat2 = np.radians(lat2)
    lon2 = np.radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = np.sin(dlat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

    distance = R * c

    return distance


def does_sensor_have_datatype(sensor, datatype):
    for sensor_datatype in sensor["sensordatavalues"]:
        if(sensor_datatype["value_type"] == datatype):
            return True
    return False


def filter_sensors(all_sensors, lat, lon, rad, measurement_type):
    # geolocator = Nominatim(user_agent="my-app")
    # location = geolocator.reverse(f"{lat}, {lon}")
    # country_code = location.raw["address"]["country_code"].upper()
    # print(country_code)

    # remove all sensors that are not in the radius
    all_sensors = [sensor for sensor in all_sensors if
                   distance(
                       lat, lon,
                       float(sensor["location"]["latitude"]),
                       float(sensor["location"]["longitude"]))
                   <= rad
                   ]

    # remove all sensors that do not have the measurement type
    all_sensors = [sensor for sensor in all_sensors if
                   does_sensor_have_datatype(sensor, measurement_type)
                   ]

    # filter out all sensors that are indoors
    all_sensors = [sensor for sensor in all_sensors if
                   sensor["location"]["indoor"] == 0
                   ]

    # remove all sensors that are not in the country
    # all_sensors = [sensor for sensor in all_sensors if
    #                sensor["location"]["country"] == country_code
    #                ]

    return all_sensors


def process_sensor(data, measurement_type):
    # the data is in a CSV format
    # the first line is the header

    # split the data into lines
    lines = data.decode('utf-8').split('\n')
    # find the index of the measurement type
    measurement_type_index = lines[0].split(';').index(measurement_type)

    # find the average value of the measurement type

    sum = 0
    count = 0

    for line in lines[1:]:
        if(line == ''):
            continue
        sum += float(line.split(';')[measurement_type_index])
        count += 1

    average = sum / count
    return average


def process_date_helper(args):
    url, measurement_type,city_name,date = args
    try:
        request = requests.get(url, timeout=2)
        try:
            if 'Not Found' in request.content.decode('utf-8'):
                # throw exception to go to the except block
                return
        except:
            try:
                fileLocation = 'C:/Users/sevcn/Documents/programming/projects/IAZiOPzZD-private/GermanyPoC/sensor.community/temp/' + str(city_name) + '/' + str(date) + '/'
                fileName = url.replace('/', '_').replace(':', '_')

                with open(fileLocation + fileName, 'wb') as f:
                    f.write(request.content)
                    print('.',end='')

            except Exception as e:
                print(e)
                print('Could not download ' + url)
                return None
    except:
        pass

def generate_urls(sensors, date):
    while(len(sensors) > 250):
        # remover random sensors
        sensors.pop(np.random.randint(0, len(sensors)))

    base_url = 'https://archive.sensor.community/'
    year = date[:4]
    urls = []
    date_endings = ['-01', '-05', '-09', '-13', '-17', '-21', '-25']
    for date_ending in date_endings:
        whole_date = date + date_ending
        for sensor in sensors:
            sensor_name = str(sensor['sensor']['sensor_type']['name'])
            sensor_id = str(sensor['sensor']['id'])
            temp_url = base_url + '/' + year + '/' + whole_date + '/' + \
                whole_date + '_' + sensor_name + '_sensor_' + sensor_id + '.csv'
            temp_url = temp_url.lower()
            urls.append(temp_url)
            temp_url += '.gz'
            urls.append(temp_url)

    return urls


def process_date(city_name, sensors, measurement_type, date):
    print(len(sensors), measurement_type, date)
    
    urls = generate_urls(sensors, date)
    data = []
    # create a folder in temp called city name 
    try:
        os.mkdir('C:/Users/sevcn/Documents/programming/projects/IAZiOPzZD-private/GermanyPoC/sensor.community/temp/' + str(city_name))
    except:
        pass
    try:
        os.mkdir('C:/Users/sevcn/Documents/programming/projects/IAZiOPzZD-private/GermanyPoC/sensor.community/temp/' + str(city_name) + '/' + str(date))
    except:
        return 


    # Create a pool of worker processes
    pool = Pool()

    # Map the process_sensor_helper function to each URL in parallel

    tasks = [(url, measurement_type, city_name, date) for url in urls]
    pool.map(
        process_date_helper,
        tasks
    )

    # Close the pool and wait for the worker processes to finish
    pool.close()
    pool.join()
    print('')

    # Filter out the None values and return the average of the remaining data
    # data = [d for d in data if d is not None]
    # data.sort()
    # print(data)
    # if(len(data) < 5):
    #     return -1
    # data = data[int(len(data) / 3):int(len(data) * 2 / 3)]
    # return sum(data) / len(data)


def get_data_from_sc(city_name, lat, lon, start_date, end_date, radius, measurement_type):
    if(measurement_type == "PM10"):
        measurement_type = "P1"
    if(measurement_type == "PM2.5"):
        measurement_type = "P2"

    # load all sensors from local json file
    with open('C:/Users/sevcn/Documents/programming/projects/IAZiOPzZD-private/GermanyPoC/sensor.community/all_sensors.json', 'r') as f:
        all_sensors = json.load(f)
    all_sensors = filter_sensors(
        all_sensors, lat, lon, radius, measurement_type)

    # create a list of dates between the start and end date
    dates = pd.date_range(start_date, end_date,
                          freq='MS').strftime("%Y-%m").tolist()

    print(city_name, len(all_sensors))
    # you got rid of for dates
    for date in dates:
        process_date(city_name, all_sensors, measurement_type, date)
    return


if __name__ == '__main__':
    # # freeze_support()

    cities_input = 'C:/Users/sevcn/Documents/programming/projects/IAZiOPzZD-private/GermanyPoC/FinalValues/Cities.csv'
    # get all cities from the csv file
    cities = pd.read_csv(cities_input, sep=',', encoding='utf-8')
    # make an array of triples (city_name, lat, lon)
    cities = cities[['City', 'Latitude', 'Longitude']].values.tolist()

    for city in cities:
        city_name, lat, lon = city
        print(city_name, lat, lon)
        sc_data = get_data_from_sc(
            city_name,
            lat,
            lon,
            '2020-01',
            '2020-12',
            20,
            "PM10"
        )



    # if __name__ == "__main__":
    #     # get the data
    #     sc_data = get_data_from_sc(
    #         'Ljubljana',
    #         46.056946,
    #         14.505751,
    #         '2021-01',
    #         '2021-12',
    #         20,
    #         "PM10"
    #     )

    #     # dump data to json
    #     with open('sensors.json', 'w') as f:
    #         json.dump(sc_data, f)
