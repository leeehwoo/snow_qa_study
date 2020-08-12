#Q2) 필터 ID를 받아서 필터 NAME을 리턴하는 함수를 만들어보자
import requests, json 
 
 
def getKajiFilterJson():
    apiUrl = "http://qa-api.b612kaji.com/v1/filter/overview"
    headers = {
        'User-Agent': 'iphoneapp.b612cn/9.1.0 (iPhone; U; CPU iOS 13_1_3 like Mac OS X; ko-KR-KR; occ-KR "iPhone X" )'
    }
    response = requests.get(apiUrl, headers = headers)
 
    return json.loads(response.text)
 
def getFilterName(filterJson, filterId):
    filters = filterJson["result"]["filters"]
     
    i = 0
    for a in filters:
        a = filters [i]
         
        if a['id'] == filterId:
            b = a['name']
            return b
            break
        
        else:
            i = i + 1
 
 
filterJson = getKajiFilterJson()
filterName = getFilterName(filterJson, 300324)
print (filterName)