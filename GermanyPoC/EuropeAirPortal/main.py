import pandas as pd

input_file = 'C:/Users/sevcn/Documents/programming/projects/IAZiOPzZD-private/GermanyPoC/EuropeAirPortal/DataExtract.csv'

# from the input file, remove all collumns that are not in keep_labels
keep_labels = [
    'Country',
    'Air Pollutant',
    'Data Aggregation Process',
    'Year',
    'Air Pollution Level',
    'Unit Of Air Pollution Level',
    'Air Quality Station Type',
    'Air Quality Station Area',
    'Longitude',
    'Latitude',
    'City',
    'Calculation Time'
]

# read in the csv file
df = pd.read_csv(input_file, sep=',', encoding='utf-8')

#print all column names
print(df.columns)

# remove all collumns that are not in keep_labels
df = df[keep_labels]

# save as EEAData.csv
df.to_csv('EEAData.csv', sep=',', encoding='utf-8', index=False)
