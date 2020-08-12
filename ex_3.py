'''
Q1) API result → filters[] 내부 필터들의 id & name 을 모두 출력해보자
Q2) API result → groups[] 내부의 그룹의 id, name과 그룹에 속한 filtersIds를 모두 출력해보자.
Q3) API result → filters[] 내부 필터들 중에서, type == "BUILT_IN" 에 해당하는 필터들의 id & name 을 출력해보자.
Q4) API result → filters[] 내부 필터들 중에서, subname 이 있는 필터들의 id & name & subname 을 출력해보자.
'''


import requests
import json
import pprint
from urllib.request import urlopen
#with urlopen('https://pypi.org/pypi/sampleproject/json') as resp:
#    project_info = json.load(resp)['info']
with urlopen('http://qa-api.b612kaji.com/v1/filter/overview') as resp:
    assert isinstance(resp, object)
    filterOverview = json.load(resp)

headers = {
    'User-Agent': 'iphoneapp.b612cn/9.1.0 (iPhone; U; CPU iOS 13_1_3 like Mac OS X; ko-KR-KR; occ-KR "iPhone X" )'
}
print(resp)

#pprint.pprint(filterOverview)

print('--------No.1------')
for e in filterOverview['result']['filters']:
    print("NAME: %s, ID: %d" % (e['name'], e['id']))

    print('----------------------------------------------------------------')

'''
    print('-------No.2-----')
    for e in filterOverview['result']['groups']:
        print("group ID: %d, NAME: %s, filterIds: %s" % (e['id'], e['name'], e['filterIds']))

    print('---------------------------------------------------------------------------')

    print('-------No.3-----')
    for e in filterOverview['result']['filters']:
        if "type" in e and e['type'] == "BUILT_IN":
            print("ID: %d, NAME: %s" % (e['id'], e['name']))

    print('---------------------------------------------------------------------------')

    print('-------No.4-----')
    for e in filterOverview['result']['filters']:
        if "subName" in e:
            print("ID: %d, NAME: %s, subName: %s" % (e['id'], e['name'], e['subName']))

    print('---------------------------------------------------------------------------')
    '''