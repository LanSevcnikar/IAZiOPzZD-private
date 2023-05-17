# create a program that parses the xlsx file and outputs a csv file. Mind you that the original file has 101 sheets and I only want the data from the 3rd sheet onward

import pandas as pd
import numpy as np
import os
import glob
import re

input_file = "C:/Users/sevcn/Documents/programming/projects/IAZiOPzZD-private/GermanyPoC/EuroStat/og_data.xlsx"
output_file = "C:/Users/sevcn/Documents/programming/projects/IAZiOPzZD-private/GermanyPoC/EuroStat/data.csv"

# there is only one file called raw_data.xlsx
# read it in

# read in the excel file
df = pd.read_excel(input_file, sheet_name=None)

# create a file called data.csv and create headers called Time frequency; Unit of measure;	Sex	Age class;	ICD-10 2010; year; value
# create a list of the headers

headers = [
    'Time Frequency',
    'Unit Of Measure',
    'Sex',
    'Age Class',
    'ICD-10 2010',
    'Location',
    'Year',
    'Value',

]

# write the headers to the file
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(';'.join(headers) + '\n')

    # create a list of the sheets
    sheets = list(df.keys())

    # create a list of the sheets that we want to keep
    sheets_to_keep = sheets[2:]

    # create a list of the dataframes
    dataframes = []

    # loop through the sheets and create a dataframe for each sheet
    for sheet in sheets_to_keep:
        print(sheet)
        # read the data on 5C,6C,7C,8C,9C
        sheet_time_frequency = df[sheet].iloc[3, 2]
        sheet_unit_of_measure = df[sheet].iloc[4, 2]
        sheet_sex = df[sheet].iloc[5, 2]
        sheet_age_class = df[sheet].iloc[6, 2]
        sheet_icd_10_2010 = df[sheet].iloc[7, 2]

        # loop through the locations that are on the cells A13:A67
        for i in range(11, 67):
            location = df[sheet].iloc[i, 0]
            # loop through the years that are on the collumns B:T
            for j in range(1, 20):
                year = df[sheet].iloc[9, j]
                value = df[sheet].iloc[i, j]
                try:
                    value = float(value)
                    year = int(year)
                    if(year > 2020 or year < 201):
                        continue
                    f.write(
                        ';'.join([
                            sheet_time_frequency,
                            sheet_unit_of_measure,
                            sheet_sex,
                            sheet_age_class,
                            sheet_icd_10_2010,
                            location,
                            str(year),
                            str(value)
                        ]) + '\n'
                    )
                except:
                    continue
