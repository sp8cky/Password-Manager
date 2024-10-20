import sqlite3, os
from encryption_handler import *

class PasswordManager:
    def __init__(self, db_name=None):
        self.db_name = db_name
        self.connection = None

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_name)
        except sqlite3.Error as e:
            print(f"\n>Error connecting to database: {e}")
            return None

    def create_table(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(''' 
                CREATE TABLE IF NOT EXISTS entries (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    website TEXT NOT NULL,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL
                )
            ''')
            cursor.execute(''' 
                CREATE TABLE IF NOT EXISTS master (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    master_password TEXT NOT NULL
                )
            ''')

    ## add entry including webiste, username and password to the database
    def add_entry(self, website, username, password):
        try:
            encrypted_password = encrypt_password(password, self.db_name)  # encrypt the password
            with self.connection:
                cursor = self.connection.cursor()
                cursor.execute(''' 
                    INSERT INTO entries (website, username, password) VALUES (?, ?, ?)
                ''', (website, username, encrypted_password))
        except sqlite3.Error as e:
            print(f"\n>Error adding entry: {e}")

    # get all entries from the database
    def get_entries(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute('SELECT * FROM entries')
            entries = cursor.fetchall()
            for i in range(len(entries)): # decrypt the passwords before returning
                encrypted_password = entries[i][3]
                decrypted_password = decrypt_password(encrypted_password, self.db_name)
                entries[i] = (
                    entries[i][0], # ID
                    entries[i][1], # Website
                    entries[i][2], # Username
                    decrypted_password, # Decrypted password TODO: change
                    encrypted_password # Encrypted password TODO: change
                )
            return entries
        except sqlite3.Error as e:
            print(f"\n>Error retrieving entries: {e}")
            return []

    # delete one entry by id from the database
    def delete_entry(self, entry_id):
        try:
            with self.connection:
                cursor = self.connection.cursor()
                cursor.execute('DELETE FROM entries WHERE id = ?', (entry_id,))
        except sqlite3.Error as e:
            print(f"\n>Error deleting entry: {e}")

    # delete all entries from the database
    def delete_all_entries(self):
        try:
            with self.connection:
                cursor = self.connection.cursor()
                cursor.execute('DELETE FROM entries')
        except sqlite3.Error as e:
            print(f"\n>Error deleting all entries: {e}")

    # set the master password for a new database
    def set_master_password(self):
        while True:
            master_password = input("Set your master password: ")
            confirm_password = input("Confirm your master password: ")
            
            if master_password == confirm_password:
                hashed_password = hash_password(master_password)
                with self.connection:
                    cursor = self.connection.cursor()
                    cursor.execute('INSERT INTO master (master_password) VALUES (?)', (hashed_password,))
                print("Master password set successfully!")
                break
            else:
                print("Passwords do not match. Try again.")
    # verify with three attempts the master password before allowing access to the database
    def verify_master_password(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT master_password FROM master WHERE id = 1')
        stored_hashed_password = cursor.fetchone()[0]

        attempts = 3
        while attempts > 0:
            user_password = input("Enter the master password: ")
            
            if check_password(stored_hashed_password, user_password):
                print("Master password verified!")
                return True
            else:
                attempts -= 1
                print(f"Incorrect password. {attempts} attempts left.")
        
        print("Too many failed attempts. Exiting.")
        exit()
