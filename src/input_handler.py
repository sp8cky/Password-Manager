from db_handler import open_database, create_database, delete_database

def get_user_choice():
    print("\nChoose an option:")
    print("1. View entries")
    print("2. Add entry")
    print("3. Delete entry")
    print("4. Delete all entries")
    print("9. Exit to database menu")
    print("0. Exit")
    choice = input("Enter your choice: ")
    return choice

def get_entry_input():
    website = input("Enter the name of the website: ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    return website, username, password

def database_options():
    while True:
        print("\nDatabase Menu:")
        print("1. Open existing database")
        print("2. Create new database")
        print("3. Delete existing database")
        print("0. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            db_name = input("Enter the name of the existing database (with .key extension): ")
            connection = open_database(db_name)
            if connection:
                print(f"Opened database: {db_name}")
                return connection 
        
        elif choice == '2':
            db_name = input("Enter the name for the new database (with .key extension): ")
            connection = create_database(db_name)
            if connection:
                print(f"Created new database: {db_name}")
                return connection 
        
        elif choice == '3':
            db_name = input("Enter the name of the database to delete (with .key extension): ")
            delete_database(db_name) 
            
        elif choice == '0':
            print("Exiting the program.")
            exit()

        else:
            print("Invalid choice. Please try again.")
