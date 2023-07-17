import datetime
from time import sleep
import pandas as pd
import csv
import mysql.connector

cnx = mysql.connector.connect(
    host='aws.connect.psdb.cloud',           # Replace with your host
    user='ynez4krhqvm8d8l7gc04',       # Replace with your username
    password='pscale_pw_IBPNPuquQt36B8JT2O2wbodPZtitqEO039q6vWDF0xp',   # Replace with your password
    database='ida4health',    # Replace with your database name
    connection_timeout=600
)


def one():
    # open cities csv
    df = pd.read_csv('cities.csv', encoding="utf-8", sep=";")
    # for each city, output the following line (name, "By NUTS 2 classification")
    for city in df['city']:
        print("(\""+city+"\", \"By NUTS 2 classification\"),")

def get_dicts():
    location_to_id = {}
    ageGroup_to_id = {}
    seks_to_id = {}
    cause_to_id = {}

    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM location;")
    data = cursor.fetchall()
    cursor.close()
    for row in data:
        location_to_id[row[5]] = row[0]
    
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM ageGroup;")
    data = cursor.fetchall()
    cursor.close()
    for row in data:
        ageGroup_to_id[row[3]] = row[0]
    
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM sex;")
    data = cursor.fetchall()
    cursor.close()
    for row in data:
        seks_to_id[row[1]] = row[0]

    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM cause;")
    data = cursor.fetchall()
    cursor.close()
    for row in data:
        cause_to_id[row[1]] = row[0]

    return location_to_id, ageGroup_to_id, seks_to_id, cause_to_id


