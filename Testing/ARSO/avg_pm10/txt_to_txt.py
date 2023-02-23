import os
import re
import time
import csv


def is_date(data):
    # remove all spaces from the date_text
    data = data.replace(" ", "")
    # create a regex that checks if it starts with format dd.dd.dd with the last one being of length anywhere between 2 and 4 and there can be whitespace anywhere
    date_regex = r"^\d{1,2}.\d{1,2}.\d{2,4}"
    # check if the date_text matches the regex
    if(re.search(date_regex, data)):
        return True
    return False

def is_value(data):
    if(len(data) == 0):
        return False
    if(is_date(data)):
        return False
    if(data[0].isdigit() or data[0] == '-'):
        return True
    return False
        


def get_corrected_month(month):
    line_index = 0
    corrected_month = [month[0]]
    while line_index < len(month):
        if(is_date(month[line_index])):
            corrected_string = month[line_index]
            line_index += 1
            while line_index < len(month) and is_value(month[line_index]):
                corrected_string += f" {month[line_index]}"
                line_index += 1
            corrected_month.append(corrected_string)
            line_index -= 1
        line_index += 1
    return corrected_month



years = [ 2015, 2016, 2017, 2018 ]

# delete all files in data_csv but leave the folders alone
for filename in os.listdir('./data_csv'):
    try:
        os.remove(f"./data_csv/{filename}")
    except:
        pass

# Read the data_txt/{year}.txt and save all the text to one variable
for year in years:
    print(f"Year: {year}")
    # create a dictionary that will hold the number of lines that have some number of elements
    # the key will be the number of elements and the value will be the number of lines
    # this will be used to check if the data is in the correct format

    validity_dictionary = {}

    with open(f"./data_txt/{year}_temp.txt", "r", encoding='utf-8') as file:
        data = file.read()

    months = []

    # Split the data by new line
    data_by_lines = data.split("\n")
    line_index = 0
    while line_index < len(data_by_lines):
        line = data_by_lines[line_index]
        if(line.startswith("stran")):
            line_index += 1
            month_lines = []
            while line_index < len(data_by_lines) and not data_by_lines[line_index].startswith("stran"):
                month_lines.append(data_by_lines[line_index])
                line_index += 1
            line_index -= 1
            months.append(month_lines)
        line_index += 1
    

    
    with open(f"./data_txt/{year}.txt", "w", encoding='utf-8') as file:
        for month in months:
            month = month[6:]
            corrected_month = get_corrected_month(month)
            for line in corrected_month:
                file.write(line + "\n")
                if(line[0].isdigit()):
                    number_of_elements = len(line.split(" "))
                    if(number_of_elements in validity_dictionary):
                        validity_dictionary[number_of_elements] += 1
                    else:
                        validity_dictionary[number_of_elements] = 1

    for key in validity_dictionary:
        print(f"{key} elements: {validity_dictionary[key]}")


    print("=====================================")
