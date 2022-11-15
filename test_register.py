import requests

url = 'https://pdiot-367920.ew.r.appspot.com/register'

registerObject = {'student_id': 's1911028', 'password': '12312312312'}
response = requests.post(url, json=registerObject)

print(response)
print(response.status_code)