def insertHealth():
    with open('log.txt', 'w', encoding="utf-8") as log:
        csv_file = 'health.csv'  # Replace with the path to your CSV file

        # MySQL script templates
        health_data_point_value_template = "('{name}', (SELECT id FROM location WHERE name = '{location}'), (SELECT id FROM unit WHERE abbreviation = 'Standardized rate'), (SELECT id FROM ageGroup WHERE name = '{age_group}'), (SELECT id FROM sex WHERE name = '{sex}'), (SELECT id FROM cause WHERE name = '{cause}')), "
        health_data_point_template_2 = "SELECT id FROM healthDataPoint WHERE location =  {location} AND unit = {unit} AND ageGroup = {age_group} AND sex = {seks} AND cause = {cause};"
        measurement_template = " ('{datapoint_id}', '{measurement_date}', '{value}'), "

        dataPoint_to_id_dict = {}
        measurement_to_id_dict = {}

        sex_dict = {
            "Females": "female",
            "Total": "total",
            "Males": "male"
        }

        age_dict = {
            "65 years or over": "65 and up",
            "Total": "Total",
            "Less than 65 years": "up to 65"
        }
        location_to_id = {}
        ageGroup_to_id = {}
        seks_to_id = {}
        cause_to_id = {}


        dataPoints = []
        measurements = []

        stations = []
        count = 0

        with open(csv_file, 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=';')
            insert_h_query = "INSERT INTO healthDataPoint (name, location, unit, ageGroup, sex, cause) VALUES "
            for row in reader:
                name = f"Standardized rate of deaths from {row['name']}"
                location = (row['city_name'].replace("'", "\\'")).replace("\\\\", "\\")
                age_group = age_dict[row['age']]
                sex = sex_dict[row['sex']]
                cause = row['name']
                value = row['value']
                measurement_date = row['measurement_date'] + "-01-01 00:00:00" #
                timestamp = datetime.datetime.strptime(measurement_date, '%Y-%m-%d %H:%M:%S')

                count += 1
                dataPointIdentifier = (name,location,age_group,sex,cause)
                if(stations.count(dataPointIdentifier) == 0):
                    stations.append(dataPointIdentifier)
                    insert_h_query += health_data_point_value_template.format(
                        name=name,
                        location=location,
                        age_group=age_group,
                        sex=sex,
                        cause=cause
                    )

                if(count % 1000 == 0):
                    if(len(insert_h_query) == len("INSERT INTO healthDataPoint (name, location, unit, ageGroup, sex, cause) VALUES ")):
                        continue
                    print(count)
                    log.write(insert_h_query + "\n\n\n\n\n\n")
                    # cursor = cnx.cursor()
                    # insert_h_query = insert_h_query[:-2] + ";"
                    # cursor.execute(insert_h_query)
                    # cnx.commit()
                    # cursor.close()
                    insert_h_query = "INSERT INTO healthDataPoint (name, location, unit, ageGroup, sex, cause) VALUES "

            if(count % 1000 != 0):
                if(len(insert_h_query) != len("INSERT INTO healthDataPoint (name, location, unit, ageGroup, sex, cause) VALUES ")):
                    print(count)
                    log.write(insert_h_query + "\n\n\n\n\n\n")
                    # cursor = cnx.cursor()
                    # insert_h_query = insert_h_query[:-2] + ";"
                    # cursor.execute(insert_h_query)
                    # cnx.commit()
                    # cursor.close()

        

        count = 0
        print("Inserted ALL health data points")

        location_to_id, ageGroup_to_id, seks_to_id, cause_to_id = get_dicts()
        
        # dump all dicts to log
        log.write("location_to_id: " + str(location_to_id) + "\n")
        log.write("ageGroup_to_id: " + str(ageGroup_to_id) + "\n")
        log.write("seks_to_id: " + str(seks_to_id) + "\n")
        log.write("cause_to_id: " + str(cause_to_id) + "\n")

        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM healthDataPoint;")
        data = cursor.fetchall()
        cursor.close()
        print(len(data))

        for row in data:
            dataPointIdentifier = (row[2],row[4],row[5],row[6])
            dataPoint_to_id_dict[dataPointIdentifier] = row[0]
            log.write(str(dataPointIdentifier) + " " + str(row[0]) + "\n")
        
        print("Finished getting ids")
        

        count = 0

        with open(csv_file, 'r', encoding="utf-8") as file:

            reader = csv.DictReader(file, delimiter=';')
            insert_m_query = "INSERT INTO measurement (datapoint, timestamp, value) VALUES "
            for row in reader:
                name = f"Standardized rate of deaths from {row['name']}"
                location = (row['city_name'])
                age_group = age_dict[row['age']]
                sex = sex_dict[row['sex']]
                cause = row['name']
                value = row['value']
                measurement_date = row['measurement_date'] + "-01-01 00:00:00" #
                timestamp = datetime.datetime.strptime(measurement_date, '%Y-%m-%d %H:%M:%S')

                count += 1
                dataPointIdentifier = (
                    location_to_id[location],
                    ageGroup_to_id[age_group],
                    seks_to_id[sex],
                    cause_to_id[cause]
                )

                measurement_query = measurement_template.format(
                    datapoint_id=dataPoint_to_id_dict[dataPointIdentifier],
                    value=value,
                    measurement_date=timestamp
                )
                insert_m_query += measurement_query

                if(count % 1000 == 0):
                    log.write(insert_m_query + "\n\n\n\n\n\n")
                    print(count)
                    cursor = cnx.cursor()
                    insert_m_query = insert_m_query[:-2] + ";"
                    cursor.execute(insert_m_query)
                    insert_m_query = "INSERT INTO measurement (datapoint, timestamp, value) VALUES "
                    cnx.commit()
                    cursor.close()

                

                # dataPoints.append(health_data_point_query)
                # measurements.append(measurement_query)

        dataPoints = list(set(dataPoints))

        
                
        i = 0
        with open('health_data_points.sql', 'w', encoding="utf-8") as file:
                
            for query in dataPoints:
                i += 1
                if(i % 1000 == 0):
                    file.write("\n\n\n\n")
                file.write(query)
        
        with open('measurements.sql', 'w', encoding="utf-8") as file:
            for query in measurements:
                file.write(query)

    
