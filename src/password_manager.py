from input_handler import get_user_choice, get_input
from db_handler import create_table, add_entry, get_entries, delete_entry, delete_all_entries, display_entries, select_entry_to_delete, delete_database
import os


def database_options():
    while True:
        print("\nDatabase Options:")
        print("1. Open existing database")
        print("2. Create new database")
        print("3. Delete existing database")
        print("4. Exit to main menu")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            db_name = input("Enter the name of the existing database (with .key extension): ")
            if os.path.exists(db_name):
                print(f"Opened database: {db_name}")
                return db_name
            else:
                print("Database does not exist. Please try again.")
        
        elif choice == '2':
            db_name = input("Enter the name for the new database (with .key extension): ")
            if db_name.endswith('.key'):
                open(db_name, 'w').close()  # Create an empty file
                print(f"Created new database: {db_name}")
                return db_name
            else:
                print("Please ensure the database name ends with .key.")
        
        elif choice == '3':
            db_name = input("Enter the name of the database to delete (with .key extension): ")
            delete_database(db_name)
        
        elif choice == '4':
            print("Exiting to main menu.")
            return None

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


def main():
    db_name = None
    while db_name is None:
        db_name = database_options()
    
    create_table()  # create table (if not exists)
    
    while True:
        choice = get_user_choice()

        if choice == '1':  # View entries
            entries = get_entries()
            display_entries(entries)

        elif choice == '2':  # Add entry
            website, username, password = get_input()
            add_entry(website, username, password)
            print("Entry added successfully!")

        elif choice == '3':  # Delete entry
            entries = get_entries()
            if not entries:
                print("No entries to delete.")
                continue
            entry_index = select_entry_to_delete(entries)
            if 0 <= entry_index < len(entries):
                delete_entry(entries[entry_index][0])  # Using the entry ID for deletion
                print("Entry deleted successfully!")
            else:
                print("Invalid entry number.")

        elif choice == '4':  # Delete all entries
            delete_all_entries()
            print("All entries deleted successfully!")
            
        elif choice == '5':
            print("Exiting the program.")
            break
            
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
