import os
import PyPDF2

years = [
    '2013', 
    '2014',
    '2015',
    '2016',
    '2017',
    '2018',
    '2019',
    '2020',
    '2021',
    '2022'
]

#check if there exists a folder called dat_txt, if not create it
if not os.path.exists('./data_txt'):
    os.makedirs('./data_txt')

for year in years:
    # if the folder data_txt/{year} does not exist, create it
    if not os.path.exists(f"./data_txt/{year}"):
        os.makedirs(f"./data_txt/{year}")
        
    #delete all files in folder data_txt/{year}
    for filename in os.listdir(f'./data_txt/{year}'):
        os.remove(f"./data_txt/{year}/{filename}")

    pdf_file = open(f'data_raw/PM10_D_dec{year[2:]}_slo.pdf','rb')
    pdf_reader=PyPDF2.PdfReader(pdf_file)
    
    number_of_pages = len(pdf_reader.pages)

    for page in range(number_of_pages):
        page_object = pdf_reader.pages[page]
        text = page_object.extract_text()
        #page str should have leading zeros
        file = open(f"./data_txt/{year}/MP10_{year}_Page_{page+1:02d}.txt","a", encoding='utf-8')
        file.writelines(text)