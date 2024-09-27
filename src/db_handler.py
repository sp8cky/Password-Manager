import sqlite3

# create database connection
def connect():
    connection = sqlite3.connect('password_manager.key')
    return connection

# create table (if not exists)
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

# add new entry to the database
def add_entry(website, username, password):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO entries (website, username, password) VALUES (?, ?, ?)
    ''', (website, username, password))
    connection.commit()
    connection.close()

# get all entries from the database
def get_entries():
    connection = connect()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM entries')
    entries = cursor.fetchall()
    connection.close()
    return entries

# delete entry from the database using the entry ID
def delete_entry(entry_id):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute('DELETE FROM entries WHERE id = ?', (entry_id,))
    connection.commit()
    connection.close()

# delete all entries from the database
def delete_all_entries():
    connection = connect()
    cursor = connection.cursor()
    cursor.execute('DELETE FROM entries')
    connection.commit()
    connection.close()