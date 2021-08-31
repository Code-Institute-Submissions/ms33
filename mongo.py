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

#Pep8 compliance, splitting onto multiple lines
new_doc = {
        title: "Polaris-Road_To_Riches", price: "5",
        prize: "0..2nd-Chance_Lottery_Special_TicketEntry1-VehicleRaffle",
        county: "charleston", date: "05/19/2021", address: "Rivriera Dr.",
        city: "mount_pleasant", retailer: "harris_teeter"
    }

coll.insert(new_doc)

documents = coll.find()

for doc in documents:
    print(doc)
