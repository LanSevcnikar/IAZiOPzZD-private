import csv
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from bs4 import BeautifulSoup
import pandas as pd
import requests


class WeatherGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Weather Data Downloader")
        self.create_widgets()

    def create_widgets(self):
        # Create labels and entry fields for start and end dates
        self.start_date_label = tk.Label(
            self.master, text="Start Date (yyyy-mm-dd):")
        self.start_date_label.grid(row=0, column=0, padx=10, pady=10)
        self.start_date_entry = tk.Entry(self.master)
        self.start_date_entry.grid(row=0, column=1, padx=10, pady=10)
        self.start_date_entry.insert(0, "2022-12-01")

        self.end_date_label = tk.Label(
            self.master, text="End Date (yyyy-mm-dd):")
        self.end_date_label.grid(row=1, column=0, padx=10, pady=10)
        self.end_date_entry = tk.Entry(self.master)
        self.end_date_entry.grid(row=1, column=1, padx=10, pady=10)
        self.end_date_entry.insert(0, "2022-12-03")

        # Create checkboxes for station selection
        self.station_frame = ttk.Frame(self.master)
        self.station_frame.grid(
            row=2, column=0, columnspan=2, padx=10, pady=10)
        self.station_vars = []
        self.station_names = ["1 - Bežigrad, Ljubljana",
                              "3 - Križišče Vošnjakove u. in Tivolske c., Lj"]
        for i, name in enumerate(self.station_names):
            var = tk.IntVar(value=1)
            cb = ttk.Checkbutton(self.station_frame, text=name, variable=var)
            cb.grid(row=i, column=0, sticky="w")
            self.station_vars.append(var)

        # Create download button
        self.download_button = tk.Button(
            self.master, text="Download", command=self.download_data)
        self.download_button.grid(
            row=3, column=0, columnspan=2, padx=10, pady=10)

    def download_data(self):
        # Get start and end dates from entry fields
        start_date_str = self.start_date_entry.get()
        end_date_str = self.end_date_entry.get()

        # get the selected stations
        selected_stations = []
        for i, var in enumerate(self.station_vars):
            if var.get() == 1:
                selected_stations.append(self.station_names[i].split(" ")[0])

        # loop through all the dates between start and end date
        # and download data for each date
        for date_full in pd.date_range(start_date_str, end_date_str):
            
            # make date_str of format d.m.yyyy
            date_str = date_full.strftime("%d.%m.%Y")

            for selected_station in selected_stations:
                self.download_data_date(selected_station, date_str)

    def download_data_date(self, station, date):
        print(f"Downloading data for station {station} on {date}")
        url = f"https://www.ljubljana.si/sl/moja-ljubljana/varstvo-okolja/stanje-okolja/kakovost-zraka/?Date={date}&AirMonitoringPointID={station}"
        print(url)

        # Download the data
        response = requests.get(url)
        if response.status_code != 200:
            messagebox.showerror("Error", f"Error downloading data from {url}")
            return

        # create a BeautifulSoup object from the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # find the table element in the HTML using its class name or ID
        table_parent = soup.find('div', {'class': 'data-table'})
        table = table_parent.find('table')

        if(station == "1"):
            file_name = f"./Bezigrad, Ljubljana/{date}.csv"
        else:
            file_name = f"./Krizisce Vosnjakove u. in Tivolske c., Lj/{date}.csv"

        # create a CSV file to save the table data
        with open(file_name, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)

            # loop through each row in the table
            for row in table.find_all('tr'):

                # get the cells in the row as a list
                cells = [cell.get_text(strip=True)
                        for cell in row.find_all(['th', 'td'])]

                # write the cells to the CSV file
                writer.writerow(cells)

        # print a message to confirm that the table has been saved as a CSV file
        print('Table has been saved as table.csv')


def main():
    root = tk.Tk()
    app = WeatherGUI(master=root)
    app.mainloop()


if __name__ == '__main__':
    main()
