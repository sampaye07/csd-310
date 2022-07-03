""" 
    Title: pytech_insert.py
    Author: Sam Paye
    Date: 03 July 2022
    Description: Test program for connecting to a 
                 MongoDB Atlas cluster
"""

""" import statements """
from pymongo import MongoClient

# MongoDB connection string 
url = mongodb+srv://admin:admin@cluster0.kcxahui.mongodb.net/?retryWrites=true&w=majority

# connect to the MongoDB cluster 
client = MongoClient(url)

# connect pytech database
db = client.pytech

""" New student documtents
# Thorin Oakenshield
Thorin = {
    "student_id": "1007",
    "first_name": "Thorin",
    "last_name": "Oakenshield",
    "enrollments": [
        {
            "term": "Winter",
            "gpa": "3.9",
            "start_date": "20221201",
            "end_date": "20230301",
            "courses": [
                {
                    "course_id": "CYBR1000",
                    "description": "Hacking Crypto",
                    "instructor": "Professor Blackhat",
                    "grade": "A"
                },
                {...},
		{...}
            ]
        }
    ]
    [...],
    [...]
}

# Bilbo Baggins
Bilbo = {
    "student_id": "1008",
    "first_name": "Bilbo",
    "last_name": "Baggins",
    "enrollments": [
        {
            "term": "Winter",
            "gpa": "4.0",
            "start_date": "20221201",
            "end_date": "20230301",
            "courses": [
                {
                    "course_id": "CYBR1000",
                    "description": "Hacking Crypto",
                    "instructor": "Professor Blackhat",
                    "grade": "A+"
                },
                {...},
		{...}
            ]
        }
    ]
    [...],
    [...]
}

#Frodo Baggins
Frodo = {
    "student_id": "1009",
    "first_name": "Frodo",
    "last_name": "Baggins",
    "enrollments": [
        {
            "term": "Winter",
            "gpa": "2.3",
            "start_date": "20221201",
            "end_date": "20230301",
            "courses": [
                {
                    "course_id": "CYBR1000",
                    "description": "Hacking Crypto",
                    "instructor": "Professor Blackhat",
                    "grade": "D-"
                },
                {...},
		{...}
            ]
        }
    ]
    [...],
    [...]
}

# get students collection
students = db.students

#insert statements with output
print("\n  -- INSERT STATEMENTS --")
thorin_student_id = students.insert_one(Thorin).inserted_id
print("  Inserted student record Thorin Oakenshield into the students collection with document_id " + str(thorin_student_id))

bilbo_student_id = students.insert_one(Bilbo).inserted_id
print("  Inserted student record Bilbo Baggins into the students collection with document_id " + str(bilbo_student_id))

frodo_student_id = students.insert_one(Frodo).inserted_id
print("  Inserted student record Frodo Baggins into the students collection with document_id " + str(frodo_student_id))

input("\n\n  End of program, press any key to exit... ")
