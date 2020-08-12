import requests
import json
import pprint
from urllib.request import urlopen



def getKajiFilterJson():
    
    with urlopen('http://qa-api.b612kaji.com/v1/filter/overview') as resp:
        filterOverview = json.load(resp)  
        return filterOverview


filterJson = getKajiFilterJson()  
print(filterJson)  



def getFilterName(filterJson, filterId):
    for f in filterJson['result']['filters']:  
        if str(f['id']) == filterId:  
            return f['name']  
    return None  


filterJson = getKajiFilterJson()  
filterName = getFilterName(filterJson, "300299")  
print(filterName)  



def printFilterName(filterJson, *args):
    for f_id in args:  
        print(getFilterName(filterJson, f_id))  


filterJson = getKajiFilterJson()  
printFilterName(filterJson, "300299", "300171", "300252") 
