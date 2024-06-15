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

# data = cursor.execute("SELECT * FROM student")

# for i in data:
#     for a in i:
#         print(a)

# cursor.execute(("UPDATE student SET last_name = ?, course = ?, WHEE id = 4"), (first_name, last_name, course))
# cursor.execute(("DELETE FROM student WHERE id = ?"), (2,))
data = cursor.execute(("SELECT * FROM student WHERE id = ?"), (3,)).fetchall()

connect.commit()
connect.close()


