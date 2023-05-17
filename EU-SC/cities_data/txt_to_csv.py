import csv
import requests

# OpenCage Geocoding API endpoint
geocoding_api_url = "https://api.opencagedata.com/geocode/v1/json"

# Open the file containing the list of city names
with open("german_cities.txt", "r", encoding="utf-8") as f:
    city_names = f.read().splitlines()

# Create a list to store the results
results = []

# Loop through the city names and call the OpenCage Geocoding API for each one
for city_name in city_names:
    print(f"Processing {city_name}...")
    # Construct the query parameters
    params = {
        "key": "91d8adc8e3a04c75ba8b6bd287426c3f",
        "q": city_name,
        "limit": 1
    }

    

    # Send the request to the API
    response = requests.get(geocoding_api_url, params=params)

    # Parse the JSON response and extract the latitude and longitude
    data = response.json()
    try:
        lat = data["results"][0]["geometry"]["lat"]
        lon = data["results"][0]["geometry"]["lng"]

        # Add the city name, latitude, and longitude to the results list
        results.append([city_name, lat, lon])
    except:
        print(f"Error processing {city_name}")

# Save the results to a CSV file
with open("city_coords.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["City", "Latitude", "Longitude"])
    writer.writerows(results)

print("Done!")
