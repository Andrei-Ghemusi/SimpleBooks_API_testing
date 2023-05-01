import requests

from requests_pack.get_token import generate_token


def get_an_order(orderId):
    req_body = {
        "orderId":orderId
    }
    token = generate_token()
    header_params = {"Authorization":token}
    response = requests.get(f'https://simple-books-api.glitch.me/orders/{orderId}', headers= header_params, json=req_body)
    return response

