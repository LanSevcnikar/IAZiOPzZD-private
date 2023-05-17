import pandas as pd


input_file = 'C:/Users/sevcn/Documents/programming/projects/IAZiOPzZD-private/GermanyPoC/EuroStat/data.csv'
output_file = 'C:/Users/sevcn/Documents/programming/projects/IAZiOPzZD-private/GermanyPoC/EuropeAirPortal/cities.csv'

# read in the csv file and find all unique types of cities
df = pd.read_csv(input_file, sep=';', encoding='utf-8')
cities = df['Location'].unique()
# sort alphabetically
cities.sort()

# write the cities to a csv file
with open(output_file, 'w', encoding='utf-8') as f:
    f.write('City\n')
    for city in cities:
        f.write(city + '\n')