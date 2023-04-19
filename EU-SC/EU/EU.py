import csv
import datetime
from itertools import groupby
import json
from multiprocessing import Pool
from bs4 import BeautifulSoup
import requests
from collections import defaultdict


def is_it_the_correct_date_of_a_row(row):
    # check for every column if it is a date
    for i, column in enumerate(row):
        try:
            # if it is a date, convert it to a datetime object
            row[i] = datetime.datetime.strptime(column[:10], "%Y-%m-%d")
            # check if it is the first of any month
            if row[i].day == 1:
                # return the date in format yyyy-mm
                return row[i].strftime("%Y-%m")

        except ValueError:
            # if it is not a date, just skip it
            pass
    return -1


def find_the_measurement(row, first_row):
    # check the first row for a column concentration and if it exists, find its index
    for i, column in enumerate(first_row):
        if column == "Concentration":
            # if it exists, return the measurement of the row
            return row[i]

    # If it does not exist, find a value that is a double and return that
    for i, column in enumerate(first_row):
        try:
            # if it is a double, return it
            value = float(row[i])
            return value
        except ValueError:
            # if it is not a double, just skip it
            pass


def download_csv(url):
    response = requests.get(url)

    # find all the meassurements that are done on the first of any month
    # and return the data as an array
    data = response.text.split("\n")
    data = [row.split(",") for row in data]

    return_data = []

    for row in data:
        date = is_it_the_correct_date_of_a_row(row)
        if date != -1:
            measurement = find_the_measurement(row, data[0])
            return_data.append((date, measurement))

    print(f"Got data from {url}")
    return return_data


def get_data_from_eu(city_name, country_code, start_year, end_year, measurement_type):
    pollutant_to_code = {
        "(CH3)2-CH-CH2-CH2-CH3": 316,
        "As": 7018,
        "As in PM10": 5018,
        "As in PM2.5": 1018,
        "BaP": 7029,
        "BaP in PM10": 5029,
        "BaP in PM2.5": 1029,
        "Benzo(a)anthracene": 611,
        "Benzo(a)anthracene in PM10": 5610,
        "Benzo(a)anthracene in PM2.5": 1610,
        "Benzo(b)fluoranthene": 618,
        "Benzo(b)fluoranthene in PM10": 5617,
        "Benzo(b)fluoranthene in PM2.5": 1617,
        "Benzo(b,j)fluorantheneinPM10": 5480,
        "Benzo(b,j,k)fluoranthene": 7380,
        "Benzo(b,j,k)fluorantheneInPM1": 5380,
        "Benzo(j)fluoranthene": 760,
        "Benzo(j)fluoranthene in PM10": 5759,
        "Benzo(j)fluoranthene in PM2.5": 1759,
        "Benzo(k)fluoranthene": 627,
        "Benzo(k)fluoranthene in PM10": 5626,
        "Benzo(k)fluoranthene in PM2.5": 1626,
        "BS": 6,
        "C2H6": 428,
        "C6H14": 443,
        "C6H5-C2H5": 431,
        "C6H5-CH3": 21,
        "C6H6": 20,
        "C7H16": 441,
        "Ca2+ in PM10": 5629,
        "Ca2+ in PM2.5": 1629,
        "Cd": 7014,
        "Cd in PM10": 5014,
        "Cd in PM2.5": 1014,
        "CH2=CH-C(CH3)=CH2": 451,
        "CH2=CH-CH=CH2": 24,
        "CH2=CH-CH3": 505,
        "CH4": 41,
        "cis-H3C-CH=CH-CH3": 6007,
        "Cl- in PM10": 5631,
        "Cl- in PM2.5": 1631,
        "CO": 10,
        "Co in PM10": 5064,
        "CO2": 71,
        "Cu in PM10": 5073,
        "Dibenzo(ah)anthracene": 7419,
        "Dibenzo(ah)anthracene in PM10": 5419,
        "Dibenzo(ah)anthracene in PM2.5": 1419,
        "EC in PM10": 5771,
        "EC in PM2.5": 1771,
        "H2C=CH2": 430,
        "H2C=CH-CH2-CH3": 6005,
        "H2S": 11,
        "H3C-(CH2)3-CH3": 486,
        "H3C-CH(CH3)2": 447,
        "H3C-CH2-CH(CH3)2": 450,
        "H3C-CH2-CH2-CH3": 394,
        "H3C-CH2-CH3": 503,
        "HC=CH": 432,
        "Hg": 7013,
        "Hg in PM2.5": 1013,
        "Hg0 + Hg-reactive": 4813,
        "Indeno-(1,2,3-cd)pyrene": 656,
        "Indeno-(1,2,3-cd)pyrene in PM": 5655,
        "Indeno-(1,2,3-cd)pyrene in PM2": 1655,
        "K+ in PM10": 5657,
        "K+ in PM2.5": 1657,
        "m,p-C6H4(CH3)2": 464,
        "Mg2+ in PM10": 5659,
        "Mg2+ in PM2.5": 1659,
        "Mn in PM10": 5017,
        "N2O": 425,
        "Na+ in PM10": 5668,
        "Na+ in PM2.5": 1668,
        "NH3": 35,
        "NH4+ in PM10": 5045,
        "NH4+ in PM2.5": 1045,
        "Ni": 7015,
        "Ni in PM10": 5015,
        "Ni in PM2.5": 1015,
        "NO": 38,
        "NO2": 8,
        "NO3- in PM10": 5046,
        "NO3- in PM2.5": 1046,
        "NOX as NO2": 9,
        "O3": 7,
        "OC in PM10": 5772,
        "OC in PM2.5": 1772,
        "o-C6H4-(CH3)2": 482,
        "Pb": 7012,
        "Pb in PM10": 5012,
        "Pb in PM2.5": 1012,
        "PM1": 6002,
        "PM10": 5,
        "PM2.5": 6001,
        "SO2": 1,
        "SO42- in PM10": 5047,
        "SO42- in PM2.5": 1047,
        "THC (NM)": 32,
        "trans-H3C-CH=CH-CH3": 6006,
        "V in PM10": 5049,

    }

    pollutant_code = pollutant_to_code[measurement_type]
    source_url = f"https://fme.discomap.eea.europa.eu/fmedatastreaming/AirQualityDownload/AQData_Extract.fmw?CountryCode={country_code}&CityName={city_name}&Pollutant={pollutant_code}&Year_from={start_year}&Year_to={end_year}&Station=&Samplingpoint=&Source=All&Output=HTML&UpdateDate=&TimeCoverage=Year"

    # Get the data from the source
    response = requests.get(source_url)
    print(f"Got data from {source_url}")
    # use bs4 to parse the html and find all the links
    soup = BeautifulSoup(response.text, "html.parser")
    link_elements = soup.find_all("a")
    links = [link_element["href"] for link_element in link_elements]

    all_data = []

    # using multiprocessing, download all the csv files
    with Pool(4) as p:
        all_data = p.map(download_csv, links)

        result = defaultdict(list)

        # loop over the data and aggregate it
        for data in all_data:
            for key, value in data:
                if(value != ''):
                    try:
                        result[key].append(float(value))
                    except ValueError:
                        pass

        # create the final output list by joining the key and averaging the values
        reformatted = [(key, sum(values) / len(values))
                       for key, values in result.items()]

        return reformatted

    # flatten the array


if __name__ == "__main__":
    get_data_from_eu("Berlin", "DE", 2021, 2021, "PM10")
