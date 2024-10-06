from input_handler import start_pw_manager, get_database_name
from db_handler import open_database, create_database

def login(master_password):
    # Simulierter Login-Prozess
    input("Enter your master password: ")
    print("Login successful.\n")
    return True

def main_menu():
    print("Welcome to the main menu!")
    print("1. View entries")
    print("2. Add entry")
    print("3. Delete entry")
    print("4. Exit")

    choice = input("Enter the number of your choice: ")
    return choice

def main():
    action = start_pw_manager()
    db_name = get_database_name(action)

    if action == "open":
        open_database(db_name)
        print(f"Database '{db_name}' opened successfully.\n")

        if login("master_password"):  # Simulierter Login
            main_menu()

    elif action == "create":
        create_database(db_name)
        print(f"Database '{db_name}' created successfully.\n")

        main_menu()

if __name__ == "__main__":
    main()