def insertPollutants():
    csv_file = 'pollutants.csv'

    location_to_id = {}
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM location;")
    data = cursor.fetchall()
    cursor.close()
    for row in data:
        location_to_id[row[5]] = row[0]


    pollutant_data_point_value_template = "({location}, 5, '{description}'), "
    pollutant_data = "INSERT INTO dataPoint (location, unit, description) VALUES "

    # with open(csv_file, 'r', encoding="utf-8") as file:
    #     reader = csv.DictReader(file, delimiter=';')
    #     for row in reader:
    #         location = location_to_id[row['NUTS Region']]
    #         if(row["CO"] != ""):
    #             pollutant_data += pollutant_data_point_value_template.format(
    #                 description=f"Pollution from CO by EAQP",
    #                 location=location,
    #             )
    #         if(row["NO2"] != ""):
    #             pollutant_data += pollutant_data_point_value_template.format(
    #                 description=f"Pollution from NO2 by EAQP",
    #                 location=location,
    #             )
    #         if(row["O3"] != ""):
    #             pollutant_data += pollutant_data_point_value_template.format(
    #                 description=f"Pollution from O3 by EAQP",
    #                 location=location,
    #             )
    #         if(row["PM10"] != ""):
    #             pollutant_data += pollutant_data_point_value_template.format(
    #                 description=f"Pollution from PM10 by EAQP",
    #                 location=location,
    #             )
    #         if(row["NO"] != ""):
    #             pollutant_data += pollutant_data_point_value_template.format(
    #                 description=f"Pollution from NO by EAQP",
    #                 location=location,
    #             )
    #         if(row["SO2"] != ""):
    #             pollutant_data += pollutant_data_point_value_template.format(
    #                 description=f"Pollution from SO2 by EAQP",
    #                 location=location,
    #             )
    #     cursor = cnx.cursor()
    #     pollutant_data = pollutant_data[:-2] + ";"
    #     print(pollutant_data)
    #     cursor.execute(pollutant_data)
    #     cnx.commit()
    #     cursor.close()
    #     print("Inserted pollutant data points")
    
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM dataPoint WHERE description LIKE '%by EAQP';")
    data = cursor.fetchall()
    cursor.close()
    print(len(data))

    identifier_to_id = {}
    for row in data:
        identifier_to_id[(row[2], row[3])] = row[0]

    
    measurement_data = "INSERT INTO measurement (datapoint, timestamp, value) VALUES "
    measurement_template = " ('{datapoint_id}', '{measurement_date}', '{value}'), "

    with open(csv_file, 'r', encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            measurement_date = "2020-12-31"
            timestamp = datetime.datetime.strptime(measurement_date, '%Y-%m-%d %H:%M:%S')
            location = location_to_id[row['NUTS Region']]
            if(row["CO"] != ""):
                measurement_data += measurement_template.format(
                    datapoint_id=identifier_to_id[(location, "Pollution from CO by EAQP")],
                    measurement_date=timestamp,
                    value=row["CO"]
                )
            if(row["NO2"] != ""):
                measurement_data += measurement_template.format(
                    datapoint_id=identifier_to_id[(location, "Pollution from NO2 by EAQP")],
                    measurement_date=timestamp,
                    value=row["NO2"]
                )
            if(row["O3"] != ""):
                measurement_data += measurement_template.format(
                    datapoint_id=identifier_to_id[(location, "Pollution from O3 by EAQP")],
                    measurement_date=timestamp,
                    value=row["O3"]
                )
            if(row["PM10"] != ""):
                measurement_data += measurement_template.format(
                    datapoint_id=identifier_to_id[(location, "Pollution from PM10 by EAQP")],
                    measurement_date=timestamp,
                    value=row["PM10"]
                )
            if(row["NO"] != ""):
                measurement_data += measurement_template.format(
                    datapoint_id=identifier_to_id[(location, "Pollution from NO by EAQP")],
                    measurement_date=timestamp,
                    value=row["NO"]
                )
            if(row["SO2"] != ""):
                measurement_data += measurement_template.format(
                    datapoint_id=identifier_to_id[(location, "Pollution from SO2 by EAQP")],
                    measurement_date=timestamp,
                    value=row["SO2"]
                )
        cursor = cnx.cursor()
        measurement_data = measurement_data[:-2] + ";"
        print(measurement_data)
        cursor.execute(measurement_data)
        cnx.commit()
        cursor.close()
        print("Inserted pollutant measurements")


        


                
                

insertPollutants()