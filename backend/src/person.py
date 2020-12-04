from typing import List


class Person:

    def __init__(self, name: str, dateOfBirth: str, dateOfDeath: str, gender: str, dynasty: str, parents: List[object], children: List[object]):
        self.name = name
        self.dateOfBirth = dateOfBirth
        self.dateOfDeath = dateOfDeath
        self.gender = gender
        self.dynasty = dynasty
        self.parents = parents if parents is not None else []
        self.children = children if children is not None else []

    def get_parents_tree(self):
        res = '['
        if self.parents is not None:
            res += '['
            for i, val in enumerate(self.parents):
                res += val.name
                res += ',' if i!=self.parents.__len__() else ''
                res += val.get_parents_tree()
            res += ']'
        res += ']'
        return res

    def get_children_tree(self):
        res = '['
        if self.parents is not None:
            res += '['
            for i, val in enumerate(self.children):
                res += val.name
                res += ',' if i!=self.children.__len__() else ''
                res += val.get_children_tree()
            res += ']'
        res += ']'
        return res

    def __str__(self):
        return f'Person({self.name} {self.dateOfBirth} {self.dateOfDeath} {self.gender} {self.dynasty})'

    def __eq__(self, other: 'Person'):
        return self.name == other.name and self.dateOfBirth == other.dateOfBirth
    
    @staticmethod
    def create_from_dict(obj) -> 'Person':
        return Person(obj['name'], obj['dateOfBirth'], obj['dateOfDeath'], obj['gender'], obj['dynasty'],
                      obj['parents'], obj['children'])
