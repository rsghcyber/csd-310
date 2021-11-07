"""
    Title: pytech_insert.py
    Author: Robin Sebbag
    Date: 11/07/2021
    Description: Test program for inserting new documents into the students collection.
"""

"""import statements"""
from pymongo import MongoClient

# MongoDB Connection string
url = "mongodb+srv://admin:admin@cluster0.ddqvy.mongodb.net/test"

# Connect to MongoDB cluster
client = MongoClient(url)

# Connect pytech database
db = client.pytech

""" Student documents """

#Student 1 document: John Doe
john = {
    "student_id": "1007",
    "first_name": "John",
    "last_name": "Doe",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "3.0",
            "start_date": "July 10, 2021",
            "end_date": "September 20, 2021",
            "courses": [
                {
                    "course_id": "CSD320",
                    "description": "Programming with Python",
                    "instructor": "Professor X",
                    "grade": "B"

                },
                {
                    "course_id": "CSD340",
                    "description": "Application Security",
                    "instructor": "Professor Y",
                    "grade": "B-"
                }
            ]
        }
    ]
}


#Student 2 document: Jane Doe
jane = {
    "student_id": "1008",
    "first_name": "Jane",
    "last_name": "Doe",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "3.3",
            "start_date": "July 10, 2021",
            "end_date": "September 20, 2021",
            "courses": [
                {
                    "course_id": "CSD320",
                    "description": "Programming with Python",
                    "instructor": "Professor X",
                    "grade": "B+"

                }
            ]
        }
    ]
}

#Student 3 document: Jennifer White
jennifer = {
    "student_id": "1009",
    "first_name": "Jennifer",
    "last_name": "White",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "2.8",
            "start_date": "July 10, 2021",
            "end_date": "September 20, 2021",
            "courses": [
                {
                    "course_id": "CSD320",
                    "description": "Programming with Python",
                    "instructor": "Professor X",
                    "grade": "B-"

                },
                {
                    "course_id": "CSD340",
                    "description": "Application Security",
                    "instructor": "Professor Y",
                    "grade": "B-"
                }
            ]
        }
    ]
}

students = db.students

# Insert statements + output
print("\n  -- INSERT STATEMENTS --")
john_student_id = students.insert_one(john).inserted_id
print("  Inserted student record John Doe into the students collection with document_id " + str(john_student_id))

jane_student_id = students.insert_one(jane).inserted_id
print("  Inserted student record Jane Doe into the students collection with document_id " + str(jane_student_id))

jennifer_student_id = students.insert_one(jennifer).inserted_id
print("  Inserted student record Jennifer White into the students collection with document_id " + str(jennifer_student_id))

input("\n\n  End of program, press any key to exit... ")