import sqlite3

first_name = input("Enter your First Name\n>>")
last_name = input("Enter your Last Name\n>>")
email = input("Enter your Email\n>>")
address = input("Enter your Address\n>>")
place_of_birth = input("Enter your Place of birth\n>>")
state_of_origin = input("Enter your State of Origin\n>>")
nationality = input("Enter your Nationality\n>>")
phone_number = input("Enter your Phone Number\n>>")
nin = input("Enter your National Identification Number\n>>")

connect = sqlite3.connect('studentinfo.db')
cursor = connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS studentform(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               first_name TEXT,
               last_name TEXT,
               email TEXT,
               address TEXT,
               place_of_birth TEXT,
               state_of_origin TEXT,
               nationality TEXT,
               phone_number TEXT CHECK (LENGTH(phone_number) <= 11),
               NIN TEXT CHECK (LENGTH(NIN) <= 11))''')

cursor.execute("INSERT INTO studentform(first_name, last_name, email, address, place_of_birth, state_of_origin, nationality, phone_number, nin) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (first_name, last_name, email, address, place_of_birth, state_of_origin, nationality, phone_number, nin))

connect.commit()
connect.close()

# Assignment 
# create student form, collect phone number (only 11 digits), first name, last name, email, Address, 
# Place of birth, State of origin,NIN (11 dgits)
# Nationality and add it to a database