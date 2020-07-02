import requests, json
import pprint

apiUrl = "http://qa-api.b612kaji.com/v1/filter/overview"
headers = {'User-Agent': 'iphoneapp.b612cn/9.1.0 (iPhone; U; CPU iOS 13_1_3 like Mac OS X; kr-KR-KR; occ-KR "iPhone X" )'}
#headers = {'User-Agent': 'iphoneapp.b612cn/9.1.0 (iPhone; U; CPU iOS 13_1_3 like Mac OS X; cn-CN-CN; occ-CN "iPhone X" )'}
response = requests.get(apiUrl, headers=headers)
filterOverview = json.loads(response.text)

filters = filterOverview["result"]["filters"]
#pprint.pprint(filters)
#typeSearch = filters[9]["type"]
#print(typeSearch)
filtersCount = 0
for filtersInfo in filters:
    #filterType = filters[filtersCount]["type"]
    filterType = filters[filtersCount]
    filterId = filters[filtersCount]["id"]
    filterName = filters[filtersCount]["name"]
    if "type" in filterType:
        #print('Id : %s, Name : %s, Type : %s' % (filterId, filterName, filterType))
        print('Id : %s, Name : %s' % (filterId, filterName))
    else:
        #print("pass : %d" %filtersCount)
        pass
    filtersCount = filtersCount +1
