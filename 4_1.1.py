#Q1) 03-03. PYTHON+API 활용 연습 2 까지 작성한 코드에서 API CALL 부분을 함수로 만들어보자.
import requests, json
   
 
 
def getKajiFilterJson():
    apiUrl = "http://qa-api.b612kaji.com/v1/filter/overview"
    headers = {
        'User-Agent': 'iphoneapp.b612cn/9.1.0 (iPhone; U; CPU iOS 13_1_3 like Mac OS X; ko-KR-KR; occ-KR "iPhone X" )'
    }
    response = requests.get(apiUrl, headers = headers)
    filterOverview = json.loads(response.text)
 
    return filterOverview
 
 
filterJson = getKajiFilterJson()