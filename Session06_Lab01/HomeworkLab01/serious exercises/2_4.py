from pymongo import MongoClient
import matplotlib
from matplotlib import pyplot

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)

db = client.get_default_database()

customers = db["customers"]

all_customer = customers.find()

references = {
    "Advertisements" : 0 ,
    "Events" : 0 ,
    "Word of mouth" : 0
}

for customer in all_customer:
    if customer["ref"] == "events":
        references["Events"] += 1
    elif customer["ref"] == "ads":
        references["Advertisements"] += 1
    else:
        references["Word of mouth"] += 1

for key, value in references.items():
    print("Number of customers by {}: {}".format(key, value))

pyplot.pie(
    references.values() , 
    labels = references.keys()
    )

pyplot.axis('equal')

pyplot.show()