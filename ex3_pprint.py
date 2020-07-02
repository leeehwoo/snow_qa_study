import json
import pprint
from urllib.request import urlopen
with urlopen('http://qa-api.b612kaji.com/v1/filter/overview') as resp:
    project_info = json.load(resp)['result']
pprint.pprint(project_info)
#pprint.pprint(project_info, depth=1)
#pprint.pprint(project_info, depth=5, width=60)
