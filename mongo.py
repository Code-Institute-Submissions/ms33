import os
import pymongo
if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "lotteryDB"
COLLECTION = "scratchers"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]

# Pep8 compliance - no long lines
# two dictionaries array
# fill in the value below to add multiple records
new_doc = [{
    "title": "game_name",
    "price": "1,2,3,5,10",
    "prize": "dollarAmt",
    "county": "nearestCounty",
    "date": "05/19/2021",
    "address": "street",
    "city": "where_purchased",
    "retailer": "store_name"
}, {
    "title": "game_name",
    "price": "1,2,3,5,10",
    "prize": "dollarAmt",
    "county": "nearestCounty",
    "date": "05/19/2021",
    "address": "street",
    "city": "where_purchased",
    "retailer": "store_name"
}]

coll.insert_many(new_doc)

documents = coll.find()

for doc in documents:
    print(doc)
