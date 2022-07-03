""" 
    Title: pytech_queries.py
    Author: Sam Paye
    Date: 03 July 2022
    Description: Queries
"""

""" import statements """
from pymongo import MongoClient

# MongoDB connection string 
url = mongodb+srv://admin:admin@cluster0.kcxahui.mongodb.net/?retryWrites=true&w=majority

# connect to the MongoDB cluster 
client = MongoClient(url)

# connect pytech database
db = client.pytech

# get students collection
students = db.students

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over the collection and output the results 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# find document by student_id
bilbo = students.find_one({"student_id": "1008"})

# output the results 
print("\n  -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print("  Student ID: " + Bilbo["student_id"] + "\n  First Name: " + Bilbo["first_name"] + "\n  Last Name: " + Bilbo["last_name"] + "\n")

# exit message 
input("\n\n  End of program, press any key to continue...")
