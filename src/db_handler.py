import sqlite3
import os

# create database connection
def connect(db_name):
    try:
        connection = sqlite3.connect(db_name)
        return connection
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

# create table (if not exists)
def create_table(connection):
    with connection:
        cursor = connection.cursor()
        cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS entries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                website TEXT NOT NULL,
                username TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')

# Open the existing database file
def open_database(db_name):
    if os.path.exists(db_name):
        return connect(db_name)
    else:
        print("Database does not exist.")
        return None

# Create a new database file
def create_database(db_name):
    if not db_name.endswith('.key'):
        print("Please ensure the database name ends with .key.")
        return None
    connection = sqlite3.connect(db_name)
    create_table(connection)
    return connection


# add new entry
def add_entry(connection, website, username, password):
    try:
        with connection:
            cursor = connection.cursor()
            cursor.execute(''' 
                INSERT INTO entries (website, username, password) VALUES (?, ?, ?)
            ''', (website, username, password))
    except sqlite3.Error as e:
        print(f"Error adding entry: {e}")

# get all entries from the database
def get_entries(connection):
    try:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM entries')
        entries = cursor.fetchall()
        return entries
    except sqlite3.Error as e:
        print(f"Error retrieving entries: {e}")
        return []

# Helper function to display entries
def display_entries(entries):
    print("\nStored entries (Website, Username, Password):")
    for index, entry in enumerate(entries):
        print(f"{index + 1}. {entry[1]}, {entry[2]}, {entry[3]}")


# delete entry from the database using the entry ID
def delete_entry(connection, entry_id):
    try:
        with connection:
            cursor = connection.cursor()
            cursor.execute('DELETE FROM entries WHERE id = ?', (entry_id,))
    except sqlite3.Error as e:
        print(f"Error deleting entry: {e}")


# Helper function to select an entry to delete
def select_entry_to_delete(entries):
    print("\nSelect an entry to delete:")
    for index, entry in enumerate(entries):
        print(f"{index + 1}. Website: {entry[1]}")
    entry_index = int(input("Enter the number of the entry to delete: ")) - 1
    return entry_index


# delete all entries from the database
def delete_all_entries(connection):
    try:
        with connection:
            cursor = connection.cursor()
            cursor.execute('DELETE FROM entries')
    except sqlite3.Error as e:
        print(f"Error deleting all entries: {e}")
    

# delete the database file
def delete_database(db_name):
    if os.path.exists(db_name):
        confirmation = input(f"Are you sure you want to delete the database '{db_name}'? (yes/no): ")
        if confirmation.lower() == 'yes':
            try:
                os.remove(db_name)
                print("Database deleted successfully!")
            except Exception as e:
                print(f"Error deleting database: {e}")
        else:
            print("Database deletion cancelled.")
    else:
        print("Database does not exist.")


