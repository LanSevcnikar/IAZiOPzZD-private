import pandas as pd


# extract all city codes from input file
# input_file_1 = 'C:/Users/sevcn/Documents/programming/projects/IAZiOPzZD-private/GermanyPoC/EuropeAirPortal/DataExtract.csv'

# df = pd.read_csv(input_file_1, sep=',', encoding='utf-8')

# cities = df['City'].unique()
# # strip each
# cities = [str(city).strip() for city in cities]
# cities.sort()
# print(cities)

cities1 = ['Aachen', 'Augsburg', 'Bamberg', 'Bayreuth', 'Berlin', 'Bielefeld', 'Bochum', 'Bonn', 'Bottrop', 'Brandenburg an der Havel', 'Braunschweig', 'Bremen', 'Bremerhaven', 'Chemnitz', 'Cottbus', 'Darmstadt', 'Dessau-Roßlau', 'Dortmund', 'Dresden', 'Duisburg', 'Düsseldorf', 'Erfurt', 'Essen', 'Esslingen am Neckar', 'Flensburg', 'Frankfurt (Oder)', 'Frankfurt am Main', 'Freiburg im Breisgau', 'Friedrichshafen', 'Fulda', 'Fürth', 'Gelsenkirchen', 'Gera', 'Gießen', 'Görlitz', 'Göttingen', 'Hagen', 'Halle an der Saale', 'Hamburg', 'Hanau', 'Hannover', 'Heidelberg', 'Heilbronn', 'Herne', 'Hildesheim', 'Ingolstadt', 'Jena', 'Kaiserslautern', 'Karlsruhe', 'Kassel', 'Kiel', 'Koblenz', 'Konstanz', 'Krefeld',
           'Köln', 'Landshut', 'Leipzig', 'Leverkusen', 'Ludwigsburg', 'Ludwigshafen am Rhein', 'Lübeck', 'Lüneburg', 'Magdeburg', 'Mainz', 'Mannheim', 'Marburg', 'Mönchengladbach', 'Mülheim a.d.Ruhr', 'München', 'Münster', 'Neu-Ulm', 'Neubrandenburg', 'Neuss', 'Nürnberg', 'Oberhausen', 'Offenbach am Main', 'Oldenburg (Oldenburg)', 'Osnabrück', 'Passau', 'Pforzheim', 'Plauen', 'Potsdam', 'Recklinghausen', 'Regensburg', 'Reutlingen', 'Rostock', 'Saarbrücken', 'Salzgitter', 'Schweinfurt', 'Schwerin', 'Solingen', 'Speyer', 'Stralsund', 'Stuttgart', 'Trier', 'Tübingen', 'Ulm', 'Villingen-Schwenningen', 'Weimar', 'Wetzlar', 'Wiesbaden', 'Wilhelmshaven', 'Witten', 'Wolfsburg', 'Wuppertal', 'Würzburg', 'Zwickau', 'nan']
cities2 = ["Arnsberg", "Baden-Württemberg", "Bayern", "Berlin", "Brandenburg", "Braunschweig", "Bremen", "Chemnitz", "Darmstadt", "Detmold", "Dresden", "Düsseldorf", "Freiburg", "Germany (until 1990 former territory of the FRG)", "Gießen", "Hamburg", "Hannover", "Hessen", "Karlsruhe", "Kassel", "Koblenz", "Köln", "Leipzig", "Lüneburg",
           "Mecklenburg-Vorpommern", "Mittelfranken", "Münster", "Niederbayern", "Niedersachsen", "Nordrhein-Westfalen", "Oberbayern", "Oberfranken", "Oberpfalz", "Rheinhessen-Pfalz", "Rheinland-Pfalz", "Saarland", "Sachsen", "Sachsen-Anhalt", "Schleswig-Holstein", "Schwaben", "Stuttgart", "Thüringen", "Trier", "Tübingen", "Unterfranken", "Weser-Ems", ]


common_cities = list(set(cities1) & set(cities2))
common_cities.sort()


input_file = 'C:/Users/sevcn/Documents/programming/projects/IAZiOPzZD-private/EU-SC/cities.csv'
output_file = 'C:/Users/sevcn/Documents/programming/projects/IAZiOPzZD-private/GermanyPoC/EuropeAirPortal/cities.csv'

df = pd.read_csv(input_file, sep=',', encoding='utf-8')

with open(output_file, 'a', encoding='utf-8') as f:
    f.write('City,Latitude,Longitude\n')
    # for each city in the common cities var find its lat and long and print all
    for city in common_cities:
        try:
            city_df = df[df['City'] == city]
            str_city = str(city)
            str_lat = str(city_df['Latitude'].values[0])
            str_long = str(city_df['Longitude'].values[0])
            f.write(str_city + ',' + str_lat + ',' + str_long + '\n')

        except:
            print('error')