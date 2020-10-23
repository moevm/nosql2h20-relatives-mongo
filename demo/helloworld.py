import pymongo
import pprint

client = pymongo.MongoClient(host='localhost', port=27027)
db = client['helloworld-db']

doc1 = {"band": "AC/DC",
        "tracks": ["Back in Black", "A Shot In The Dark"]}
doc2 = {"band": "Motley Crue",
        "tracks": ["Girls, girls, girls!", "Kickstart My Heart"]}

posts = db.posts
id1 = posts.insert_one(doc1).inserted_id
id2 = posts.insert_one(doc2).inserted_id

pprint.pprint(posts.find_one({"_id": id1}))
pprint.pprint(posts.find_one({"_id": id2}))