import geopandas as gpd
import matplotlib.pyplot as plt
import mplleaflet

# Load your shapefile data into a GeoDataFrame
path = "./shapefiles/Europe/Europe.shp"
data = gpd.read_file(path)

# Plot the map
fig, ax = plt.subplots(figsize=(10, 10))
data.plot(ax=ax, alpha=0.5, edgecolor='k')

# Set the title and show the plot
mplleaflet.show(fig=fig)