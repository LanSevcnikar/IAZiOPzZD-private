# define a function that takes in city name, lat, lon, start date, end date, radious and will return some data that it will scrape from s.c
# import dependencies

import requests
import json
import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim
import os
from multiprocessing import Pool

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
    url, measurement_type = args
    try:
        request = requests.get(url)
        # check if the content contains the words Not Found
        if 'Not Found' in request.content.decode('utf-8'):
            # print('Could not download ' + url)
            return None

        return process_sensor(request.content, measurement_type)

    except:
        # print('Could not download ' + url)
        return None


def process_date(sensors, measurement_type, date):
    base_url = 'https://archive.sensor.community/'
    year = date[:4]
    whole_date = date + '-01'

    data = []
    urls = []
    for sensor in sensors:
        sensor_name = str(sensor['sensor']['sensor_type']['name'])
        sensor_id = str(sensor['sensor']['id'])
        url = base_url + '/' + year + '/' + whole_date + '/' + \
            whole_date + '_' + sensor_name + '_sensor_' + sensor_id + '.csv'
        url = url.lower()
        urls.append(url)

    # Create a pool of worker processes
    pool = Pool()

    # Map the process_sensor_helper function to each URL in parallel
    data = pool.map(
        process_date_helper,
        [(url, measurement_type) for url in urls]
    )

    # Close the pool and wait for the worker processes to finish
    pool.close()
    pool.join()

    # Filter out the None values and return the average of the remaining data
    data = [d for d in data if d is not None]
    data.sort()
    data = data[int(len(data) / 3):int(len(data) * 2 / 3)]
    return sum(data) / len(data)


def get_data_from_sc(city_name, lat, lon, start_date, end_date, radius, measurement_type):
    if(measurement_type == "PM10"):
        measurement_type = "P1"
    if(measurement_type == "PM2.5"):
        measurement_type = "P2"

    # the dates are formatted as YYYY-MM and I want to get all the dates between the two
    # all_sensors_json = requests.get(
    #     "https://maps.sensor.community/data/v1/data.json")
    # all_sensors = all_sensors_json.json()
    # load all sensors from local json file
    with open('./SC/all_sensors.json', 'r') as f:
        all_sensors = json.load(f)
    all_sensors = filter_sensors(
        all_sensors, lat, lon, radius, measurement_type)

    # create a list of dates between the start and end date
    dates = pd.date_range(start_date, end_date,
                          freq='MS').strftime("%Y-%m").tolist()

    return_value = []

    # process each date
    for date in dates:
        date_result = process_date(all_sensors, measurement_type, date)
        print(date_result)
        return_value.append((date, date_result))

    return return_value


if __name__ == "__main__":
    # get the data
    sc_data = get_data_from_sc(
        'Ljubljana',
        46.056946,
        14.505751,
        '2021-01',
        '2021-12',
        20,
        "PM10"
    )

    # dump data to json
    with open('sensors.json', 'w') as f:
        json.dump(sc_data, f)
