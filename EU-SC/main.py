import tkinter as tk
from tkinter import ttk
import pandas as pd
import subprocess
import matplotlib.pyplot as plt
from datetime import datetime

# import get_data_from_sc from ./SC/SC.py
from SC.SC import get_data_from_sc
#import get_data_from_eu from ./EU/EU.py
from EU.EU import get_data_from_eu

class CityPlotter(tk.Tk):
    def load_data(self):
        # Read in city data from csv file
        self.city_data = pd.read_csv('cities.csv', encoding='utf-8')
        self.cities = []
        for city in self.city_data['City']:
            self.cities.append(city)

        # load all the chemicals into chemicals list
        self.chemicals = []
        with open('chems.txt', 'r') as file:
            for line in file:
                self.chemicals.append(line.strip())

    def __init__(self):
        self.load_data()
        super().__init__()

        # Set the window title
        self.title('City Plotter')
        # make the app 500 x 500 large
        self.geometry('500x500')

        # Create a label and entry for the city name
        city_label = ttk.Label(self, text='City Name:')
        city_label.grid(row=0, column=0)
        # create a dropdown with cities
        self.city_entry = ttk.Combobox(self, values=self.cities)
        self.city_entry.grid(row=0, column=1)
        # make the default value Berlin
        self.city_entry.current(
            self.cities.index('Berlin')
        )
        # listen to changes in dropdown and call on_city_change when that happens
        self.city_entry.bind('<<ComboboxSelected>>', self.on_city_change)

        # create a drop down that contains all the chemicals but deafults to PM10
        chem_label = ttk.Label(self, text='Chemical:')
        chem_label.grid(row=0, column=3)
        self.chem_entry = ttk.Combobox(self, values=self.chemicals)
        self.chem_entry.grid(row=0, column=4)
        self.chem_entry.current(
            self.chemicals.index('PM10')
        )

        # Add a long and lat text fields beneath but I do not want the user to be able to edit them
        long_label = ttk.Label(self, text='Longitude:')
        long_label.grid(row=1, column=0)
        self.long_entry = ttk.Entry(self)
        self.long_entry.grid(row=1, column=1)

        lat_label = ttk.Label(self, text='Latitude:')
        lat_label.grid(row=1, column=3)
        self.lat_entry = ttk.Entry(self)
        self.lat_entry.grid(row=1, column=4)

        self.on_city_change(event=None)

        # Add starting and ending dates (wihout days)
        start_label = ttk.Label(self, text='Start Date:')
        start_label.grid(row=2, column=0)
        self.start_entry = ttk.Entry(self)
        self.start_entry.grid(row=2, column=1)

        end_label = ttk.Label(self, text='End Date:')
        end_label.grid(row=2, column=3)
        self.end_entry = ttk.Entry(self)
        self.end_entry.grid(row=2, column=4)

        # Default those two to 2021-01 and 2022-01
        self.start_entry.insert(0, '2021-01')
        self.end_entry.insert(0, '2021-12')

        # Create a button to plot the data and put it on its own row
        plot_button = ttk.Button(
            self, text='Plot Data', command=self.plot_data)
        plot_button.grid(row=3, column=2, columnspan=2)

        # Create a matplotlib figure and axis
        self.fig, self.ax = plt.subplots()

    def plot_data(self):
        # self.sc_data = get_data_from_sc(
        #     self.city_entry.get(),
        #     self.lat_entry.get(),
        #     self.long_entry.get(),
        #     self.start_entry.get(),
        #     self.end_entry.get(),
        #     15,
        #     self.chem_entry.get()
        # )

        # self.eu_data  = get_data_from_eu(
        #     self.city_entry.get(),
        #     'DE',
        #     self.start_entry.get()[:4],
        #     self.end_entry.get()[:4],
        #     self.chem_entry.get()
        # )


        # # save the data into two files that will be losless 
        # with open('sc_data.txt', 'w') as file:
        #     file.write(str(self.sc_data))
        # with open('eu_data.txt', 'w') as file:
        #     file.write(str(self.eu_data))

        with open('sc_data.txt', 'r') as file:
            self.sc_data = file.read()
        with open('eu_data.txt', 'r') as file:
            self.eu_data = file.read()

        # convert the strings into lists
        self.sc_data = eval(self.sc_data)
        self.eu_data = eval(self.eu_data)


        print (self.eu_data)
        print (self.sc_data)
        # loop though the list of pairs and print them out
        for (x, y) in self.eu_data:
            print (x, y)
        
        er_y = [y for x, y in self.eu_data]
        er_x = [datetime.strptime(x, '%Y-%m') for x, y in self.eu_data]
        sc_y = [y for x, y in self.sc_data]
        sc_x = [datetime.strptime(x, '%Y-%m') for x, y in self.sc_data]


        plt.plot_date(er_x, er_y, color='red', label='ER Data', fmt='-')
        plt.plot_date(sc_x, sc_y, color='blue', label='SC Data', fmt='-')
        plt.legend()
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title('ER and SC Data Comparison')
        plt.show()

        return 
    # Get the city name from the entry
        city_name = self.city_entry.get()

        # Look up the lat and long for the city
        city = city_data[city_data['City'] == city_name].iloc[0]
        lat, lon = city['Latitude'], city['Longitude']

        # Call the SC.py script with the lat and long as arguments
        sc_output = subprocess.check_output(
            ['python', 'SC.py', str(lat), str(lon)])

        # Call the EU.py script with the lat and long as arguments
        eu_output = subprocess.check_output(
            ['python', 'EU.py', str(lat), str(lon)])

        # Parse the output of the scripts to get the data
        sc_data = [float(x) for x in sc_output.decode('utf-8').split()]
        eu_data = [float(x) for x in eu_output.decode('utf-8').split()]

        # Plot the data on the axis
        self.ax.clear()
        self.ax.plot(sc_data, label='SC')
        self.ax.plot(eu_data, label='EU')
        self.ax.legend()
        self.ax.set_title(city_name)
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Temperature')
        self.fig.canvas.draw() 


    #  turn off the app when the window is closed
    def destroy(self):
        self.quit()
        self.master.destroy()

    # Run a function when the value of the dropbox has changed
    def on_city_change(self, event):
        print(self.city_entry.get())

        # get the city, find its lat and long and put them in the text fields
        city = self.city_data[self.city_data['City']
                              == self.city_entry.get()].iloc[0]
        print(city)
        print(city['Latitude'])
        print(city['Longitude'])
        self.lat_entry.delete(0, tk.END)
        self.lat_entry.insert(0, city['Latitude'])
        self.long_entry.delete(0, tk.END)
        self.long_entry.insert(0, city['Longitude'])


# Run the GUI
if __name__ == '__main__':
    app = CityPlotter()
    app.mainloop()
