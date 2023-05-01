import requests

from requests_pack.get_token import generate_token


def update_order(orderId, customerName):
    req_body = {
        "orderId":orderId,
        "customerName":customerName
    }
    token = generate_token()
    header_params = {"Authorization":token}
    response = requests.patch(f'https://simple-books-api.glitch.me/orders/{orderId}', headers= header_params, json=req_body)
    return response