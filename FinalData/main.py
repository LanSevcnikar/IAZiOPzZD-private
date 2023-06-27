import os
import glob
import pandas as pd

# ! THIS WORKED FOR THE FIRST 3, NOW I AM GOING FORWARD
# def freeze_rows(df, headers, header_names, sheet):
#     # Read mae the first and the second column until you either read the word "Time" or a year in plain text yyyy
#     row = 0
#     txt_data = ""

#     while True:
#         if type(df[sheet].iloc[row, 0]) == str and df[sheet].iloc[row, 0].lower().strip() == "time":
#             row += 1
#             break
#         try:
#             if df[sheet].iloc[row, 1].isnumeric() and len(str(df[sheet].iloc[row, 1])) == 4:
#                 row += 1
#                 break
#         except:
#             pass

#         attribute_name = df[sheet].iloc[row, 0]
#         attribute_value = df[sheet].iloc[row, 1]

#         if(type(attribute_value) == float and str(attribute_value) == "nan"):
#             attribute_value = df[sheet].iloc[row, 2]

#         if(type(attribute_name) == float and str(attribute_name) == "nan"):
#             row += 1
#             continue

#         header_names.append(attribute_name)
#         headers.append(attribute_value)

#         txt_data += str(attribute_name) + ": " + str(attribute_value) + "\n"

#         row += 1
#     return (row, txt_data)

# def find_years(df, sheet, starting_row):
#     years = []
#     column = 0

#     while True:
#         column += 1
#         try:
#             year = df[sheet].iloc[starting_row-1, column]
#             print(year)
#             if(type(year) == float and str(year) == "nan"):
#                 break
#             years.append((int(year), column))
#         except:
#             break
#     return (years)


# ! THIS WORKED FOR THE 4th AND 9th
# def freeze_rows(df, headers, header_names, sheet):
#     # Read me the first and the second column until you either read the word "Time" or a year in plain text yyyy
#     row = 0
#     txt_data = ""

#     while True:
#         if type(df[sheet].iloc[row, 0]) == str and df[sheet].iloc[row, 0].lower().strip() == "time":
#             row += 1
#             break
#         try:
#             if df[sheet].iloc[row, 1].isnumeric() and len(str(df[sheet].iloc[row, 1])) == 4:
#                 row += 1
#                 break
#         except:
#             pass

#         attribute_name = df[sheet].iloc[row, 0]
#         attribute_value = df[sheet].iloc[row, 1]

#         if(type(attribute_value) == float and str(attribute_value) == "nan"):
#             attribute_value = df[sheet].iloc[row, 2]

#         if(type(attribute_name) == float and str(attribute_name) == "nan"):
#             row += 1
#             continue

#         header_names.append(attribute_name)
#         headers.append(attribute_value)

#         txt_data += str(attribute_name) + ": " + str(attribute_value) + "\n"

#         row += 1
#     return (row, txt_data)

# def find_years(df, sheet, starting_row):
#     years = []
#     column = -1

#     while True:
#         column += 2
#         try:
#             year = df[sheet].iloc[starting_row-1, column]
#             if(type(year) == float and str(year) == "nan"):
#                 break
#             years.append((int(year), column))
#         except:
#             break
#     return (years)

# ! THIS WORKED FOR THE 5th AND 8th
# def freeze_rows(df, headers, header_names, sheet):
#     # Read me the first and the second column until you either read the word "Time" or a year in plain text yyyy
#     row = 0
#     txt_data = ""

#     while True:
#         if type(df[sheet].iloc[row, 0]) == str and df[sheet].iloc[row, 0].lower().strip() == "geo (labels)":
#             break

#         attribute_name = df[sheet].iloc[row, 0]
#         attribute_value = df[sheet].iloc[row, 1]

#         if(type(attribute_value) == float and str(attribute_value) == "nan"):
#             attribute_value = df[sheet].iloc[row, 2]

#         if(type(attribute_name) == float and str(attribute_name) == "nan"):
#             row += 1
#             continue

#         header_names.append(attribute_name)
#         headers.append(attribute_value)

#         txt_data += str(attribute_name) + ": " + str(attribute_value) + "\n"

#         row += 1
#     return (row, txt_data)

# def find_years(df, sheet, starting_row):
#     years = []
#     column = -1

