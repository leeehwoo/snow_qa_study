#Q1) API result → filters[] 내부 필터들의 id & name 을 모두 출력해보자
import requests, json
   
apiUrl = "http://qa-api.b612kaji.com/v1/filter/overview"
headers = {
 'User-Agent': 'iphoneapp.b612cn/9.1.0 (iPhone; U; CPU iOS 13_1_3 like Mac OS X; ko-KR-KR; occ-KR "iPhone X" )'
}
response = requests.get(apiUrl, headers = headers)
filterOverview = json.loads(response.text)
 
 
 
filters = filterOverview["result"]["filters"]
 
i = 0
for a in filters:
    a = filters[i]
    print("(id = ",a['id'],")")
    i = i + 1