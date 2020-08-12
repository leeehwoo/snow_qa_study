#!/usr/local/bin/python3
import requests, json, urllib.request
 
apiUrl = "https://api.generated.photos/api/v1/faces"
authKey = "jjjGLDylANlDIQdWgJf7wQ" # 발급받은키
 
headers = {
    'Authorization': 'API-Key ' + authKey
}
 
data = {
    'gender': 'female',
    'ethnicity': 'asian',
    'age': 'young-adult',
}
 
response = requests.get(apiUrl, headers = headers, data=data)
resultJson = json.loads(response.text)
 
for face in resultJson["faces"]:
    id = face["id"]
    imageUrl = face["urls"][4]["512"]
    filePath = "/Users/user/study_python/face" + id + ".jpg"
    urllib.request.urlretrieve(imageUrl, filePath)
    print(filePath)