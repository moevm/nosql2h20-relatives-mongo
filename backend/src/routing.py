from bottle import run, get, post, request, response
from network import host, port
from person import Person
from dynasty import Dynasty
from database import MongoDB
import json


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
    return json.dumps(result)
    # print(db.db.command("dbstats"))


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
    return json.dumps(result)


@get('/persons_list')
def persons_list():
    response.content_type = 'application/json'

    print('GET')
    result = dict()

    try:
        result['success'] = True
        result['res'] = []
        all_docs = db.persons.collection.find()
        for i in all_docs:
            try:
                person = all_docs.next()
                result['res'].append({key: person[key] for key in person if key == 'name'})
            except StopIteration:
                break
    except:
        result['success'] = False
    print(result)
    return json.dumps(result)


@get('/dynasty_list')
def dynasty_list():
    response.content_type = 'application/json'

    print('GET')
    result = dict()
    fulltree()

    try:
        result['success'] = True
        result['res'] = []
        all_docs = db.dynasties.collection.find()
        for i in all_docs:
            try:
                dynasty = all_docs.next()
                result['res'].append({key: dynasty[key] for key in dynasty if key == 'name'})
            except StopIteration:
                break
    except:
        result['success'] = False
    print(result)
    return json.dumps(result)


@get('/fulltree')
def fulltree():
    response.content_type = 'application/json'

    print('GET')
    result = dict()
    try:
        result['success'] = True
        result['res'] = []
        all_docs = db.dynasties.collection.find()
        for i, dynasty in enumerate(all_docs):
            try:
                founder = db.get_person(dynasty['founder'])
                result['res'].append(founder.name)
                result['res'].append(db.get_dynasty_tree(founder))
            except StopIteration:
                break
    except:
        result['success'] = False
    print(result)
    return json.dumps(result)


def run_server():
    global db
    db = MongoDB()
    run(host=host, port=port)
    db.clear_db()


run_server()
