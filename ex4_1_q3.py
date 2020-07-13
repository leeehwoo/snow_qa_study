import requests, json

def getKajiFilterJson():
    apiUrl = "http://qa-api.b612kaji.com/v1/filter/overview"
    headers = {
        'User-Agent': 'iphoneapp.b612cn/9.1.0 (iPhone; U; CPU iOS 13_1_3 like Mac OS X; kr-KR-KR; occ-KR "iPhone X" )'}
    response = requests.get(apiUrl, headers=headers)
    filterOverview = json.loads(response.text)
    return filterOverview

def getFilterName(filterJson, filterId):
    filterResult = filterJson['result']['filters']
    filtersCount = 0
    for filterInfo in filterResult:
        allFilterID = str(filterResult[filtersCount]['id'])
        if allFilterID == filterId:
            allFilterName = filterResult[filtersCount]['name']
            return allFilterName
        filtersCount = filtersCount +1
    return None

def printFilterName(filterJson, *args):
    for filterFor in args:
        print(getFilterName(filterJson, filterFor))

filterJson = getKajiFilterJson()
printFilterName(filterJson, "300299", "300171", "300252")