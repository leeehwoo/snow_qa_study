#Q3) 필터 ID를 여러개 받아서 모두 출력하는 함수를 만들어보자.
import requests, json 
 
 
def getKajiFilterJson():
    apiUrl = "http://qa-api.b612kaji.com/v1/filter/overview"
    headers = {
        'User-Agent': 'iphoneapp.b612cn/9.1.0 (iPhone; U; CPU iOS 13_1_3 like Mac OS X; ko-KR-KR; occ-KR "iPhone X" )'
    }
    response = requests.get(apiUrl, headers = headers)
 
    return json.loads(response.text)
     
def printFilterName(filterJson, *args):
    #... getFilterName(filterJson, filterId) 를 사용한 code 작성 ...
    filters = filterJson["result"]["filters"]
    
    i = 0
     
    for a in filters:
        a = filters[i]
        id = a['id']
        name = a['name']
        if id in args:
            print(name)
 
        i = i + 1
 
filterJson = getKajiFilterJson()
printFilterName(filterJson, 300299, 300171, 300252)