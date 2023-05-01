import requests

from requests_pack.get_token import generate_token


def get_a_book(bookId):
    request_body = {
        "bookId":bookId
    }
    token = generate_token()
    header_params = {'Authorization':token}
    response = requests.get(f'https://simple-books-api.glitch.me/books/{bookId}', json=request_body, headers=header_params)
    return response