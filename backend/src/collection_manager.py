from pymongo import DESCENDING


class CollectionManager:

    def __init__(self, collection):
        self.collection = collection
        self.id = self._generate_ids()

    def next_id(self):
        return next(self.id)

    def _generate_ids(self):
        id_: int = self.get_max_id()
        while True:
            id_ += 1
            yield str(id_)

    def get_all_documents(self):
        return self.collection.find()

    def get_all_keys(self):
        only_ids_cursor = self.collection.find({}, {'_id': 1})
        list = []
        for elem in only_ids_cursor:
            list.append(elem['_id'])
        return list

    def remove_object(self, _id):
        self.collection.delete_one({'_id': _id})

    def get_max_id(self) -> int:
        try:
            return int(self.get_all_documents().sort([('_id', DESCENDING)])[0]['_id'])
        except:
            return -1

    def is_empty(self) -> bool:
        return False if self.get_all_documents().count() > 0 else True
