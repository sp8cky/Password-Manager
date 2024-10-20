import os
from password_manager_class import PasswordManager
from encryption_handler import *

# opens an existing database
def open_database(db_name):
    if os.path.exists(db_name):
        pm = PasswordManager(db_name)
        pm.connect()
        return pm
    else:
        print("\n>Database does not exist.")
        return None

# creates a new database with .key extension
def create_database(db_name):
    if not db_name.endswith('.key'):
        print("\n>Please ensure the database name ends with .key.")
        return None
    pm = PasswordManager(db_name)
    pm.connect()
    pm.create_table()
    return pm

# deletes an existing database
def delete_database(db_name):
    pm = PasswordManager(db_name)
    pm.connect()
    if os.path.exists(db_name):
        try:
            if pm.connection: # close the connection if it is open
                pm.connection.close()
            os.remove(db_name) 
            print("\n>Database deleted successfully!")

            # delete the corresponding secret file
            secret_file_name = f"secret-{db_name}"
            if os.path.exists(secret_file_name):
                os.remove(secret_file_name)
                print(f"\n>Secret file '{secret_file_name}' deleted successfully!")
            else:
                print(f"\n>Secret file '{secret_file_name}' does not exist.")

        except Exception as e:
            print(f"\n>Error deleting database: {e}")
    else:
        print("\n>Database does not exist.")

# add entry including webiste, username and password to the database
def add_entry(pm, website, username, password):
    try:
        encrypted_password = encrypt_password(password, pm.db_name) # encrypt the password
        with pm.connection:
            cursor = pm.connection.cursor()
            cursor.execute(''' 
                INSERT INTO entries (website, username, password) VALUES (?, ?, ?)
            ''', (website, username, encrypted_password))
    except sqlite3.Error as e:
        print(f"\n>Error adding entry: {e}")

# displays the stored entries
def display_entries(entries):
    print("\n>Stored entries (ID, Website, Username, Decrypted Password, Encrypted Password):")
    for index, entry in enumerate(entries):
        print(f"{index + 1}. {entry[1]}, {entry[2]}, {entry[3]}, {entry[4]}")

# delete one entry by id from the database
def delete_entry(pm, entry_id):
    try:
        with pm.connection:
            cursor = pm.connection.cursor()
            cursor.execute('DELETE FROM entries WHERE id = ?', (entry_id,))
    except sqlite3.Error as e:
        print(f"\n>Error deleting entry: {e}")

# Helper function to select an entry to delete
def select_entry_to_delete(entries):
    print("\n>Select an entry to delete:")
    for index, entry in enumerate(entries):
        print(f"{index + 1}. Website: {entry[1]}")
    entry_index = int(input("Enter the number of the entry to delete: ")) - 1
    return entry_index

# delete all entries from the database
def delete_all_entries(pm):
    try:
        with pm.connection:
            cursor = pm.connection.cursor()
            cursor.execute('DELETE FROM entries')
    except sqlite3.Error as e:
        print(f"\n>Error deleting all entries: {e}")