import requests


def get_all_books(type="", limit=""):
    params = {}
    if type:
        params["type"] = type
    if limit:
        params["limit"] = limit
    response = requests.get("https://simple-books-api.glitch.me/books", params=params)

    return response
