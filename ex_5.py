import requests
import pprint
import json
from urllib.request import urlopen


class FilterApi(object):
    def __init__(self):
        super(FilterApi, self).__init__()
        self.filterOverview = dict()  

   
    def getKajiFilterJson(self):
        with urlopen('http://qa-api.b612kaji.com/v1/filter/overview') as resp:  
            self.filterOverview = json.load(resp)  

    
    def getFilterName(self, filterId):
        for f in self.filterOverview['result']['filters']:  
            if str(f['id']) == filterId:  
                return f['name']
        return None
 
    
    def printFilterName(self, *args):  
        for f_id in args:  
            print(self.getFilterName(f_id))  


filter_api = FilterApi()  

filter_api.getKajiFilterJson()  
print(filter_api.filterOverview)  

filterName = filter_api.getFilterName("300299")  
print(filterName)  

filter_api.printFilterName("300299", "300171", "300252")  
