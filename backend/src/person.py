from typing import List


class Person:

    def __init__(self, name: str, byear: str, dyear: str, gender: str, mother: str, father: str, dynasty=None):
        self.name = name
        self.byear = byear
        self.dyear = dyear
        self.gender = gender
        self.dynasty = dynasty
        self.parents = [mother,
                        father]  # добавить поиск по бд и определение династии, хранить список детей было бы удобно

    def add_dynasty(self, dynasty: str):
        self.dynasty = dynasty

    def get_parents_tree(self):
        res = '['
        if self.parents is not None:
            res += '['
            for i, val in enumerate(self.parents):
                res += val.name
                res += ',' if i != self.parents.__len__() else ''
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
                res += ',' if i != self.children.__len__() else ''
                res += val.get_children_tree()
            res += ']'
        res += ']'
        return res

    def __str__(self):
        return f'Person({self.name} {self.byear} {self.dyear} {self.gender} {self.dynasty})'

    def __eq__(self, other: 'Person'):
        return self.name == other.name and self.byear == other.byear

    @staticmethod
    def create_from_dict(obj) -> 'Person':
        return Person(obj['name'], obj['byear'], obj['dyear'], obj['gender'], obj['mid'], obj['fid'], obj['dynasty'])
