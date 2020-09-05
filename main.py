from flask import Flask, jsonify, request
import settings
import helper

app = Flask(__name__)

TOKEN = settings.get_token()
SIZE = settings.get_size()
dictionary = {}
clients = {}


@app.route("/")
def index():
    return jsonify({'len': len(dictionary)})


@app.route("/get/<key>")
def get(key):
    if helper.client_check(request.headers.get('client_token'), clients):
        if key in dictionary:
            item = dictionary[key]
            return jsonify({key: item, 'status': 1})
        else:
            return jsonify({'status': 404})
    else:
        return jsonify({'auth': 401})


@app.route('/delete/<key>')
def delete(key):
    if helper.client_check(request.headers.get('client_token'), clients):
        dictionary.pop(key)
        return jsonify({'status': 1})
    else:
        return jsonify({'auth': 401})


@app.route("/add/<key>/<value>")
def add(key, value):
    if helper.client_check(request.headers.get('client_token'), clients):
        if key in dictionary:
            return jsonify({'status': 400})
        else:
            dictionary[key] = value
            return jsonify({'status': 1})
    else:
        return jsonify({'auth': False})


@app.route("/auth")
def auth():
    print(request.headers)
    if TOKEN == request.headers.get('token'):
        client_token = settings.secure_token()
        clients[client_token] = helper.epoch_time()
        print(clients)
        return jsonify({'token': client_token, 'auth': True})
    else:
        return jsonify({'auth': False})


if __name__ == "__main__":
    app.run()
