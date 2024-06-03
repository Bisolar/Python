import sqlite3

# first_name = str(input("Enter your first name\n>"))
# last_name = str(input("Enter your last name\n>"))
# course = str(input("Enter your course\n>"))
connect = sqlite3.connect('program.db')

cursor = connect.cursor()

# cursor.execute('''CREATE TABLE IF NOT EXISTS student(
#                id INTEGER PRIMARY KEY AUTOINCREMENT, 
#                first_name TEXT, 
#                last_name TEXT, 
#                course TEXT)''')

# print("done")


# print(f"{first_name}, {last_name} your {course} has been registered")
# cursor.execute("INSERT INTO student (first_name, last_name, course) VALUES(?, ?, ?)", (first_name, last_name, course))

data = cursor.execute("SELECT * FROM student")

for i in data:
    for a in i:
        print(a)

connect.commit()
connect.close()


# Assignment 
# create student form, collect phone number (only 11 digits), first name, last name, email, Address, 
# Place of birth, State of origin,NIN (11 dgits)
# Nationality and add it to a database