import sqlite3

user = input("Enter your ID Number\n >>")

# Connect to SQLite database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Check SQLite version
# cursor.execute('SELECT sqlite_version()')
# sqlite_version = cursor.fetchone()[0]
# print(f"SQLite Version: {sqlite_version}")

# Create a test table with a CHECK constraint
cursor.execute('''
    CREATE TABLE IF NOT EXISTS test_table(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        value TEXT CHECK (LENGTH(value) <= 5)
    )
''')

conn.commit()

# Function to insert a value and check for errors
def insert_value(val):
    try:
        cursor.execute('INSERT INTO test_table (value) VALUES (?)', (val,))
        conn.commit()
        print(f"Inserted: {val}")
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")

# Test inserting valid and invalid values
insert_value('12345')  # Should succeed
insert_value('123456')  # Should fail

# Close the connection
conn.close()

