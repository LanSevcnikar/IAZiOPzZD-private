years = [
    2013,
    2014,
    2015,
    2016,
    2017,
    2018,
    2019,
    2020,
    2021,
    2022,
]


def analyze_data(data):
    analyzed_data = {}
    dict = {}
    for line_index in range(len(data)):
        if(data[line_index] == ""):
            continue
        if('0' <= data[line_index][0] <= '9'):
            split_line = data[line_index].split(" ")
            for i in range(len(split_line)):
                analyzed_data[dict[i]] = split_line[i]
        else:
            row_index = 0
            while(line_index < len(data) and 
                  data[line_index] != "" and 
                  not ('0' <= data[line_index][0] <= '9')):
                dict[row_index] = data[line_index]
                row_index += 1
                line_index += 1
    print(dict)
    return analyzed_data


for year in years:
    data = []
    with open(f"data_txt/{year}.txt", "r", encoding="utf-8") as f:
        data = f.read()
        data = data.split("\n")
    analyzed_data = analyze_data(data)
    print(analyzed_data)
    break
