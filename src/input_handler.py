from db_handler import *

def database_options():
    print("Welcome to the Password Manager!")
    while True:
        print("\nDatabase Menu:")
        print("1. Open existing database")
        print("2. Create new database")
        print("3. Delete existing database")
        print("0. Exit")

        choice = input("Enter your choice: ")
        
        if choice == '1':  # open existing database
            db_name = input("Enter the name of the database to open (with .key extension): ")
            pm = open_database(db_name)
            if pm and pm.verify_master_password():
                print(f"\n>Opened database: {db_name}")
                return pm  # Gebe das PasswordManager-Objekt zurück
        
        elif choice == '2':  # create new database
            db_name = input("Enter the name for the new database (with .key extension): ")
            pm = create_database(db_name)
            if pm:
                generate_key(db_name) # generate key for the new database
                pm.set_master_password() 
                print(f"\n>Created new database: {db_name}")
                return pm  # Gebe das PasswordManager-Objekt zurück
        
        elif choice == '3':  # delete database
            db_name = input("Enter the name of the database to delete (with .key extension): ")
            confirm = input(f"Are you sure you want to delete the database '{db_name}'? (yes/no): ")
            if confirm.lower() == 'yes':
                delete_database(db_name)
        
        elif choice == '0':  # exit
            print("Exiting the program.")
            exit()
        
        else:
            print("Invalid choice. Please try again.")

def get_user_choice():
    print("\nChoose an option:")
    print("1. View entries")
    print("2. Add entry")
    print("3. Delete entry")
    print("4. Delete all entries")
    print("5. Generate password")
    print("9. Exit to database menu")
    print("0. Exit")
    choice = input("Enter your choice: ")
    return choice

def get_entry_input():
    website = input("Enter the name of the website: ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    return website, username, password
