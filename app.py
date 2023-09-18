from flask import Flask, jsonify, request
import requests

app = Flask(__name__)


quotes = [
    {
        'id': 1,
        'author': 'Костенко',
        'quote': 'Сильный можно быть будучи слабым'
    },
    {
        'id': 2,
        'author': 'Полетайкин',
        'quote': 'Не каждый сильный может быть слабым'
    },
    {
        'id': 3,
        'author': 'Костенко',
        'quote': 'Люблю кошек'
    }
]


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/get_question', methods=['GET'])
def get_question():
    return requests.get('http://jservice.io/api/random?count=1').json()


@app.route('/api/v1/quotes', methods=['GET'])
def get_quotes():
    return jsonify({'quotes': quotes})

@app.route('/api/v1/quotes/find/author', methods=['POST'])
def find_author():
    data = request.get_json()
    query_value = ''
    list = []
    if 'query' in data:
        query_value = data['query']

    for quot in quotes:
        if quot['author'] == query_value:
            list.append(quot)

    return jsonify({'findedQuotes': list})



if __name__ == '__main__':
    app.run(debug=True)
