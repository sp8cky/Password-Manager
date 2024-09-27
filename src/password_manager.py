import os

from input_handler import get_user_choice, get_input
from encryption_handler import generate_key
from db_handler import create_table, add_entry, get_entries, delete_entry, delete_all_entries

def main():
    if not os.path.exists("secret.key"): # generate key if it doesn't exist
        generate_key() 
    create_table() # create table (if not exists)

    while True:
        choice = get_user_choice()

        if choice == '1': # view entries
            entries = get_entries()
            print("\nStored entries (Website, Username, Password):")
            for index, entry in enumerate(entries):
                print(f"{index + 1}. {entry[1]}, {entry[2]}, {entry[3]}")

        elif choice == '2': # qdd entry
            website, username, password = get_input()
            add_entry(website, username, password)
            print("Entry added successfully!")

        elif choice == '3': # delete entry
            entries = get_entries()
            if not entries:
                print("No entries to delete.")
                continue
            print("\nSelect an entry to delete:")
            for index, entry in enumerate(entries):
                print(f"{index + 1}. Website: {entry[1]}")

            entry_index = int(input("Enter the number of the entry to delete: ")) - 1
            if 0 <= entry_index < len(entries):
                delete_entry(entries[entry_index][0])  # using the entry ID for deletion
                print("Entry deleted successfully!")
            else:
                print("Invalid entry number.")

        elif choice == '4': # delete all entries
            delete_all_entries()
            print("All entries deleted successfully!")

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
