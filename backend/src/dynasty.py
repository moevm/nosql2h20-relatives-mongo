from person import Person


class Dynasty:

    def __init__(self, name: str, founder: Person):
        self.name = name
        self.founder = founder

    def __str__(self):
        return f'Card({self.name} {self.founder})'

    @staticmethod
    def create_from_dict(obj) -> 'Dynasty':
        return Dynasty(obj['name'], obj['founder'])
