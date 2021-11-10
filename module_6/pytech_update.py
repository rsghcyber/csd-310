""" 
    Title: pytech_update.py
    Author: Robin Sebbag
    Date: 14/11/2021
    Description: Test program for updating documents in pytech collection.
 """

# Import statements

from pymongo import MongoClient

#Connection string#
url = "mongodb+srv://admin:admin@cluster0.ddqvy.mongodb.net/test"

#Connect to MongoDB cluster#
client = MongoClient(url)

# Connect pytech database
db = client.pytech

# Call students collection
students = db.students

# Finding all students
student_list = students.find({})

# Displaying all student documents
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# Updating student document
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Smith"}})

# Finding updated student document
john = students.find_one({"student_id": "1007"})

# Displaying updated student document
print("\n  -- DISPLAYING STUDENT DOCUMENT 1007 --")

print(" Student ID: " + john["student_id"] + "\n First Name:" + john["first_name"] + "\n Last Name:" + john["last_name"] + "\n")

input("\n\n  End of program, press any key to continue...")
