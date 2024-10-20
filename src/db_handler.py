import os
from encryption_handler import *
from password_manager_class import PasswordManager

def open_database(db_name):
    if os.path.exists(db_name):
        pm = PasswordManager(db_name)
        pm.connect()
        return pm
    else:
        print("\n>Database does not exist.")
        return None

def create_database(db_name):
    if not db_name.endswith('.key'):
        print("\n>Please ensure the database name ends with .key.")
        return None
    pm = PasswordManager(db_name)
    pm.connect()
    pm.create_table()
    return pm

def delete_database(db_name):
    if os.path.exists(db_name):
        confirmation = input(f"Are you sure you want to delete the database '{db_name}'? (yes/no): ")
        if confirmation.lower() == 'yes':
            try:
                os.remove(db_name) 
                print("\n>Database deleted successfully!")
            except Exception as e:
                print(f"\n>Error deleting database: {e}")
        else:
            print("\n>Database deletion cancelled.")
    else:
        print("\n>Database does not exist.")

def display_entries(entries):
    print("\n>Stored entries (ID, Website, Username, Decrypted Password, Encrypted Password):")
    for index, entry in enumerate(entries):
        print(f"{index + 1}. {entry[1]}, {entry[2]}, {entry[3]}, {entry[4]}")

# Helper function to select an entry to delete
def select_entry_to_delete(entries):
    print("\n>Select an entry to delete:")
    for index, entry in enumerate(entries):
        print(f"{index + 1}. Website: {entry[1]}")
    entry_index = int(input("Enter the number of the entry to delete: ")) - 1
    return entry_index