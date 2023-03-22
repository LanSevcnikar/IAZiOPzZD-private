import tkinter as tk


class DataGUI:
    def __init__(self, master):
        self.master = master
        master.title("Data Sources")

        self.label = tk.Label(master, text="Select a data source:")
        self.label.pack()

        self.sources = ["1: Dejavniki tveganja, Slovenija, letno", "2: Preventiva, Slovenija, letno",
                        "3: Zdravstveno stanje, Slovenija, letno", "4: Umrljivost, Slovenija, letno"]
        self.selected_source = tk.StringVar(master)
        self.selected_source.set(self.sources[0])

        self.source_menu = tk.OptionMenu(
            master, self.selected_source, *self.sources)
        self.source_menu.pack()

        self.types_button = tk.Button(
            master, text="Display Data Types", command=self.display_data_types)
        self.types_button.pack()

        self.query_button = tk.Button(
            master, text="Query Data", command=self.query_data)
        self.query_button.pack()

        self.learn_button = tk.Button(
            master, text="Learn More", command=self.learn_more)
        self.learn_button.pack()

    def display_data_types(self):
        source = self.selected_source.get()
        # code to display the data types for the selected source

    def query_data(self):
        source = self.selected_source.get()
        # code to allow the user to query data for the selected source

    def learn_more(self):
        source = self.selected_source.get()
        # code to display more information about the selected source


root = tk.Tk()
my_gui = DataGUI(root)
root.mainloop()
