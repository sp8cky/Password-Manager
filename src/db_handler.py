import sqlite3
from encryption_handler import encrypt_password, decrypt_password

# Create database connection
def connect():
    connection = sqlite3.connect('password_manager.key')
    return connection

# Create table (if not exists)
def create_table():
    connection = connect()
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            website TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    connection.commit()
    connection.close()

# Add new entry to the database
def add_entry(website, username, password):
    encrypted_password = encrypt_password(password)
    connection = connect()
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO entries (website, username, password) VALUES (?, ?, ?)
    ''', (website, username, encrypted_password))
    connection.commit()
    connection.close()

# Get all entries from the database
def get_entries():
    connection = connect()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM entries')
    entries = cursor.fetchall()
    connection.close()
    
    # decrypt password before returning
    decrypted_entries = []
    for entry in entries:
        decrypted_password = decrypt_password(entry[3])
        decrypted_entries.append((entry[0], entry[1], entry[2], decrypted_password))

        print(f"Website: {entry[1]}, Username: {entry[2]}, Password: {decrypted_password}") # test print

    return decrypted_entries

# Delete entry from the database using the entry ID
def delete_entry(entry_id):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute('DELETE FROM entries WHERE id = ?', (entry_id,))
    connection.commit()
    connection.close()

# Delete all entries from the database
def delete_all_entries():
    connection = connect()
    cursor = connection.cursor()
    cursor.execute('DELETE FROM entries')
    connection.commit()
    connection.close()