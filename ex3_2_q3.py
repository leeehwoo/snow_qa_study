import requests, json
import pprint

apiUrl = "http://qa-api.b612kaji.com/v1/filter/overview"
headers = {'User-Agent': 'iphoneapp.b612cn/9.1.0 (iPhone; U; CPU iOS 13_1_3 like Mac OS X; kr-KR-KR; occ-KR "iPhone X" )'}
response = requests.get(apiUrl, headers=headers)
filterOverview = json.loads(response.text)

filters = filterOverview["result"]["filters"]
filtersCount = 0
for filtersInfo in filters:
    filterType = filters[filtersCount]
    filterId = filters[filtersCount]["id"]
    filterName = filters[filtersCount]["name"]
    if "type" in filterType:
        print('Id : %s, Name : %s' % (filterId, filterName))
    else:
        pass
    filtersCount = filtersCount +1
