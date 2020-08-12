import requests, json, pprint

apiUrl = "http://qa-api.b612kaji.com/v1/filter/overview"
headers = {
    'User-Agent': 'iphoneapp.b612cn/9.1.0 (iPhone; U; CPU iOS 13_1_3 like Mac OS X; zh-Hans-DE-DE; occ-NULL "iPhone X" )'
}
response = requests.get(apiUrl, headers = headers)
filterOverview = json.loads(response.text)
pprint.pprint(filterOverview)