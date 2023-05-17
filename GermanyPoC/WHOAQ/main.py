# open the local file data.xlsx and into a separate file germany.csv write the data from the excel file where the column WHO COUNTRY NAME is equal to Germany
#
# Path: GermanyPoC\WHOAQ\main.py

import pandas as pd
import numpy as np
import os

# read the excel file
file_name = 'C:/Users/sevcn/Documents/programming/projects/IAZiOPzZD-private/GermanyPoC/WHOAQ/data.xlsx'
df = pd.read_excel(file_name, sheet_name='AAP_2022_city_v9')

# filter the data
df = df[df['WHO Country Name'] == 'Germany']

# write the data to a csv file
df.to_csv('C:/Users/sevcn/Documents/programming/projects/IAZiOPzZD-private/GermanyPoC/WHOAQ/germany.csv', index=False)
