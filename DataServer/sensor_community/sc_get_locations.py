import json
import requests

def get_sensor_community_locations():
    # Load all locations from file ./data.json
    with open('data.json') as f:
        data = json.load(f)
        print(data)
    # Return the locations
    return data
