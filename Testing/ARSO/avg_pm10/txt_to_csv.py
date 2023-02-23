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


# testing

# tests = [  
#     "09.02.13 36 35 30 34 34 44 32 32 26 14 53 47 24 18 12 ",
#     "10.02.13 51 29 32 44 29 51 47 38 31 12 85 42 28 18 18 ",
#     "11.02.13 42 62 48 44 41 56 62 29 50 19 37 76 27 30 14 ",
#     "12.02.13 50 42 55 54 50 63 68 54 46 32 82 63 31 44 22 ",
#     "13.02.13 - 52 41 30 35 35 37 53 30 13 69 58 31 33 1 7 ",
#     "14.02.13 34 27 42 38 37 49 39 42 47 28 53 45 - 30 2 0 ",
#     "15.02.13 65 58 79 81 69 86 82 69 83 36 71 86 31 68 24 ",
#     "16.02.13 50 42 78 74 56 82 82 42 103 28 38 80 23 46  17 ",
#     "17.02.13 44 39 63 68 57 - 58 54 81 31 135 75 18 61 14 ",
#     "18.02.13 50 51 51 64 48 59 54 55 65 29 57 59 30 62 28 ",
#     "19.02.13 58 42 47 65 44 79 54 46 70 25 65 59 39 43 37 ",
#     "20.02.13 46 40 40 42 36 50 39 34 35 16 39 51 37 31 39 ",
#     "21.02.13 15 16 33 32 15 23 19 19 31 14 81 25 9 17 1 0 ",
#     "22.02.13 22 22 44 26 22 30 28 24 41 24 61 31 18 24 16 ",
#     "06.08.13 - 37 41 27 31 33 27 30 26 26 33 30 28 31 3 2 ",
#     "07.08.13 - 43 45 30 31 35 28 32 31 22 34 35 27 34 2 8 ",
#     "08.08.13 - 45 43 32 33 34 29 34 38 28 37 39 29 35 3 3 ",
#     "09.08.13 - 36 37 29 30 37 26 31 29 22 37 33 29 35 3 2 ",
#     "10.08.13 - 12 9 9 7 8 11 6 9 7 10 11 8 6 14 ",
#     "11.08.13 - 14 14 11 12 13 10 10 14 9 11 11 10 13 13  ",
#     "12.08.13 - 17 21 14 14 18 12 - 15 11 15 17 14 16 16  ",
#     "13.08.13 - 18 23 14 19 16 12 16 14 10 14 15 16 15 2 8 ",
#     "17.10.13 22 22 23 29 22 35 23 17 25 8 16 30 21 19 1 4 ",
#     "18.10.13 31 28 25 34 31 40 33 26 25 10 16 29 27 23 36 ",
#     "19.10.13 24 23 27 20 19 21 30 27 31 8 23 24 26 19 3 0 ",
#     "20.10.13 16 17 25 14 13 12 19 22 24 8 16 12 32 15 1 6 ",
#     "21.10.13 8 12 29 17 9 15 15 17 13 8 22 8 - 14 12 ",
#     "22.10.13 9 12 22 12 10 8 21 16 16 13 19 9 22 12 23 ",
#     "23.10.13 15 19 27 21 17 16 17 13 16 10 26 16 28 16 24 ",
#     "24.10.13 - 27 39 30 26 27 26 35 22 16 23 37 22 21 2 6 ",
#     "25.10.13 15 17 31 21 19 24 19 17 19 12 19 22 26 15 31 ",
#     "23.12.13 30 17 50 35 26 29 56 49 27 12 40 34 61 26 87 ",
#     "24.12.13 10 16 24 17 12 12 24 28 17 6 31 13 46 15 4 0 ",
#     "25.12.13 13 14 14 14 9 9 11 14 12 4 8 9 15 9 17 ",
#     "26.12.13 12 15 24 41 19 35 19 10 25 2 13 26 12 15 1 5 ",
#     "27.12.13 13 10 20 24 13 21 21 16 19 5 18 17 20 11 8  ",
#     "28.12.13 26 20 23 32 32 28 18 30 - 8 15 28 25 16 16  ",
#     "29.12.13 - 20 13 31 23 23 - 16 - 3 20 18 18 7 13 ",
# ]

# for test in tests:
#     print(test)
#     print(check_data(test))
#     print()

# quit()













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
            print(extract_everything_but_date(date_line).split(" "), number_of_elements)
            validity_dictionary[number_of_elements] = 1

    print(f"Found {len(date_lines)} lines that start with a date in {year}")
    # print all elements in validity_dictionary
    for key in validity_dictionary:
        print(f"Found {validity_dictionary[key]} lines with {key} elements")
    print("=====================================")


