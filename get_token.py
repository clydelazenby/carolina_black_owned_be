import requests

response = requests.post('http://localhost:8000/api/token/', json={
    'username': 'MikeSmith',
    'password': 'Dipset07!',
})

if response.status_code == 200:
    token = response.json()['token']
    print('Token:', token)
else:
    print('Failed to obtain token:', response.content)