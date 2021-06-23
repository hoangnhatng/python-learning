import pymongo
from pymongo import MongoClient
import pprint

cluster = pymongo.MongoClient("mongodb+srv://hoangnhatng02:qpi1YEWOuVMtgokj@cluster0.bphkg.mongodb.net/test-iot?retryWrites=true&w=majority")
db = cluster["test-iot"]
collection = db["test-01"]

post = {"x":1}
#collection.insert_one(post)
#db.create_collection("test-04")can't find '__main__' module in ''
#collection = db.collection_names(include_system_collections=False)

collection.create_index([('c1',"text")],default_language='english')

results = collection.find({'$text':{'$search':"\"2021/06/23\""}})
r_one = collection.find_one({'$text':{'$search':"\"2021/06/23\""}})

#for db_name in cluster.list_databases():
#   print(db_name)

#for x in results:
#   pprint.pprint(x)
print(r_one)
print(r_one['_id'].generation_time)


