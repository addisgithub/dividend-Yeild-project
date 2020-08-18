import scrape


def threshold():
    dividends = []
    for stock in scrape.arrange():
        if stock.Yield >= 3:
            dividends.append(stock)
    return dividends
    
def main():

    req_dividends = threshold()
    for i in req_dividends:
        print(i.symbol + "\t\t" + str(i.Yield))

if __name__ == "__main__":
    main()