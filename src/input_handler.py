from db_handler import open_or_create_database, delete_database

def get_user_choice():
    print("\nChoose an option:")
    print("1. View entries")
    print("2. Add entry")
    print("3. Delete entry")
    print("4. Delete all entries")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    return choice

def get_input():
    website = input("Enter the name of the website: ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    return website, username, password

def database_options():
    while True:
        print("\nDatabase Options:")
        print("1. Open existing database")
        print("2. Create new database")
        print("3. Delete existing database")
        print("4. Exit to main menu")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            db_name = input("Enter the name of the existing database (with .key extension): ")
            connection = open_or_create_database(db_name)
            if connection:
                print(f"Opened database: {db_name}")
                return connection  # Rückgabe der Verbindung
        
        elif choice == '2':
            db_name = input("Enter the name for the new database (with .key extension): ")
            connection = open_or_create_database(db_name)
            if connection:
                print(f"Created new database: {db_name}")
                return connection  # Rückgabe der Verbindung
        
        elif choice == '3':
            db_name = input("Enter the name of the database to delete (with .key extension): ")
            delete_database(db_name)  # Aufruf der Löschfunktion
            
        elif choice == '4':
            print("Exiting to main menu.")
            return None

        else:
            print("Invalid choice. Please try again.")
