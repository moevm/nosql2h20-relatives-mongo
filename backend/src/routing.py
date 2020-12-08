from bottle import run, get, post, request, response
from backend.src.network import host, port
from backend.src.person import Person
from backend.src.dynasty import Dynasty
from backend.src.database import MongoDB


@post('/add_person')
def add_person():
    response.content_type = 'application/json'

    print('POST', request.json)
    result = dict()

    try:
        key = db.add_person(Person(request.json['name'],
                                   request.json['byear'],
                                   request.json['dyear'],
                                   request.json['gender'],
                                   request.json['mid'],
                                   request.json['fid']))
        result['success'] = True
        result['id'] = key
        result['name'] = request.json['name']
        result['byear'] = request.json['byear']
        result['dyear'] = request.json['dyear']
        result['mid'] = request.json['mid']
        result['fid'] = request.json['fid']
        result['gender'] = request.json['gender']

    except:
        result['success'] = False

    print(result)
    print(db.db.command("dbstats"))


@post('/add_dynasty')
def add_dynasty():
    response.content_type = 'application/json'

    print('POST', request.json)
    result = dict()

    try:
        founder = Person(request.json['name'],
                     request.json['byear'],
                     request.json['dyear'],
                     request.json['gender'],
                     None,
                     None)
        dynasty = Dynasty(request.json['dyn'], founder)
        founder_key = db.add_person(founder)
        dynasty_key = db.add_dynasty(dynasty, founder_key)
        founder.add_dynasty(dynasty_key)
        db.update_person(founder_key, founder)
        result['success'] = True
        result['dynasty_id'] = dynasty_key
        result['founder_id'] = founder_key
        result['dyn'] = request.json['dyn']
        result['name'] = request.json['name']
        result['byear'] = request.json['byear']
        result['dyear'] = request.json['dyear']
        result['gender'] = request.json['gender']

    except:
        result['success'] = False

    print(result)


# @post('show_dynasty')
# def show_dynasty():
#     response.content_type = 'application/json'
#
#     print('POST', request.json)
#     result = dict()
#
#     try:
#
#
#     except:
#         result['success'] = False
#
#     print(result)


def run_server():
    global db
    db = MongoDB()
    run(host=host, port=port)


run_server()
