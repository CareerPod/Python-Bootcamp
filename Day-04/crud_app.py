import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
''')
conn.commit()

# Function to create a new user
def create_user(name, age):
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
    conn.commit()
    print(f'User {name} added successfully.')

# Function to read all users
def read_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    print('All users:')
    for user in users:
        print(user)

# Function to update a user
def update_user(user_id, name, age):
    cursor.execute('UPDATE users SET name = ?, age = ? WHERE id = ?', (name, age, user_id))
    conn.commit()
    print(f'User with ID {user_id} updated successfully.')

# Function to delete a user
def delete_user(user_id):
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    print(f'User with ID {user_id} deleted successfully.')

# Create users
create_user('Alice', 30)
create_user('Bob', 25)

# Read users
read_users()

# Update a user
update_user(1, 'Alice Smith', 31)

# Read users again to see the update
read_users()

# Delete a user
delete_user(2)

# Read users again to see the deletion
read_users()

# Close the connection
conn.close()
