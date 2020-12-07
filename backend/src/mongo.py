from pymongo import DESCENDING as DESCENDING
from pymongo import MongoClient
import unittest
from pymongo.database import Database as MongoDatabase
from pymongo.collection import Collection as MongoCollection
from backend.src.person import Person
from backend.src.dynasty import Dynasty

# gender constants
M = 'M'
F = 'F'


class MongoDB:

    def __init__(self, host='localhost', port=27017):
        self.client = MongoClient(host, port)
        self.db = self.client['dynasty-db']
        self.persons = self.db.persons
        self.dynasties = self.db.dynasties
        self.clear_db()
        self.persons_id = self._generate_ids(self.persons)  # исправить говнокод со статикметодами
        self.dynasties_id = self._generate_ids(self.dynasties)

    @staticmethod
    def _generate_ids(collection):
        id_: int = MongoDB.get_max_id(collection)
        while True:
            id_ += 1
            yield str(id_)

    def _next_id(self, collection):
        if collection.name == 'persons':
            return next(self.persons_id)
        if collection.name == 'dynasties':
            return next(self.dynasties_id)

    def get_tree(self, id_):
        try:
            res = self.persons.find({"_id": id_}).next()
            person = Person.create_from_dict({key: res[key] for key in res if key != '_id'})
            tree = person.get_parents_tree() + '[' + person.name + ']' + person.get_children_tree()
            return tree
        except:
            return None

    def update_person(self, id_, person: Person):
        self.persons.update(self.persons.find({"_id": id_}).next(),
                            {"$set": {"dynasty": person.dynasty}})

    def add_person(self, person: Person):
        id_ = self._next_id(self.persons)
        mother = self.get_person(person.parents.__getitem__(0))
        father = self.get_person(person.parents.__getitem__(1))
        if mother is not None and father is not None:
            mother_dynasty = self.get_dynasty({"_id": mother.dynasty})
            father_dynasty = self.get_dynasty({"_id": father.dynasty})
            if mother_dynasty is None:
                person.add_dynasty(self.get_dynasty({"_id": father.dynasty}))
            elif father_dynasty is None:
                person.add_dynasty(self.get_dynasty({"_id": mother.dynasty}))
            else:
                if self.get_person(mother_dynasty.founder).gender == 'F' and self.get_person(father_dynasty.founder).gender == 'M':
                    person.add_dynasty(father_dynasty)
                elif self.get_person(mother_dynasty.founder).gender == 'F':
                    person.add_dynasty(mother_dynasty)
                elif self.get_person(father_dynasty.founder).gender == 'F':
                    person.add_dynasty(father_dynasty)
                else:
                    person.add_dynasty(father_dynasty)
        try:
            self.persons.insert_one({"_id": id_,
                                     "name": person.name,
                                     "byear": person.byear,
                                     "dyear": person.dyear,
                                     "gender": person.gender,
                                     "dynasty": person.dynasty,
                                     "mid": person.parents.__getitem__(0),
                                     "fid": person.parents.__getitem__(1)})
            return id_
        except:
            self.persons.replace_one(self.persons.find({"_id": id_}).next(),
                                     {"_id": id_,
                                      "name": person.name,
                                      "byear": person.byear,
                                      "dyear": person.dyear,
                                      "gender": person.gender,
                                      "dynasty": person.dynasty,
                                      "mid": person.parents.__getitem__(0),
                                      "fid": person.parents.__getitem__(1)
                                      })
            return id_

    def get_person(self, id_):
        try:
            res = self.persons.find({"_id": id_}).next()
            return Person.create_from_dict({key: res[key] for key in res if key != '_id'})
        except:
            return None

    def add_dynasty(self, dynasty: Dynasty, founder_id: str):
        id_ = self._next_id(self.dynasties)
        try:
            self.dynasties.insert_one({"_id": id_,
                                       "name": dynasty.name,
                                       "founder": founder_id})

            return id_
        except:
            self.dynasties.replace_one(self.dynasties.find({"_id": id_}).next(),
                                       {"_id": id_,
                                        "name": dynasty.name,
                                        "founder": founder_id})
            return id_

    def get_dynasty(self, id_):
        try:
            res = self.dynasties.find({"_id": id_}).next()
            return Dynasty.create_from_dict({key: res[key] for key in res if key != '_id'})
        except:
            return None

    def clear_db(self):
        self.persons.drop()
        self.dynasties.drop()

    @staticmethod
    def get_all_documents(collection):
        return collection.find()

    @staticmethod
    def get_all_keys(collection):
        only_ids_cursor = collection.find({}, {'_id': 1})
        list = []
        for elem in only_ids_cursor:
            list.append(elem['_id'])
        return list

    @staticmethod
    def remove_object(collection, _id):
        collection.delete_one({'_id': _id})

    @staticmethod
    def get_max_id(collection) -> int:
        try:
            return int(MongoDB.get_all_documents(collection).sort([('_id', DESCENDING)])[0]['_id'])
        except:
            return -1

    @staticmethod
    def is_empty(collection) -> bool:
        return False if MongoDB.get_all_documents(collection).count() > 0 else True

    def get_size(self):
        self.db.__sizeof__()


class MongoTest(unittest.TestCase):
    def test_add_and_get(self):
        mongoDB = MongoDB()
        person = Person('John Snow', '2.2.2', '2.2.2', 'male', 2, 3)
        mongoDB.add_person(person)
        self.assertIsInstance(mongoDB.get_person('0'), Person)
        mongoDB.clear_db()
