from pymongo import MongoClient
import unittest
from backend.src.person import Person
from backend.src.dynasty import Dynasty
from backend.src.collection_manager import CollectionManager

# gender constants
M = 'M'
F = 'F'


class MongoDB:

    def __init__(self, host='localhost', port=27017):
        self.client = MongoClient(host, port)
        self.db = self.client['dynasty-db']
        self.persons = CollectionManager(self.db.persons)
        self.dynasties = CollectionManager(self.db.dynasties)

    def get_dynasty_tree(self, dynasty_member):
        children = dynasty_member.get_children()
        res = []
        for i, val in enumerate(children):
            next_member = self.get_person(val)
            if next_member is not None:
                res.append(next_member.name)
            if next_member.get_children().__len__() != 0:
                res.append(self.get_dynasty_tree(next_member))
        return res

    def update_person(self, id_, person: Person):
        self.persons.collection.update(self.persons.collection.find({"_id": id_}).next(),
                                       {"$set": {"dynasty": person.dynasty, "children": person.children}})

    def add_person(self, person: Person):
        id_ = self.persons.next_id()
        mother = self.get_person(person.parents.__getitem__(0))
        father = self.get_person(person.parents.__getitem__(1))
        if mother is not None:
            mother.add_children(id_)
            self.update_person(person.parents.__getitem__(0), mother)
        if father is not None:
            father.add_children(id_)
            self.update_person(person.parents.__getitem__(1), father)
        if mother is not None and father is not None:
            mother_dynasty = self.get_dynasty({"_id": mother.dynasty})
            father_dynasty = self.get_dynasty({"_id": father.dynasty})
            if mother_dynasty is None:
                person.add_dynasty(self.get_dynasty({"_id": father.dynasty}))
            elif father_dynasty is None:
                person.add_dynasty(self.get_dynasty({"_id": mother.dynasty}))
            else:
                if self.get_person(mother_dynasty.founder).gender == 'F' and self.get_person(
                        father_dynasty.founder).gender == 'M':
                    person.add_dynasty(father_dynasty)
                elif self.get_person(mother_dynasty.founder).gender == 'F':
                    person.add_dynasty(mother_dynasty)
                elif self.get_person(father_dynasty.founder).gender == 'F':
                    person.add_dynasty(father_dynasty)
                else:
                    person.add_dynasty(father_dynasty)
        try:
            self.persons.collection.insert_one({"_id": id_,
                                                "name": person.name,
                                                "byear": person.byear,
                                                "dyear": person.dyear,
                                                "gender": person.gender,
                                                "dynasty": person.dynasty,
                                                "mid": person.parents.__getitem__(0),
                                                "fid": person.parents.__getitem__(1),
                                                "children": person.children
                                                })
            return id_
        except:
            self.persons.collection.replace_one(self.persons.collection.find({"_id": id_}).next(),
                                                {"_id": id_,
                                                 "name": person.name,
                                                 "byear": person.byear,
                                                 "dyear": person.dyear,
                                                 "gender": person.gender,
                                                 "dynasty": person.dynasty,
                                                 "mid": person.parents.__getitem__(0),
                                                 "fid": person.parents.__getitem__(1),
                                                 "children": person.children
                                                 })
            return id_

    def get_person(self, id_):
        try:
            res = self.persons.collection.find({"_id": id_}).next()
            return Person.create_from_dict({key: res[key] for key in res if key != '_id'})
        except:
            return None

    def add_dynasty(self, dynasty: Dynasty, founder_id: str):
        id_ = self.dynasties.next_id()
        try:
            self.dynasties.collection.insert_one({"_id": id_,
                                                  "name": dynasty.name,
                                                  "founder": founder_id})

            return id_
        except:
            self.dynasties.collection.replace_one(self.dynasties.collection.find({"_id": id_}).next(),
                                                  {"_id": id_,
                                                   "name": dynasty.name,
                                                   "founder": founder_id})
            return id_

    def get_dynasty(self, id_):
        try:
            res = self.dynasties.collection.find({"_id": id_}).next()
            return Dynasty.create_from_dict({key: res[key] for key in res if key != '_id'})
        except:
            return None

    def clear_db(self):
        self.persons.collection.drop()
        self.dynasties.collection.drop()


class MongoTest(unittest.TestCase):
    def test_add_and_get(self):
        mongoDB = MongoDB()
        person = Person('John Snow', '2.2.2', '2.2.2', 'male', 2, 3)
        mongoDB.add_person(person)
        self.assertIsInstance(mongoDB.get_person('0'), Person)
        mongoDB.clear_db()
