import requests
import random

def generate_token():
    nr = random.randint(1,999999)
    request_body = {
        "clientName":'Andrei',
        "clientEmail":f'andreighemusi{nr}@example.com'
    }
    response = requests.post('https://simple-books-api.glitch.me', json=request_body)
    token = response.json()['accessToken']
    return token