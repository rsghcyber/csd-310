"""
    Title: mongodb_test.py
    Author: Robin Sebbag 
    Date: 11/07/2021
    Description: Test program for connecting to a MongoDB Atlas Cluster
"""
"""import statements"""

from pymongo import MongoClient

#Connection string#
url = "mongodb+srv://admin:<password>@cluster0.ddqvy.mongodb.net/test"

#Connect to MongoDB cluster#
client = MongoClient(url)

#Connect to pytech database#
db = client.pytech

#Show connected collections#
print("\n -- Pytech COllection List --")
print(db.list_collection_names())

#Exit message#
input("\n\n  End of program, press any key to exit... ")
