from bs4 import BeautifulSoup
import requests
from yahoo_finance import Share
r = requests.get("https://api.scrapingdog.com/scrape?api_key=5f19a05ed72b6a7122abe7d0&url=https://www.slickcharts.com/sp500").text

response = BeautifulSoup(r, 'html.parser')

data = response.find_all("tbody")
#print(data)
try:
    table1 = data[0].find_all("tr")
except:
    table1 = None


l = {}
#print(table1)
u = list()


class Row():
    def __init__(self):
        self.Position = ""
        self.Company = ""
        self.Symbol = ""
        self.Weight = ""
        self.Price = ""
        self.Change = ""
        self.PercentChange = ""


listOfStonks = []

for tr in table1:
    rows = tr.find_all("td")
    
    index = 0
    s = Row()
    for r in rows:
        if (index == 0):
            s.Position = r.text
        elif (index == 1):
            s.Company = r.text
        elif (index == 2):
            s.Symbol = r.text
        elif (index == 3):
            s.Weight = r.text
        elif (index == 4):
            s.Price = r.text
        elif (index == 5):
            s.Change = r.text
        elif (index == 6):
            s.PercentChange = r.text
        
        index += 1
        #print("index:", index)
        if (index > 6):
            listOfStonks.append(s)
        
        #print(r.text)

for stock in listOfStonks:
    #print(stock.Symbol)
    #print(stock.Price)

    #yahoo = Share(stock.Symbol)

    print(yahoo.get_price)

'''
for i in range(0,len(table1)):
    try:
        table1_td = table1[i].find_all("tr")
    except:
        table1_td = None

    l[table1_td[0].text] = table1_td[1].text
    
    u.append(1)
    l = {}

    #print(l)
'''