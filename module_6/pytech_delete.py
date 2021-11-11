"""
    Title: pytech_delete
    Author: Robin Sebbag
    Date: 14/11/2021
    Description: Test program for deleting documents from pytech collection.
"""

# Import statements
from pymongo import MongoClient

# Connection string 
url = "mongodb+srv://admin:admin@cluster0.ddqvy.mongodb.net/test"

# Connect to MongoDB cluster
client = MongoClient(url)

# Connect pytech database
db = client.pytech

# Call students collection
students = db.students

# Find all students in collection
student_list = students.find({})

# Display results
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# Creating new student document
new_doc = {
    "student_id": "1010",
    "first_name": "Harry",
    "last_name": "Houdini"
}

# Inserting new document into Atlas
new_doc_id = students.insert_one(new_doc).inserted_id

# Insert statements and output
print("\n -- INSERT STATEMENTS --")
print(" Inserted student record into students collection with document_id" + str(new_doc_id))

# Find student 1010
student_test_doc = students.find_one({"student_id": "1010"})

# Display results
print("\n -- DISPLAYING STUDENT TEST DOC --")
print(" Student ID: " + student_test_doc["student_id"] + " \n First name: " + student_test_doc["first_name"] + " \n Last name: " + student_test_doc["last_name"] + "\n")

# Delete test doc
deleted_student_test_doc = students.delete_one({"student_id": "1010"})

# Find all students in collection
new_student_list = students.find({})

print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# Loop over collection and display results
for doc in new_student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# Exit message
input("\n\n  End of program, press any key to continue...")