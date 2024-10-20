import os
from input_handler import *
from encryption_handler import *

# includes the mainloop of the program
def main():
    pm = None
    while pm is None:  # user enters the database name
        pm = database_options()

    # interaction loop
    while True:
        choice = get_user_choice()

        if choice == '1': # view entries
            entries = pm.get_entries()
            display_entries(entries)

        elif choice == '2': # add entry
            website, username, password = get_entry_input()
            pm.add_entry(website, username, password)
            print("\n>Entry added successfully!")

        elif choice == '3': # delete entry
            entries = pm.get_entries()
            if not entries:
                print("\n>No entries to delete.")
                continue
            entry_index = select_entry_to_delete(entries)
            if 0 <= entry_index < len(entries):
                pm.delete_entry(entries[entry_index][0]) 
                print("\n>Entry deleted successfully!")
            else:
                print("\n>Invalid entry number.")

        elif choice == '4': # delete all entries
            pm.delete_all_entries()
            print("\n>All entries deleted successfully!")

        elif choice == '5': # generate password
            length = int(input("Enter the length of the password (minimum 8): "))
            if length < 8:
                print("\n>Password length should be at least 8.")
                continue
            generated_password = generate_password(length)
            print(f"\n>Generated password: {generated_password}")
        
        elif choice == '9': # exit to database menu
            if pm.connection:
                pm.connection.close() # close the connection
            print("Back to database menu.")
            pm = database_options()
            
        elif choice == '0':  # exit
            print("Exiting the program.")
            if pm.connection:
                pm.connection.close() # close the connection
            exit()
            
        else:
            print("\n>Invalid choice. Please try again.")

if __name__ == "__main__":
    main()