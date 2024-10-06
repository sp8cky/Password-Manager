from input_handler import get_user_choice, get_input, database_options
from db_handler import create_table, add_entry, get_entries, delete_entry, delete_all_entries, display_entries, select_entry_to_delete
import os

def main():
    connection = None
    while connection is None:
        connection = database_options()
    
    create_table(connection)  # create table (if not exists)
    
    while True:
        choice = get_user_choice()

        if choice == '1':  # View entries
            entries = get_entries(connection)
            display_entries(entries)

        elif choice == '2':  # Add entry
            website, username, password = get_input()
            add_entry(connection, website, username, password)
            print("Entry added successfully!")

        elif choice == '3':  # Delete entry
            entries = get_entries(connection)
            if not entries:
                print("No entries to delete.")
                continue
            entry_index = select_entry_to_delete(entries)
            if 0 <= entry_index < len(entries):
                delete_entry(connection, entries[entry_index][0]) 
                print("Entry deleted successfully!")
            else:
                print("Invalid entry number.")

        elif choice == '4':  # Delete all entries
            delete_all_entries(connection)
            print("All entries deleted successfully!")
        
        elif choice == '9': # exit to database menu
            print("Back to database menu.")
            database_options()
            
        elif choice == '0': # exit
            print("Exiting the program.")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
