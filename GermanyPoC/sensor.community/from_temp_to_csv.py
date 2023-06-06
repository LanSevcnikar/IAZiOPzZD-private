import os
import gzip
import shutil

file_prefix = 'C:/Users/sevcn/Documents/programming/projects/IAZiOPzZD-private/GermanyPoC/sensor.community/temp/'

# find all folders in temp
folders_in_temp = os.listdir(file_prefix)

# loop through all folders in folders in temp
for city_folder in folders_in_temp:
    folders_in_city = os.listdir(file_prefix + city_folder)
    for date_folder in folders_in_city:
        print('unzipping ' + date_folder + ' in ' + city_folder)
        # loop through all files in date folder
        try:
            files_in_date = os.listdir(file_prefix + city_folder + '/' + date_folder)
        except:
            continue
        for file in files_in_date:
            #skip the folders
            if file == 'csvs' or file == 'zips':
                continue
            #skip the file if it does not end in .gz
            if file[-3:] != '.gz':
                continue
            # unizip the file
            input_file = file_prefix + city_folder + '/' + date_folder + '/' + file
            output_file = file_prefix + city_folder + '/' + date_folder + '/' + 'csvs/' + file[:-3]
            print('unzipping ' + file)

            # move the zip file into a new folder called zips
            try:
                os.mkdir(file_prefix + city_folder + '/' + date_folder + '/zips')
            except:
                pass
            try:
                os.mkdir(file_prefix + city_folder + '/' + date_folder + '/csvs')
            except:
                pass
            try:
                with gzip.open(input_file, 'rb') as gz_file:
                # Open the output file in binary mode
                    with open(output_file, 'wb') as out_file:
                        # Copy the contents from the .gz file to the output file
                        shutil.copyfileobj(gz_file, out_file)
            except:
                pass
            
        #     try:
        #         move_command = 'move "' + input_file + '" "' + file_prefix + city_folder + '/' + date_folder + '/zips/"'
        #         print(move_command)
        #         os.system(move_command)
        #     except:
        #         pass
        # quit()