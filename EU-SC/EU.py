# define and export a function called load data that will get a city and the chemical and starting date and ending date and will return a list of the data

def load_data(self, city, chem, start_date, end_date):
    # get the data from the csv file
    df = pd.read_csv('data.csv')
    # filter the data by city, chemical, and date
    df = df[(df['City'] == city) & (df['Chemical'] == chem) & (df['Date'] >= start_date) & (df['Date'] <= end_date)]
    # get the data for the chemical
    data = df[chem].tolist()
    # get the dates
    dates = df['Date'].tolist()
    # return the data and dates
    return data, dates