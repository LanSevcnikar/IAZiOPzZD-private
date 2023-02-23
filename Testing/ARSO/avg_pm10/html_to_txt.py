from bs4 import BeautifulSoup


def get_2013():
    #load the html file data_html/PM10_D_dec13_slo.html
    with open('data_html/PM10_D_dec13_slo.html', 'r', encoding='utf-8') as f:
        html = f.read()
        #parse the html file
        soup = BeautifulSoup(html, 'html.parser')
        #find the element with the class='pc pc1 w0 h0 opened'
        bigConglomerate = soup.find('div', {'class': 'pc pc1 w0 h0 opened'})
        #loop through all child elements of bigConglomerate
        for child in bigConglomerate.children:
            
        
