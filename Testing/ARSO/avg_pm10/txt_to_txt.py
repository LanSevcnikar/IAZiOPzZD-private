import os
import time

years = [
    2013,
    2014,
    2015,
    2016,
    2017,
    2018,
    2019,
    2020,
    2021,
    2022
]

# delete all files in data_txt but leave the folders alone
for filename in os.listdir('./data_txt'):
    try:
        os.remove(f"./data_txt/{filename}")
    except:
        pass

# join all txt files in data_txt/{year} into one file called data_txt/{year}.txt
for year in years:
    path = os.path.join('data_txt', str(year))
    files = os.listdir(path)
    with open(os.path.join('data_txt', str(year) + '.txt'), 'w', encoding='utf-8') as f:
        for file in files:
            with open(os.path.join(path, file), 'r', encoding='utf-8') as f2:
                f.write(f2.read())
                f.write('\n')
