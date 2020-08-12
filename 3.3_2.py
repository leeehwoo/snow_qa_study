#b612 kaji(beta) 필터 리스트 API 를 호출하고, 결과를 출력하는 코드
import requests, json
   
apiUrl = "http://qa-api.b612kaji.com/v1/filter/overview"
headers = {
    'User-Agent': 'iphoneapp.b612cn/9.1.0 (iPhone; U; CPU iOS 13_1_3 like Mac OS X; ko-KR-KR; occ-KR "iPhone X" )'
}
response = requests.get(apiUrl, headers = headers)
filterOverview = json.loads(response.text)
 
 
#groups[] 내부의 그룹의 id, name과 그룹에 속한 filtersIds를 모두 출력해보자.
filterGroup = filterOverview["result"]["groups"]
 
i = 0
for a in filterGroup:
    a = filterGroup[i]
    print("Group Name : ", a['name'],"(id=",a['id'],")")
    print(a['filterIds'])
    i = i + 1