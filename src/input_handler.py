def start_pw_manager():
    print("Welcome to the Password Manager!")
    print("Please choose an option:")
    print("1. Open an existing database")
    print("2. Create a new database")

    choice = input("Enter the number of your choice: ")

    if choice == '1':
        return "open"
    elif choice == '2':
        return "create"
    else:
        print("Invalid input, please choose '1' or '2'.\n")
        return start_pw_manager()

# ask for the name of the database
def get_database_name(action):
    if action == "open":
        db_name = input("Enter the name of the database to open (e.g., passwords.key): ")
    elif action == "create":
        db_name = input("Enter the name for the new database (e.g., passwords.key): ")
    else:
        raise ValueError("Invalid action specified.")
    return db_name
