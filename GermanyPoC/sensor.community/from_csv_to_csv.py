import os

root_location = 'C:/Users/sevcn/Documents/programming/projects/IAZiOPzZD-private/GermanyPoC/sensor.community/temp/'

# find all folders in temp
folders_in_temp = os.listdir(root_location)
for city_folder in folders_in_temp:
    if(city_folder != 'Bremen'):
        continue
    # create a new cvs folder called city_year.csv and open it using pandas
    csv_file = open(root_location + city_folder + '/' +
                    city_folder + '_2020.csv', 'w')
    csv_file.write(
        'sensor_id,sensor_type,measurement_type,latitude,longitude,date,value\n')

    # find all folders in city folder
    folders_in_city = os.listdir(root_location + city_folder)
    for date_folder in folders_in_city:
        # find all files in date folder
        print('reading ' + date_folder + ' in ' + city_folder)
        
        # check that this is in fact a folder of the format yyyy-mm
        if len(date_folder) != 7:
            continue
        files_in_date = ""
        try:
            files_in_date = os.listdir(
                root_location + city_folder + '/' + date_folder + '/csvs')
        except Exception as e:
            print(e)
            continue

        for file in files_in_date:
            # skip the folders
            if file == 'csvs' or file == 'zips':
                continue
            # skip the file if it does not end in .gz
            if file[-3:] != 'csv':
                continue

            # open the file and read the first line
            input_file = root_location + city_folder + '/' + date_folder + '/csvs/' + file
            # print('reading ' + input_file)

            with open(input_file, 'r') as csv:
                sensor_id_index = -1
                sensor_type_index = -1
                lat_index = -1
                lon_index = -1
                timestamp_index = -1
                P1_index = -1
                P2_index = -1

                # read the first line
                first_line = csv.readline()
                # find the indexes of the columns we need
                first_line = first_line.split(';')
                for i in range(len(first_line)):
                    if(first_line[i] == 'sensor_id'):
                        sensor_id_index = i
                    elif(first_line[i] == 'sensor_type'):
                        sensor_type_index = i
                    elif(first_line[i] == 'lat'):
                        lat_index = i
                    elif(first_line[i] == 'lon'):
                        lon_index = i
                    elif(first_line[i] == 'timestamp'):
                        timestamp_index = i
                    elif(first_line[i] == 'P1'):
                        P1_index = i
                    elif(first_line[i] == 'P2'):
                        P2_index = i
                # if we did not find all the indexes, skip the file
                if sensor_id_index == -1 or sensor_type_index == -1 or lat_index == -1 or lon_index == -1 or timestamp_index == -1 or P1_index == -1 or P2_index == -1:
                    continue

                sensor_id = first_line[sensor_id_index]
                sensor_type = first_line[sensor_type_index]
                lat = first_line[lat_index]
                lon = first_line[lon_index]
                p1 = first_line[P1_index]
                p2 = first_line[P2_index]                    

                P1_sum = 0
                P2_sum = 0
                P1_count = 0
                P2_count = 0

                # read the rest of the file
                date = ""

                for _line in csv:
                    line = _line.split(';')
                    if date == "":
                        date = line[timestamp_index].split('T')[0]
                        
                    P1 = line[P1_index]
                    P2 = line[P2_index]
                    if P1 != 'nan':
                        try:
                            P1_sum += float(P1)
                            P1_count += 1
                        except:
                            continue
                    if P2 != 'nan': 
                        try:
                            P2_sum += float(P2)
                            P2_count += 1
                        except:
                            continue
                
                if P1_count == 0:
                    P1_avg = 'nan'
                else:
                    P1_avg = P1_sum / P1_count

                if P2_count == 0:
                    P2_avg = 'nan'
                else:
                    P2_avg = P2_sum / P2_count

                # write the line to the new csv file
                csv_file.write(line[sensor_id_index] + ',' + line[sensor_type_index] + ',P1,' + line[lat_index] + ',' + line[lon_index] + ',' + date + ',' + str(P1_avg) + '\n')
                csv_file.write(line[sensor_id_index] + ',' + line[sensor_type_index] + ',P2,' + line[lat_index] + ',' + line[lon_index] + ',' + date + ',' + str(P2_avg) + '\n')


    csv_file.close()
