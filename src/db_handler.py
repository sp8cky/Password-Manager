import sqlite3
import os

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


# Helper function to display entries
def display_entries(entries):
    print("\nStored entries (Website, Username, Password):")
    for index, entry in enumerate(entries):
        print(f"{index + 1}. {entry[1]}, {entry[2]}, {entry[3]}")

# Helper function to select an entry to delete
def select_entry_to_delete(entries):
    print("\nSelect an entry to delete:")
    for index, entry in enumerate(entries):
        print(f"{index + 1}. Website: {entry[1]}")
    entry_index = int(input("Enter the number of the entry to delete: ")) - 1
    return entry_index

# delete the database file
def delete_database(db_name):
    if os.path.exists(db_name):
        confirmation = input(f"Are you sure you want to delete the database '{db_name}'? (yes/no): ")
        if confirmation.lower() == 'yes':
            os.remove(db_name)
            print("Database deleted successfully!")
        else:
            print("Database deletion cancelled.")
    else:
        print("Database does not exist.")
