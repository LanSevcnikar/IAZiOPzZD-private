# This will be a GUI for the sensor.community project
# One must be able to input latitude and longitude and get a sorted list of all sensors by proximity
# The user can then select a sensor and a time frame and have a button to download the data

import json
import math
import os
import tkinter as tk
from matplotlib import pyplot as plt
import requests
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


LJUBLJANA_LAT = 46.056946
LJUBLJANA_LONG = 14.505751
STARTING_DATE = "2022-12-01"
ENDING_DATE = "2022-12-31"

class BufferingWindow:
    def __init__(self, master, text='Loading...'):
        self.parent = master
        self.top = tk.Toplevel(master)
        self.top.title('')
        self.top.resizable(False, False)
        self.top.attributes('-topmost', True)
        self.top.transient(master)
        self.top.protocol("WM_DELETE_WINDOW", self.on_close)
        self.top.bind('<Escape>', self.on_close)

        # Center the loading window
        master.update_idletasks()
        x = master.winfo_x() + (master.winfo_width() // 2) - 200
        y = master.winfo_y() + (master.winfo_height() // 2) - 100
        self.top.geometry('400x200+{}+{}'.format(x, y))

        # Create a label to display the text
        self.label = tk.Label(self.top, text=text)
        self.label.pack(pady=50)

    def destroy(self):
        self.top.destroy()

    def on_close(self, event=None):
        self.top.destroy()

class SensorCommunityGUI:
    def __init__(self, master):
        self.master = master
        master.title("Sensor Community")

        # Create latitude and longitude input fields
        self.lat_label = tk.Label(master, text="Latitude:")
        self.lat_label.pack()
        self.lat_entry = tk.Entry(master)
        self.lat_entry.insert(0, str(LJUBLJANA_LAT))
        self.lat_entry.pack()
        self.long_label = tk.Label(master, text="Longitude:")
        self.long_label.pack()
        self.long_entry = tk.Entry(master)
        self.long_entry.insert(0, str(LJUBLJANA_LONG))
        self.long_entry.pack()

        # Create button to sort sensors by proximity
        self.sort_button = tk.Button(
            master, text="Sort Sensors", command=self.sort_sensors)
        self.sort_button.pack()

        # Create listbox to display sorted sensors
        self.sensor_list = tk.Listbox(master, width=50)
        self.sensor_list.pack()

        # Create starting date and ending date input fields
        # Add them the base starting value of 2022-12-01 and 2022-12-31
        self.start_date_label = tk.Label(master, text="Start Date:")
        self.start_date_label.pack()
        self.start_date_entry = tk.Entry(master)
        self.start_date_entry.insert(0, str(STARTING_DATE))
        self.start_date_entry.pack()
        self.end_date_label = tk.Label(master, text="End Date:")
        self.end_date_label.pack()
        self.end_date_entry = tk.Entry(master)
        self.end_date_entry.insert(0, str(ENDING_DATE))
        self.end_date_entry.pack()

        # Create button to download data for selected sensor and time frame
        self.download_button = tk.Button(
            master, text="Download Data", command=self.download_data)
        self.download_button.pack()

        # Create a text object in which I will keep the info about the selected sensor
        self.lat_label = tk.Label(master, text="Last clicked sensor:")
        self.lat_label.pack()
        self.selected_sensor_data = tk.Text(master, width=40, height=10)
        self.selected_sensor_data.pack()

        # Initialize variables
        self.sensor_data = []
        # make the value null
        self.selected_sensors = []

        # Create a bit of a break
        self.break_label = tk.Label(master, text=" ")

        # Create a matplotlib figure
        self.fig = plt.figure(figsize=(5, 5), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_title("Sensor Data")
        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("PM2.5")
        self.canvas = FigureCanvasTkAgg(self.fig, master=master)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()


    def sort_sensors(self):
        # Get latitude and longitude from input fields
        latitude = float(self.lat_entry.get())
        longitude = float(self.long_entry.get())

        # Check if there already exists a file called data/sensors.json.
        # If it does, read from it, otherwise call the API and save the data to the file
        try:
            with open(f"data/sensors.json") as f:
                self.sensor_data = json.load(f)
        except FileNotFoundError:
            self.sensor_data = requests.get(
                "https://maps.sensor.community/data/v1/data.json").json()
            with open(f"data/sensors.json", "w") as f:
                json.dump(self.sensor_data, f)

        # Calculate distance from each sensor to input location
        for sensor in self.sensor_data:
            sensor_lat = float(sensor["location"]["latitude"])
            sensor_long = float(sensor["location"]["longitude"])
            sensor["distance"] = self.distance(
                latitude, longitude, sensor_lat, sensor_long)

        # Sort sensors by distance
        self.sensor_data.sort(key=lambda s: s["distance"])

        # Update sensor list
        self.sensor_list.delete(0, tk.END)
        for sensor in self.sensor_data:
            self.sensor_list.insert(
                tk.END, f"{sensor['sensor']['sensor_type']['name']} - {sensor['sensor']['id']} - {round(sensor['distance'],3)}")

    
    def download_data(self):
        buffering_window = BufferingWindow(self.master)
        for sensor in self.selected_sensors:
            if not os.path.exists("data/" + str(sensor['sensor']['sensor_type']['name']) + '-' + str(sensor['sensor']['id'])):
                os.makedirs(
                    "data/" + str(sensor['sensor']['sensor_type']['name']) + '-' + str(sensor['sensor']['id']))

        starting_date = self.start_date_entry.get()
        ending_date = self.end_date_entry.get()

        for date_full in pd.date_range(starting_date, ending_date):
            date_short = date_full.strftime('%Y-%m-%d')
            base_url = 'https://archive.sensor.community/'
            for sensor in self.selected_sensors:
                sensor_name = str(sensor['sensor']['sensor_type']['name'])
                sensor_id = str(sensor['sensor']['id'])

                url = base_url + date_short + '/' + date_short + \
                    '_' + sensor_name + '_sensor_' + sensor_id + '.csv'
                url = url.lower()
                # try downaloding the cvs file from the url, if it does not work, continue
                # then save it to the folder of the sensor
                # check first if the file has already been downloaded
                if os.path.exists("data/" + sensor_name + '-' + sensor_id + '/' + date_short + '_' + sensor_name + '_sensor_' + sensor_id + '.csv'):
                    continue
                try:
                    request = requests.get(url)
                    with open("data/" + sensor_name + '-' + sensor_id + '/' + date_short + '_' + sensor_name + '_sensor_' + sensor_id + '.csv', 'wb') as f:
                        f.write(request.content)
                except:
                    print('Could not download ' + url)
                    continue
        buffering_window.destroy()
    def distance(self, lat1, long1, lat2, long2):
        # Calculate distance between two points using the Haversine formula
        R = 6371  # Radius of the Earth in kilometers

        # Convert latitude and longitude to radians
        lat1, long1, lat2, long2 = map(
            math.radians, [lat1, long1, lat2, long2])

        # Calculate the differences between the latitudes and longitudes
        d_lat = lat2 - lat1
        d_long = long2 - long1

        # Apply the Haversine formula
        a = math.sin(d_lat / 2) ** 2 + math.cos(lat1) * \
            math.cos(lat2) * math.sin(d_long / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        d = R * c

        return d

    def on_select(self, event):
        # Get selected sensor from listbox
        widget = event.widget
        index = 0
        try:
            index = int(widget.curselection()[0])
        except:
            return
        # if the selected sensor is in the list, remove it, otherwise add it
        if self.sensor_data[index] in self.selected_sensors:
            self.selected_sensors.remove(self.sensor_data[index])
            self.sensor_list.itemconfig(index, bg="")
        else:
            self.selected_sensors.append(self.sensor_data[index])
            self.sensor_list.itemconfig(index, bg="yellow")

        sensor_data_as_string = ""
        sensor_data_as_string += f"Sensor type: {self.sensor_data[index]['sensor']['sensor_type']['name']}\n"
        sensor_data_as_string += f"Sensor ID: {self.sensor_data[index]['sensor']['id']}\n"
        sensor_data_lat = round(float(self.sensor_data[index]['location']['latitude']), 3)
        sensor_data_long = round(float(self.sensor_data[index]['location']['longitude']), 3)
        sensor_data_as_string += f"Sensor location: {self.sensor_data[index]['location']['country']}, {sensor_data_lat}, {sensor_data_long}\n"
        sensor_data_as_string += f"Sensor inside: {self.sensor_data[index]['location']['indoor']}\n"
        sensor_data_as_string += f"\n====== Data: ======\n\n"
        for sensor_data_value in self.sensor_data[index]['sensordatavalues']:
            if(sensor_data_value['value_type'] == "P1"):
                sensor_data_as_string += f"PM10: {sensor_data_value['value']}\n"
            elif(sensor_data_value['value_type'] == "P2"):
                sensor_data_as_string += f"PM2.5: {sensor_data_value['value']}\n"
            else:
                sensor_data_as_string += f"{sensor_data_value['value_type']}: {sensor_data_value['value']}\n"
        self.selected_sensor_data.delete("1.0", "end")
        self.selected_sensor_data.insert("1.0", sensor_data_as_string)
        # deselect the item
        self.sensor_list.selection_clear(index)


root = tk.Tk()
gui = SensorCommunityGUI(root)
gui.sensor_list.bind('<<ListboxSelect>>', gui.on_select)
root.mainloop()

# lat and lon of Ljubljana
# 46.056946
# 14.505751
