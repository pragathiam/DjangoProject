import requests
import json

URL1='http://127.0.0.1:8000/api/students'

URL2='http://127.0.0.1:8000/api/student/3'

# read(get)
# resp_data=requests.get(url=URL1)
# print(resp_data) # <Response [200]> # <Response [404]>
# print(resp_data.json())
#[{'s_name': 'dinesh', 's_rollno'; 11,'s_course':'comp'},{'s_name': 'mahesh','s_rollno'; 11,'s_course':'IT'},{{'s_name': 'pritik','s_rollno'; 11,'s_course':'IT'}}]

# create (post)
# py_data={'s_name':'vinay', 's_rollno': 79, 's_course': 'IT'}
# resp=requests.post(url=URL1,data=json.dumps(py_data))
# print(resp.json())

# update(put/patch)
# http://127.0.0.1:8000/api/student/3

py_data={'s_name':'pragna', 's_rollno': 99, 's_course': 'computer'}
py_data={'s_name': 'qspiders'}
resp=requests.put(url=URL2,data=json.dumps(py_data))
print(resp)
print(resp.json())

# delete

resp=requests.delete(url=URL2)
print(resp.json())
