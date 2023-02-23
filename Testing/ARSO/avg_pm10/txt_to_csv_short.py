import os
import re
import time
import csv

def starts_with_valid_date(date_text):
    #remove all spaces from the date_text
    date_text = date_text.replace(" ", "")
    # create a regex that checks if it starts with format dd.dd.dd with the last one being of length anywhere between 2 and 4 and there can be whitespace anywhere
    date_regex = r"^\d{1,2}.\d{1,2}.\d{2,4}"
    # check if the date_text matches the regex
    if(re.search(date_regex, date_text)):
        return True
    return False

def extract_date(date_text):
    date_regex = r"^\d{1,2}.\d{1,2}.\d{2,4}"
    date = re.search(date_regex, date_text)
    if(date):
        return date.group(0)
    return ""

def extract_everything_but_date(date_text):
    date_regex = r"^\d{1,2}.\d{1,2}.\d{2,4}"
    return re.sub(date_regex, "", date_text)


years = [
    2013,
    2014,
    2019,
    2020,
    2021,
    2022
]

# delete all files in data_csv but leave the folders alone
for filename in os.listdir('./data_csv'):
    try:
        os.remove(f"./data_csv/{filename}")
    except:
        pass
    
# Read the data_txt/{year}.txt and save all the text to one variable
for year in years:
    # create a dictionary that will hold the number of lines that have some number of elements
    # the key will be the number of elements and the value will be the number of lines
    # this will be used to check if the data is in the correct format

    validity_dictionary = {}

    with open(f"./data_txt/{year}.txt", "r", encoding='utf-8') as file:
        data = file.read()
        
    # Split the data by new line
    data_by_lines = data.split("\n")
    date_lines = []

    # Find all the lines that start with a date
    for line in data_by_lines:
        line = line.replace(". ", ".")
        if(starts_with_valid_date(line)):
            date_lines.append(line)

    for date_line in date_lines:
        if(extract_date(date_line) == ""):
            print(date_line)
        number_of_elements = extract_everything_but_date(date_line).split(" ")
        #remove empty elements
        number_of_elements = [x for x in number_of_elements if x != ""]
        number_of_elements = len(number_of_elements)
        if(number_of_elements in validity_dictionary):
            validity_dictionary[number_of_elements] += 1
        else:
            print(extract_everything_but_date(date_line).split(" "), number_of_elements, date_line)
            validity_dictionary[number_of_elements] = 1

    for line_index in range(len(data_by_lines)):
        if(data_by_lines[line_index] == "Dan/"):
            text = ""
            while(starts_with_valid_date(data_by_lines[line_index]) == False):
                text += data_by_lines[line_index] + '\n'
                line_index += 1
            text = text.split(" ")
            for name_index in range(len(text)):
                text[name_index] = text[name_index].replace("\n","")
            print(text)

    print(f"Found {len(date_lines)} lines that start with a date in {year}")
    # print all elements in validity_dictionary
    for key in validity_dictionary:
        print(f"Found {validity_dictionary[key]} lines with {key} elements")
    print("=====================================")

