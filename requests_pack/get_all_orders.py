import requests

from requests_pack.get_token import generate_token


def get_all_orders():
    token = generate_token()
    header_params = {'Authorization':token}
    response = requests.get('https://simple-books-api.glitch.me/orders', headers= header_params)
    return response