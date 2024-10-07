from input_handler import *
from db_handler import *
from encryption_handler import *
import os

def main():
    connection = None
    while connection is None:
        connection = database_options()
    
    # interaction loop
    while True:
        choice = get_user_choice()

        if choice == '1':  # View entries
            entries = get_entries(connection)
            display_entries(entries)

        elif choice == '2':  # Add entry
            website, username, password = get_entry_input()
            add_entry(connection, website, username, password)
            print("\n>Entry added successfully!")

        elif choice == '3':  # Delete entry
            entries = get_entries(connection)
            if not entries:
                print("\n>No entries to delete.")
                continue
            entry_index = select_entry_to_delete(entries)
            if 0 <= entry_index < len(entries):
                delete_entry(connection, entries[entry_index][0]) 
                print("\n>Entry deleted successfully!")
            else:
                print("\n>Invalid entry number.")

        elif choice == '4':  # Delete all entries
            delete_all_entries(connection)
            print("\n>All entries deleted successfully!")

        elif choice == '5':  
            length = int(input("Enter the length of the password (minimum 8): "))
            if length < 8:
                print("\n>Password length should be at least 8.")
                continue
            generated_password = generate_password(length)
            print(f"\n>Generated password: {generated_password}")
        
        elif choice == '9': # exit to database menu
            print("Back to database menu.")
            database_options()
            
        elif choice == '0': # exit
            print("Exiting the program.")
            exit()
            
        else:
            print("\n>Invalid choice. Please try again.")

if __name__ == "__main__":
    generate_key()
    main()
    # Beispiel zur manuellen Überprüfung
    """key = Fernet.generate_key()
    f = Fernet(key)
    password = "mein_passwort"
    encrypted_password = f.encrypt(password.encode())
    decrypted_password = f.decrypt(encrypted_password).decode()
    print(decrypted_password)  # sollte "mein_passwort" ausgeben"""
    
