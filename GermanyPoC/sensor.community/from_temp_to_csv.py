import os

# find all folders in temp
folders_in_temp = os.listdir('C:/Users/sevcn/Documents/programming/projects/IAZiOPzZD-private/GermanyPoC/sensor.community/temp/')

# loop through all folders in folders in temp
for city_folder in folders_in_temp:
    folders_in_city = os.listdir('C:/Users/sevcn/Documents/programming/projects/IAZiOPzZD-private/GermanyPoC/sensor.community/temp/' + city_folder)
    for date_folder in folders_in_city:
        print('unzipping ' + date_folder + ' in ' + city_folder)
        # loop through all files in date folder
        files_in_date = os.listdir('C:/Users/sevcn/Documents/programming/projects/IAZiOPzZD-private/GermanyPoC/sensor.community/temp/' + city_folder + '/' + date_folder)
        for file in files_in_date:
            #skip the folders
            if file == 'csvs' or file == 'zips':
                continue
            # unizip the file
            print('unzipping ' + file)
            unzip_command = 'tar -xf ' + 'C:/Users/sevcn/Documents/programming/projects/IAZiOPzZD-private/GermanyPoC/sensor.community/temp/' + city_folder + '/' + date_folder + '/' + file + ' -C ' + 'C:/Users/sevcn/Documents/programming/projects/IAZiOPzZD-private/GermanyPoC/sensor.community/temp/' + city_folder + '/' + date_folder
            print(unzip_command)
            os.system(unzip_command)
            # move the zip file into a new folder called zips
            try:
                os.mkdir('C:/Users/sevcn/Documents/programming/projects/IAZiOPzZD-private/GermanyPoC/sensor.community/temp/' + city_folder + '/' + date_folder + '/zips')
            except:
                pass
            os.system('move ' + 'C:/Users/sevcn/Documents/programming/projects/IAZiOPzZD-private/GermanyPoC/sensor.community/temp/' + city_folder + '/' + date_folder + '/' + file + ' ' + 'C:/Users/sevcn/Documents/programming/projects/IAZiOPzZD-private/GermanyPoC/sensor.community/temp/' + city_folder + '/' + date_folder + '/zips')
            # move the csv file into a new folder called csvs
            try:
                os.mkdir('C:/Users/sevcn/Documents/programming/projects/IAZiOPzZD-private/GermanyPoC/sensor.community/temp/' + city_folder + '/' + date_folder + '/csvs')
            except:
                pass
            os.system('move ' + 'C:/Users/sevcn/Documents/programming/projects/IAZiOPzZD-private/GermanyPoC/sensor.community/temp/' + city_folder + '/' + date_folder + '/' + file[:-3] + ' ' + 'C:/Users/sevcn/Documents/programming/projects/IAZiOPzZD-private/GermanyPoC/sensor.community/temp/' + city_folder + '/' + date_folder + '/csvs')
            
            quit()