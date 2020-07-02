import requests, json
import pprint

apiUrl = "http://qa-api.b612kaji.com/v1/filter/overview"
headers = {'User-Agent': 'iphoneapp.b612cn/9.1.0 (iPhone; U; CPU iOS 13_1_3 like Mac OS X; kr-KR-KR; occ-KR "iPhone X" )'}
response = requests.get(apiUrl, headers=headers)
filterOverview = json.loads(response.text)

filters = filterOverview["result"]["filters"]
filtersCount = 0

for filtersInfo in filters:
    filtersId = filters[filtersCount]["id"]
    filtersThumbnail = filters[filtersCount]["thumbnail"]
    #filtersCount = filtersCount + 1
    print('Id : %d, Thumbnail : %s' % (filtersId, filtersThumbnail))
    thumbnailUrl  = "http://qa.b612kaji.com/cdn/specialFilter/%s/%s" %(filtersId, filtersThumbnail)
    print(thumbnailUrl)
    filtersCount = filtersCount + 1
