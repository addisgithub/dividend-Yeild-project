from bs4 import BeautifulSoup
import requests

class Row():
    def __init__(self):
        self.symbol = ""
        self.name = ""
        self.price = ""
        self.Price_to_earnings = ""
        self.Price_to_earnings_nxt_yr = ""
        self.Div_per_share = ""
        self.Yield = ""
        self.EPS = ""


def arrange():
    r = requests.get("https://api.scrapingdog.com/scrape?api_key=5f19a05ed72b6a7122abe7d0&url=https://www.retirebeforedad.com/dividend-aristocrats/").text

    response = BeautifulSoup(r, 'html.parser')

    data = response.find_all("tbody")

    try:
        table1 = data[0].find_all("tr")
    except:
        table1 = None
    listOfStonks = []
    
    for tr in table1:
        rows = tr.find_all("td")
        #[XOM,Exxon Mobil,$43.43,16.30,27.49,3.48,8.01%,1.58,-25.74,1.01,-4.90%,16]
        index = 0
        s = Row()
        for r in rows:
            if (index == 0):
                s.symbol = r.text
            elif (index == 1):
                s.name = r.text
            elif (index == 2):
                s.price = r.text
            elif (index == 3):
                s.Price_to_earnings = r.text
            elif (index == 4):
                s.Price_to_earnings_nxt_yr = r.text
            elif (index == 5):
                s.Div_per_share = r.text
            elif (index == 6):
                #print(r.text[:-1])
                if (r.text[:-1].isnumeric() or r.text[:-1].strip() == ""):
                    s.Yield = 0.00
                else:
                    s.Yield = float(r.text[:-1])
                #print(len(listOfStonks))
                #print("Yield: " + s.Yield)
            elif (index == 7):
                s.EPS = r.text
            
            
            index += 1
            #print("index:", index)
            if (index > 7):
                listOfStonks.append(s)
                break
            
    return listOfStonks

#listOfStonks = []
#for stock in listOfStonks:
    #print(stock.symbol)
    #print(stock.price)
    #print(stock.Yield)###
    #print(len(listOfStonks))