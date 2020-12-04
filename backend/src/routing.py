from bottle import route, run, static_file, get, post, request, response
from backend.src.network import host, port
import json
from backend.src.mongo import MongoDB

@post('/')
def post_request():

    response.content_type = 'application/json'

    print('POST', request.json)
    result = dict()

    if request.json['action'] == 'add-person':

#adding

    elif request.json['action'] == 'search':

# searching

def run_server():
    global db
    db = MongoDB()
    run(host=host, port=port)