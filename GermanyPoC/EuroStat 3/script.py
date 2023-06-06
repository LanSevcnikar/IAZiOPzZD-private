# read all the data in area3.txt
# first split by the new line and then split by space
# join all the middle values together
# then sort by last value
# output as csv file 

import csv

def get_area():
    with open('area3.txt', 'r', encoding='utf-8') as f:
        data = f.read()
        data = data.split('\n')
        data = [i.split('	') for i in data]
        # remove data that does not have an int as the last value
        data = [[*i[:-1],i[-1].replace(".","")] for i in data]
        data = [i for i in data if i[-1].isdigit()]
        data = [(i[0],' '.join(i[1:-1]),i[-1]) for i in data]
        # sort
        data = sorted(data, key=lambda x: float(x[-1]))
        
        # write to csv
        with open('area3.csv', 'w', encoding='utf-8') as f2:
            for i in data:
                f2.write(';'.join(i)+'\n')

        return data

def get_population():
    with open('population2.txt', 'r', encoding='utf-8') as f:
        data = f.read()
        data = data.split('\n')
        data = [i.split('	') for i in data]
        # remove data that does not have an int as the last value
        data = [[*i[:-1],i[-1].replace(".","")] for i in data]
        data = [i for i in data if i[-1].isdigit()]
        data = [(i[0],' '.join(i[1:-1]),i[-1]) for i in data]
        print(data)
        # sort
        data = sorted(data, key=lambda x: float(x[-1]))
        
        # write to csv
        with open('population2.csv', 'w', encoding='utf-8') as f2:
            for i in data:
                f2.write(';'.join(i)+'\n')

        return data
    
area = get_area()
population = get_population()

print(population[:10])

# join together by the first value
data = []
for i in area:
    for j in population:
        if i[0] == j[0]:
            data.append([*i,j[2]])

# sort by last value
data = sorted(data, key=lambda x: float(x[-1]))
# remove all of those that are the same in the second value
data = [i for i in data if i[1] != data[0][1]]

# remove all data where the value before last is more than 1000
data = [i for i in data if int(i[-2]) < 10000]
# remove all data where the last value is more than 4000000
data = [i for i in data if int(i[-1]) < 5000000]

# write to csv
with open('data.csv', 'w', encoding='utf-8') as f2:
    for i in data:
        f2.write(';'.join(i)+'\n')