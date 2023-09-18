import json

import requests


def get_json_from_endpoint(endpoint_url: str):
    try:
        response = requests.get(endpoint_url)
        response.raise_for_status()
        json_data = response.json()
        return json_data
    except requests.exceptions.RequestException as e:
        print(f"Ошибка: {e}")
        return None


def start():
    data = get_json_from_endpoint("http://localhost:5000/api/v1/quotes")
    list_of_quotes = data['quotes']
    for unit in list_of_quotes:
        id = unit['id']
        quote = unit['quote']
        print(quote)


def lol():
    data = get_json_from_endpoint("http://localhost:5000/get_question")
    data = data[0]['question']
    print(data)

lol()