import csv
import json
import datetime
import requests

STARTING_DATE_PLACEHOLDER = '2022-01-01'
ENDING_DATE_PLACEHOLDER = '2022-12-31'

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
def download_data(location_id, times, variables):
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
    with open(f'data-{location_id}-.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(all_times)
        for variable_index in range(len(variables)):
            writer.writerow(all_data[variable_index])
                    
    return

    #goto point



import tkinter as tk

class DownloadGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Download Data")

        # Starting date label and entry
        tk.Label(master, text="Starting Date (yyyy-mm-dd)").grid(row=0, column=0)
        self.start_date_entry = tk.Entry(master)
        self.start_date_entry.grid(row=0, column=1)
        # Create a placeholder value
        self.start_date_entry.insert(0, STARTING_DATE_PLACEHOLDER)
        


        # Ending date label and entry
        tk.Label(master, text="Ending Date (yyyy-mm-dd)").grid(row=1, column=0)
        self.end_date_entry = tk.Entry(master)
        self.end_date_entry.grid(row=1, column=1)
        # Create a placeholder value
        self.end_date_entry.insert(0, ENDING_DATE_PLACEHOLDER)

        # Checkbox options
        tk.Label(master, text="Options").grid(row=2, column=0)
        self.checkbox_vars = []
        self.all_options = [
            "12 povprečen zračni tlak (hPa)", 
            "13 minimalen zračni tlak (hPa)",
            "14 maksimalen zračni tlak (hPa)",
            "2 terminska temperatura zraka na 2m (°C)",
            "15 povprečna temperatura zraka na 2m (°C)",
            "16 minimalna temperatura zraka na 2m (°C)",
            "17 maksimalna temperatura zraka na 2m (°C)",
            "4 terminska relativna vlaga (%)",
            "18 povprečna relativna vlaga (%)",
            "19 minimalna relativna vlaga (%)",
            "20 maksimalna relativna vlaga (%)",
            "26 količina padavin (mm)",
            "21 povprečna hitrost vetra (m/s)",
            "23 povprečna smer vetra (°)",
            "24 maksimalna hitrost vetra (m/s)",
            "27 povprečen energijski tok globalnega sevanja (W/m2)",
            "28 povprečen energijski tok difuznega sevanja (W/m2)",
            "29 UVB (mW/m2)"
            ]
        for i, option in enumerate(self.all_options):
            var = tk.IntVar(value=0)
            tk.Checkbutton(master, text=option, variable=var).grid(row=i+3, column=0, sticky="w")
            self.checkbox_vars.append(var)

        # Checkbox locations
        tk.Label(master, text="Locations").grid(row=len(self.all_options)+3, column=0)
        self.location_vars = []
        self.all_locations = [
            "1828 LJUBLJANA BEŽIGRAD", 
            "1872 LJUBLJANA KLEČE", 
            "2842 TOPOL"
        ]
        for i, location in enumerate(self.all_locations):
            var = tk.IntVar(value=0)
            tk.Checkbutton(master, text=location, variable=var).grid(row=i+len(self.all_options)+4, column=0, sticky="w")
            self.location_vars.append(var)

        # Download button
        tk.Button(master, text="Download", command=self.download).grid(row=len(self.all_options)+len(self.all_locations)+5, column=0, columnspan=2)

    def get_times(self, starting_date, ending_date):
        #This function should return a list of starting and ending dates that all together cover this time but also do not overlap and are not longer than 100 days
        #For example, if you want to download data from 2020-01-01 to 2020-03-31, this function should return:
        #[
        #   ['2020-01-01', '2020-03-31']
        #]
        #But if you want to download data from 2020-01-01 to 2020-04-01, this function should return:
        #[
        #   ['2020-01-01', '2020-03-31'],
        #   ['2020-04-01', '2020-04-01']
        #]

        result_array = []
        
        starting_date_obj = datetime.datetime(int(starting_date.split('-')[0]), int(starting_date.split('-')[1]), int(starting_date.split('-')[2]), 0, 0, 0)
        ending_date_obj = datetime.datetime(int(ending_date.split('-')[0]), int(ending_date.split('-')[1]), int(ending_date.split('-')[2]), 0, 0, 0)
        
        while(starting_date_obj + datetime.timedelta(days=100) < ending_date_obj):
            result_array.append([starting_date_obj.strftime('%Y-%m-%d'), (starting_date_obj + datetime.timedelta(days=100)).strftime('%Y-%m-%d')])
            starting_date_obj = starting_date_obj + datetime.timedelta(days=100)
        result_array.append([starting_date_obj.strftime('%Y-%m-%d'), ending_date_obj.strftime('%Y-%m-%d')])
        return result_array

    def download(self):
        # Retrieve input values
        start_date = self.start_date_entry.get()
        end_date = self.end_date_entry.get()
        options = [i.get() for i in self.checkbox_vars]
        locations_temp = [i.get() for i in self.location_vars]
        
        times = self.get_times(start_date, end_date)
        variables = []
        for i, option in enumerate(options):
            if option == 1:
                variables.append(int(self.all_options[i].split(' ')[0]))
        
        locations = []
        for i, location in enumerate(locations_temp):
            if location == 1:
                locations.append(int(self.all_locations[i].split(' ')[0]))

        for location in locations:
            download_data(location, times, variables)

if __name__ == "__main__":
    root = tk.Tk()
    app = DownloadGUI(root)
    root.mainloop()