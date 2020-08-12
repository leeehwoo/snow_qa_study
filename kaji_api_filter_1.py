import requests, json, pprint
  
apiUrl = "http://qa-api.b612kaji.com/v1/filter/overview"
headers = {
    'User-Agent': 'iphoneapp.b612cn/9.1.0 (iPhone; U; CPU iOS 13_1_3 like Mac OS X; ko-KR-KR; occ-KR "iPhone X" )'
}


response = requests.get(apiUrl, headers = headers)
resultJson = json.loads(response.text)


result = resultJson['result']
filters = result['filters']


for a in filters('filters'):
    pprint(name['name'])


