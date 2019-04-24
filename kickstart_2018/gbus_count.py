#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

T = int(input())
for i in range(1, T + 1):
    GBuses = int(input())
    GBusRangesInput = input().split(" ")
    GBusRanges = []
    for j in range(GBuses):
        startRange = int(GBusRangesInput.pop(0))
        endRange = int(GBusRangesInput.pop(0))
        GBusRanges.append(range(startRange, endRange+1))
    CitiesNum = int(input())
    Cities = []
    for k in range(CitiesNum):
        Cities.append(int(input()))
    # print("test {0}: cities {1}".format(i, Cities))
    Results = []
    for city in Cities:
        citycount = 0
        for gbusrange in GBusRanges:
            if city in gbusrange:
                citycount = citycount + 1
        Results.append(str(citycount))
    print("Case #{case}: {answer}".format(case=i, answer=" ".join(Results)))
    input()
