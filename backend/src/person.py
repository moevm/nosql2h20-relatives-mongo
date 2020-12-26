from typing import List
import json


class Person:

    def __init__(self, name: str, byear: str, dyear: str, gender: str, mother: str, father: str, dynasty=None,
                 children=[]):
        self.name = name
        self.byear = byear
        self.dyear = dyear
        self.gender = gender
        self.dynasty = dynasty
        self.parents = [mother,
                        father]
        self.children = children

    def add_dynasty(self, dynasty: str):
        self.dynasty = dynasty

    def add_children(self, id_):
        self.children.append(id_)
        print("append {}", id_)

    def get_parents(self):
        return self.parents

    def get_children(self):
        return self.children

    def __str__(self):
        return f'Person({self.name} {self.byear} {self.dyear} {self.gender} {self.dynasty})'

    def __eq__(self, other: 'Person'):
        return self.name == other.name and self.byear == other.byear

    @staticmethod
    def create_from_dict(obj) -> 'Person':
        return Person(obj['name'], obj['byear'], obj['dyear'], obj['gender'], obj['mid'], obj['fid'], obj['dynasty'], obj['children'])
