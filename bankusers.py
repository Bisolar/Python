import sqlite3
first_name = str(input("Enter your first name \n >>>")).upper()
last_name = str(input("Enter your last name  \n >>> ")).upper()
email = str(input("Enter your email \n >>> ")).lower()
phone_num = int(input("Enter your phone number \n >>>"))

connection = sqlite3.connect('assessment.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS bankusers (
               id INTEGER PRIMARY KEY AUTOINCREMENT, first_name VARCHAR(20), last_name VARCHAR(20),
                email VARCHAR(20), phone_num INTEGER, account_num INTEGER)''')

# print(f"{first_name}, {last_name}, your  {email} {phone_num}, has been registered")
# cursor.execute("SELECT * FROM bankusers")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)
def add_data(first_name, last_name, email, phonenumber, account):
    cursor.execute("INSERT INTO bankusers (first_name, last_name, email, phone_num, account_num) VALUES (?, ?, ?, ?, ?)",
                (first_name, last_name, email, phone_num))
    connection.commit()
    print("Account Created")
    connection.close()

add_data(first_name, last_name, email, phone_num, phone_num)


# Research, create a standard calculator app




