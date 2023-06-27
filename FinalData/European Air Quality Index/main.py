from collections import defaultdict
import json
import geopandas as gpd
from shapely.geometry import Point
# read the json
stations = json.load(open('stations.json'))
indexes = json.load(open('index.json'))
gdf = gpd.read_file('../EUS Visualization/data/NUTS_RG_01M_2021_4326.shp')

averages = defaultdict(lambda: {'sum': 0, 'count': 0})

i = 0
for station in stations:
    i += 1
    value, lat, long = None, None, None
    try:
        value = indexes[station['code']]
        lat = station['lat']
        long = station['lon']
        for index, row in gdf.iterrows():
            if row['geometry'].contains(Point(long, lat)):
                if row ['LEVL_CODE'] == 2:
                    if(value != None):
                        averages[row['NUTS_ID']]['sum'] += value
                        averages[row['NUTS_ID']]['count'] += 1
    except: 
        pass
    print(f'Done with {i} out of {len(stations)}')

for key in averages:
    averages[key] = averages[key]['sum'] / averages[key]['count']

with open('averages.json', 'w') as f:
    json.dump(averages, f)