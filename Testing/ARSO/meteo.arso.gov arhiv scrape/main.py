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
            i+= 1
            while(json_string[i] != '"'):
                i += 1
        i += 1
    return json_string

def ugly_fix_time(time_string):
    time_number = int(time_string[1:])
    #2022-12-31 00:00 - 117285120
    known_time_coded = 117285120
    known_time_dt = datetime.datetime(2022, 12, 31, 0, 0, 0)
    time_difference = time_number - known_time_coded #minutes
    new_date = known_time_dt + datetime.timedelta(minutes=time_difference)
    #format date as yyyy-mm-dd-hh-mm
    return new_date.strftime("%Y-%m-%d-%H-%M")



def getLocations(starting_date, ending_date, type_of_request):
    # 122 dni je max (3 pozvedbe na leto)
    # 4 - Podatki samodejnih postaj
    # 3 - Dnevni podatki
    # 2 - Terminski prikaz vremena

    resulting_list_of_locations = []

    query_parameters = {'d1': starting_date,
                        'd2': ending_date, 'type': type_of_request, "lang": 'si'}

    location_request_url = "https://meteo.arso.gov.si/webmet/archive/locations.xml"
    locations_xml = requests.get(location_request_url, params=query_parameters)
    locations_xml.encoding = 'utf-8'

    locations_string = locations_xml.text

    index_start = locations_string.index('points')
    index_end = locations_string.index(']]')
    # this is ugly - also I could have very easily used ugly_fix_for_json that I implemented a bit later but it works
    locations_string = locations_string[index_start+8:index_end-4]
    locations_split = locations_string.split(',_')
    for location_string in locations_split:
        location_string = location_string.replace('name', '"name"')
        location_string = location_string.replace('lon', '"lon"')
        location_string = location_string.replace('lat', '"lat"')
        location_string = location_string.replace('alt', '"alt"')
        location_string = location_string.replace('type', '"type"')
        startingIndex = location_string.index('{')
        location_id = location_string[0:startingIndex-1]
        location_string = location_string[startingIndex:]
        location_value = json.loads(location_string)

        resulting_list_of_locations.append({location_id: location_value})

    return resulting_list_of_locations





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
            data_point_value = data_value['points']['_' + str(location_id)][data_point_key]['p0']
            all_data_points.append([data_point_key, data_point_value])
        except:
            all_data_points.append([data_point_key, 'null'])

    return all_data_points

#make main function
def main():
    # type_of_request = '4'
    # list_of_locations = getLocations(starting_date, ending_date, type_of_request)

    location_id = 1828
    variables = [12, 13, 14, 2, 15, 16, 17, 4, 18, 19, 20, 26, 21, 23, 24, 27, 28, 29]
    times = [
        ['2022-01-01', '2022-03-31'],
        ['2022-04-01', '2022-06-30'],
        ['2022-07-01', '2022-09-30'],
        ['2022-10-01', '2022-12-31']
    ]

    all_data = []
    all_times = []

    for variable_index in range(len(variables)):
        all_data.append([])
        for time in times:
            print("Doing " + str(variables[variable_index]) + " from " + time[0] + " to " + time[1] + "")
            starting_date = time[0]
            ending_date = time[1]
            data_points = getData(location_id, starting_date, ending_date, [variables[variable_index]])
            
            for data_point_time, data_point_value in data_points:
                if(variable_index == 0):
                    all_times.append(ugly_fix_time(data_point_time))
                all_data[variable_index].append(data_point_value)
        
    #dump data to csv
    with open('data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(all_times)
        for variable_index in range(len(variables)):
            writer.writerow(all_data[variable_index])
                    
    return

    #goto point



main()