#     while True:
#         column += 2
#         try:
#             year = df[sheet].iloc[starting_row-1, column]
#             if(type(year) == float and str(year) == "nan"):
#                 break
#             years.append((year, column))
#         except:
#             break
#     return (years)

# ! THIS FIND REGIONS WORKED FOR ALL BUT THE 7th AND 8th

# def find_regions(df, sheet, starting_row):
#     regions = []
#     while True:
#         starting_row += 1
#         try:
#             region = df[sheet].iloc[starting_row, 0]
#             if(type(region) == float and str(region) == "nan"):
#                 break
#             regions.append((region, starting_row))
#         except:
#             break
#     return (regions)


# ! THIS WORKED ON THE 6th
def freeze_rows(df, headers, header_names, sheet):
    # Read me the first and the second column until you either read the word "Time" or a year in plain text yyyy
    row = 0
    txt_data = ""

    while True:
        if type(df[sheet].iloc[row, 1]) == str and df[sheet].iloc[row, 1].lower().strip() == "geo (labels)":
            break

        attribute_name = df[sheet].iloc[row, 0]
        attribute_value = df[sheet].iloc[row, 1]

        if(type(attribute_value) == float and str(attribute_value) == "nan"):
            attribute_value = df[sheet].iloc[row, 2]

        if(type(attribute_name) == float and str(attribute_name) == "nan"):
            row += 1
            continue

        if(type(attribute_value) == str and attribute_name.lower().strip() == "time"):
            row += 1
            continue

        header_names.append(attribute_name)
        headers.append(attribute_value)

        txt_data += str(attribute_name) + ": " + str(attribute_value) + "\n"

        row += 1
    return (row, txt_data)


def find_regions(df, sheet, starting_row):
    regions = []
    while True:
        starting_row += 1
        try:
            region = df[sheet].iloc[starting_row, 1]
            if(type(region) == float and str(region) == "nan"):
                break
            regions.append((region, starting_row))
        except:
            break
    return (regions)


def find_years(df, sheet, starting_row):
    years = []
    column = 1

    while True:
        column += 1
        try:
            year = df[sheet].iloc[starting_row-1, column]
            if(type(year) == float and str(year) == "nan"):
                break
            years.append((year, column))
        except:
            break
    return (years)


def create_data_row(values):
    data_row = []
    for value in values:
        data_row.append(value)
    return data_row

folders_that_are_done = [
    "Area by NUTS 3 region",
    "Crimes recorded by the police by NUTS 3 regions",
    "Cultural employment by NUTS 2 regions",
    "Gross domestic product (GDP) at current market prices by NUTS 2 regions",
    "Population by current activity status, educational level and NUTS 2 region",
    

    "Private households by type, tenure status and NUTS 2 region",
    "Pupils and students enrolled by education level, sex and NUTS2 regions"

]

# loop through all the folders in this directory
for folder in os.listdir():
    excel_file_number = 1

    if folder in folders_that_are_done:
        continue
    print(folder)
    # loop through all excel files in this folder
    for file in glob.glob(folder + "/*.xlsx"):
        # read the excel file
        df = pd.read_excel(file, sheet_name=None)

        # create an txt file with the same name as the folder and add the number
        output_file = folder + "/" + folder + str(excel_file_number) + ".csv"
        excel_file_number += 1

        txt_data = ""
        first_sheet = True

        data_rows = []
        for sheet in list(df.keys())[2:]:
            # loop through the sheets from the third one onward
            header_names = []
            headers = []
            (starting_row, txt_data_temp) = freeze_rows(
                df, headers, header_names, sheet)
            txt_data += txt_data_temp + "\n"

            if(first_sheet):
                first_sheet = False
                data_row = create_data_row(
                    [*header_names, "Region", "Year", "Value"])
                data_rows.append(data_row)

            # find the regions and the years
            regions = find_regions(df, sheet, starting_row)
            years = find_years(df, sheet, starting_row)


            for region in regions:
                for year in years:
                    data_row = create_data_row(
                        [*headers, region[0], year[0], df[sheet].iloc[region[1], year[1]]])
                    data_rows.append(data_row)

        print(output_file)
        with open(output_file, "w", encoding="utf-8") as f:
            for data_row in data_rows:
                line = ""
                for data in data_row:
                    line += str(data) + ";"
                line = line[:-1]
                line += "\n"
                f.write(line)