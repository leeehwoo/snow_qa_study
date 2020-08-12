#b612 kaji(beta) 필터 리스트 API 를 호출하고, 결과를 출력하는 코드
import requests, json, urllib.request
   
apiUrl = "http://qa-api.b612kaji.com/v1/filter/overview"
headers = {
    'User-Agent': 'iphoneapp.b612cn/9.1.0 (iPhone; U; CPU iOS 13_1_3 like Mac OS X; ko-KR-KR; occ-KR "iPhone X" )'
}
response = requests.get(apiUrl, headers = headers)
filterOverview = json.loads(response.text)
 
 
filters = filterOverview["result"]["filters"]
 
i = 0
for a in filters:
 
    if "type" in a:
         print(fileName)
 
    else:
        fileName = a['thumbnail']
        imageUrl = "http://qa.b612kaji.com/cdn/specialFilter/" + str(a['id']) + "/" + a['thumbnail']
        urllib.request.urlretrieve(imageUrl, fileName)
        print(fileName)
    i = i + 1