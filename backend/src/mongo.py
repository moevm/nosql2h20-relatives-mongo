from pymongo import DESCENDING as DESCENDING
from pymongo import MongoClient
from pymongo.database import Database as MongoDatabase
from pymongo.collection import Collection as MongoCollection
from backend.src.person import Person
from backend.src.dynasty import Dynasty

class MongoDB:

    def __init__(self, host='localhost', port=27027):
        self.client = MongoClient(host, port)
        self.db = self.client['dynasty-db']

    def get_tree(self, id_):
        self.client: MongoDatabase
        try:
            res = self.client.find({"_id": id_}).next()
            tree = Person.create_from_dict({key: res[key] for key in res if key != '_id'}).get_parents_tree() + '['
            + Person.create_from_dict({key: res[key] for key in res if key != '_id'}).name + ']' + Person.create_from_dict({key: res[key] for key in res if key != '_id'}).get_children_tree()
            return tree
        except:
            return  None

    def add_person(self, id_: str, person: Person):
        self.client: MongoCollection
        try:
            self.client.insert_one({"_id": id_,
                                    "name": person.name,
                                    "dateOfBirth": person.dateOfBirth,
                                    "dateOfDeath": person.dateOfDeath,
                                    "gender": person.gender,
                                    "dynasty": person.dynasty})
        except:
            self.client.replace_one(self.client.find({"_id": id_}).next(),
                                    {"_id": id_,
                                     "name": person.name,
                                    "dateOfBirth": person.dateOfBirth,
                                    "dateOfDeath": person.dateOfDeath,
                                    "gender": person.gender,
                                    "dynasty": person.dynasty})

    def get_person(self, id_):
        self.client: MongoDatabase
        try:
            res = self.client.find({"_id": id_}).next()
            return Person.create_from_dict({key: res[key] for key in res if key != '_id'})
        except:
            return None

    def add_dynasty(self, id_: str, dynasty: Dynasty):
        self.client: MongoCollection
        try:
            self.client.insert_one({"_id": id_,
                                    "name": dynasty.name,
                                    "founder": dynasty.founder})
        except:
            self.client.replace_one(self.client.find({"_id": id_}).next(),
                                    {"_id": id_,
                                     "name": dynasty.name,
                                    "founder": dynasty.founder})

    def get_dynasty(self, id_):
        self.client: MongoDatabase
        try:
            res = self.client.find({"_id": id_}).next()
            return Dynasty.create_from_dict({key: res[key] for key in res if key != '_id'})
        except:
            return None

    def clear_db(self):
        return self.client.drop()

    def get_all_documents(self):
        return self.client.find()

    def get_all_keys(self):
        only_ids_cursor = self.client.find( {}, {'_id' : 1 } )
        list = []
        for elem in only_ids_cursor:
            list.append(elem['_id'])
        return list

    def remove_object(self, _id):
        self.client.delete_one({ '_id' : _id })

    def get_max_id(self) -> int:
        try:
            return int(self.get_all_documents().sort([('_id', DESCENDING)])[0]['_id'])
        except:
            return -1

    def is_empty(self) -> bool:
        return False if self.get_all_documents().count() > 0 else True