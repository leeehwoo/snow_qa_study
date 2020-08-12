
#b612 kaji(beta) 필터 리스트 API 를 호출하고, 결과를 출력하는 코드
import requests, json
   
apiUrl = "http://qa-api.b612kaji.com/v1/filter/overview"
headers = {
    'User-Agent': 'iphoneapp.b612cn/9.1.0 (iPhone; U; CPU iOS 13_1_3 like Mac OS X; ko-KR-KR; occ-KR "iPhone X" )'
}
response = requests.get(apiUrl, headers = headers)
filterOverview = json.loads(response.text)
 
 
#filters[] 내부 필터들 중에서, type == "BUILT_IN" 에 해당하는 필터들의 id & name 을 출력해보자.
filters = filterOverview["result"]["filters"]
 
i = 0
for a in filters:
    a = filters[i]
 
    try :
        if a['type'] == "BUILT_IN":
            print(a['name'],"(id:",a['id'],")")
            i = i + 1
    except KeyError :
        i = i + 1