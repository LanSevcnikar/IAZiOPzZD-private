from http.server import BaseHTTPRequestHandler, HTTPServer
import json


import csv
import json
import datetime
import requests


def ugly_fix_for_json(json_string):
    characters_to_skip = ['{', '}', ',', ':', '"', ' ', '\\', "'", '[', ']']
    i = 0
    while i < len(json_string):
        if(json_string[i] not in characters_to_skip):
            json_string = json_string[0:i] + '"' + json_string[i:]
            i += 1
            while(json_string[i] not in characters_to_skip):
                i += 1
            json_string = json_string[0:i] + '"' + json_string[i:]
        elif(json_string[i] == '"'):
            i += 1
            while(json_string[i] != '"'):
                i += 1
        i += 1
    return json_string


def ugly_fix_time(time_string):
    time_number = int(time_string[1:])
    # 2022-12-31 00:00 - 117285120
    known_time_coded = 117285120
    known_time_dt = datetime.datetime(2022, 12, 31, 0, 0, 0)
    time_difference = time_number - known_time_coded  # minutes
    new_date = known_time_dt + datetime.timedelta(minutes=time_difference)
    # format date as yyyy-mm-dd-hh-mm
    return new_date.strftime("%Y-%m-%d-%H-%M")


def getData(location_id, starting_date, ending_date, variables):
    # 12 - povprečen zračni tlak (hPa)
    # 13 - minimalen zračni tlak (hPa)
    # 14 - maksimalen zračni tlak (hPa)
    # 2  - terminska temperatura zraka na 2m (°C)
    # 15 - povprečna temperatura zraka na 2m (°C)
    # 16 - minimalna temperatura zraka na 2m (°C)
    # 17 - maksimalna temperatura zraka na 2m (°C)
    # 4  - terminska relativna vlaga (%)
    # 18 - povprečna relativna vlaga (%)
    # 19 - minimalna relativna vlaga (%)
    # 20 - maksimalna relativna vlaga (%)
    # 26 - količina padavin (mm)
    # 21 - povprečna hitrost vetra (m/s)
    # 23 - povprečna smer vetra (°)
    # 24 - maksimalna hitrost vetra (m/s)
    # 27 - povprečen energijski tok globalnega sevanja (W/m2)
    # 28 - povprečen energijski tok difuznega sevanja (W/m2)
    # 29 - UVB (mW/m2)
    all_data_points = []

    variables_string = ','.join(str(variable) for variable in variables)

    query_parameters = {'d1': starting_date, 'd2': ending_date, "lang": 'si',
                        'vars': variables_string, 'group': 'halfhourlyData0', 'type': 'halfhourly', 'id': location_id}

    data_request_url = "https://meteo.arso.gov.si/webmet/archive/data.xml"
    data_xml = requests.get(data_request_url, params=query_parameters)
    data_xml.encoding = 'utf-8'

    data_string = data_xml.text

    index_start = data_string.index('CDATA[AcademaPUJS.set(')
    index_end = data_string.index(')]]></pujs>')
    # this is ugly
    data_string = data_string[index_start+22:index_end]
    data_string = ugly_fix_for_json(data_string)
    data_string = data_string.replace("\"'\"", "'")

    data_value = json.loads(data_string)
    for data_point_key in data_value['points']['_' + str(location_id)]:
        if(ugly_fix_time(data_point_key)[-2:] != "00"):
            continue
        try:
            data_point_value = data_value['points']['_' +
                                                    str(location_id)][data_point_key]['p0']
            all_data_points.append([data_point_key, data_point_value])
        except:
            all_data_points.append([data_point_key, 'null'])

    return all_data_points


def get_times(starting_date, ending_date):
    # This function should return a list of starting and ending dates that all together cover this time but also do not overlap and are not longer than 100 days
    # For example, if you want to download data from 2020-01-01 to 2020-03-31, this function should return:
    # [
    #   ['2020-01-01', '2020-03-31']
    # ]
    # But if you want to download data from 2020-01-01 to 2020-04-01, this function should return:
    # [
    #   ['2020-01-01', '2020-03-31'],
    #   ['2020-04-01', '2020-04-01']
    # ]

    result_array = []

    starting_date_obj = datetime.datetime(int(starting_date.split(
        '-')[0]), int(starting_date.split('-')[1]), int(starting_date.split('-')[2]), 0, 0, 0)
    ending_date_obj = datetime.datetime(int(ending_date.split(
        '-')[0]), int(ending_date.split('-')[1]), int(ending_date.split('-')[2]), 0, 0, 0)

    while(starting_date_obj + datetime.timedelta(days=100) < ending_date_obj):
        result_array.append([starting_date_obj.strftime(
            '%Y-%m-%d'), (starting_date_obj + datetime.timedelta(days=100)).strftime('%Y-%m-%d')])
        starting_date_obj = starting_date_obj + datetime.timedelta(days=100)
    result_array.append([starting_date_obj.strftime(
        '%Y-%m-%d'), ending_date_obj.strftime('%Y-%m-%d')])
    return result_array

# make main function


def download_data_temp(location_id, starting_date, ending_date, variables):
    all_data = []
    all_times = []
    times = get_times(starting_date, ending_date)

    for variable_index in range(len(variables)):
        all_data.append([])
        for time in times:
            print("Doing " + str(variables[variable_index]) +
                  " from " + time[0] + " to " + time[1] + "")
            starting_date = time[0]
            ending_date = time[1]
            data_points = getData(location_id, starting_date, ending_date, [
                                  variables[variable_index]])

            for data_point_time, data_point_value in data_points:
                if(variable_index == 0):
                    all_times.append(ugly_fix_time(data_point_time))
                all_data[variable_index].append(data_point_value)

    return {
        "times": all_times,
        "data": all_data

    }



class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        # Get the length of the incoming request data
        content_length = int(self.headers['Content-Length'])

        # Read the incoming request data
        request_data = self.rfile.read(content_length)

        # Parse the JSON data
        data = json.loads(request_data)

        location_id = data['ARSO_id']
        starting_date = data['startingDate']
        ending_date = data['endingDate']
        variables = [data['ARSO_type_id']]

        

        print(data, "HELLOWORLD")
        print(location_id, starting_date, ending_date, variables)

        scrapedData = download_data_temp(location_id, starting_date, ending_date, variables)

        print(scrapedData)
        # Send a 200 OK response with the same JSON data
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        # send scrapted data back
        self.end_headers()
        self.wfile.write(json.dumps(scrapedData).encode())


if __name__ == '__main__':
    # Set the host and port to listen on
    host = ''
    port = 3001

    # Start the server
    httpd = HTTPServer((host, port), SimpleHTTPRequestHandler)
    print(f'Starting server on {host}:{port}')
    httpd.serve_forever()
