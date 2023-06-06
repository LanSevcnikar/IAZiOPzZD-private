import os

root_dir = 'C:/Users/sevcn/Documents/programming/projects/IAZiOPzZD-private/GermanyPoC/sensor.community/'

with open(root_dir + 'final.csv', 'w', encoding='utf-8') as final_csv:
    final_csv.write('city,sensor_id,sensor_type,measurement_type,latitude,longitude,date,value\n')

    folders_in_temp = os.listdir(root_dir+'temp/')
    for city_folder in folders_in_temp:
        city = city_folder
        print('reading ' + city_folder)
        # open the city_2020.csv file
        with open(root_dir + 'temp/' + city_folder + '/' + city_folder + '_2020.csv', 'r', encoding='utf-8') as city_csv:
            # skip the first line
            city_csv.readline()
            # read the rest of the lines
            for line in city_csv.readlines():
                line = line.split(',')
                # round the last value to 4 decimal places
                line[-1] = str(round(float(line[-1]), 4))
                # write the line to the final csv

                final_csv.write(city + ',' + ','.join(line)+'\n')