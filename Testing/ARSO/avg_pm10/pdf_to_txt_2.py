import os
from pdfminer.high_level import extract_text

years = [
    '2013', 
    '2014',
    '2015',
    '2016',
    '2017',
    '2018',
    '2019',
    '2020',
    '2021',
    '2022'
]

if not os.path.exists('./data_txt'):
    os.makedirs('./data_txt')

for year in years:
    # if the folder data_txt/{year} does not exist, create it
    if not os.path.exists(f"./data_txt/{year}"):
        os.makedirs(f"./data_txt/{year}")
        
    #delete all files in folder data_txt/{year}
    for filename in os.listdir(f'./data_txt/{year}'):
        os.remove(f"./data_txt/{year}/{filename}")


    text = extract_text(f'data_raw/PM10_D_dec{year[2:]}_slo.pdf')
    file = open(f"./data_txt/{year}.txt","a", encoding='utf-8')
    file.writelines(text)