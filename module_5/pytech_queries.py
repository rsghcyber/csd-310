""" 
    Title: pytech_queries.py
    Author: Robin Sebbag
    Date: 11/07/2021
    Description: Test program for querying the students collection
"""
from pymongo import MongoClient

# Connection string
url = "mongodb+srv://admin:admin@cluster0.ddqvy.mongodb.net/test"

# Connect to MongoDB cluster
client = MongoClient(url)

# Connect pytech database
db = client.pytech

# Retrieve students collection
students = db.students

# Find all students in students collection
student_list = students.find({})

print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# Loop over collection and output results
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# Locate document by student_id
john = students.find_one({"Student_id": "1007"})

# Output results
print("\n  -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print("  Student ID: " + john["student_id"] + "\n  First Name: " + john["first_name"] + "\n  Last Name: " + john["last_name"] + "\n")

# Exit message
input("\n\n  End of program, press any key to continue...")
