class Stock:
    def __init__(self, name, high, low, date):
        self.name = name
        self.high = high
        self.low = low
        self.date = date

def remove(stonks):

    temp = []
    temp = stonks
    temp_high = getTopstock(temp)
    temp.remove(temp_high)
    temp_low = getlasthighstock(temp)
    temp.remove(temp_low)
    total = sum(x.high for x in temp)
    avg = total / len(temp)
    return avg


def getTopstock(stonks):

    highest = stonks[0]
    for i in stonks:
        if i.high > highest.high:
            highest = i
    return highest
def getlasthighstock(stonks):

    lowest = stonks[0]
    for i in stonks:
        if i.high < lowest.high:
            lowest = i
    return lowest

def getlowstock(stonks):

    highest = stonks[0]
    for i in stonks:
        if i.low < highest.low:
            highest = i
    return highest

def median(stonks):

    assemble = sorted(stonks, key=lambda x: x.high, reverse=True)
    if len(assemble) % 2 == 0:
        ans = (assemble[int(len(assemble) / 2)].high + assemble[int(len(assemble) / 2) - 1].high) / 2
        return ans
    elif len(assemble) % 2 == 1:
        ans_2 = len(assemble) / 2
        return ans_2

def main():

    stonks = []
    stonks.append(Stock("appl", 534, 220, "02-20-2020"))
    stonks.append(Stock("tsla", 543, 42, "02-20-2020"))
    stonks.append(Stock("v", 565, 96, "02-20-2020"))
    stonks.append(Stock("brhk", 5536, 963, "02-20-2020"))
    stonks.append(Stock("nio", 5350, 3560, "02-20-2020"))
    stonks.append(Stock("amzn", 3560, 780, "02-20-2020"))
    stonks.append(Stock("boa", 4200, 660, "02-20-2020"))
    stonks.append(Stock("co", 570, 70, "02-20-2020"))
    stonks.append(Stock("mst", 230, 60, "02-20-2020"))
    stonks.append(Stock("gh", 540, 40, "02-20-2020"))


    #print(getTopstock(stonks).name)
    #print(median(stonks))
    print(remove(stonks))
    #print(getlasthighstock(stonks).name)




if __name__ == "__main__":
    main()
