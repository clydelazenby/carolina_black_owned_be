import requests

# Replace with your actual token
token = '9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'

headers = {
    'Authorization': f'Token {token}',
}

response = requests.get('http://localhost:8000/api/login/', headers=headers)

print(response.json())