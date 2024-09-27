import getpass
from encryption_handler import generate_password

def get_user_choice():
    print("\nChoose an option:")
    print("1. View entries")
    print("2. Add entry <website, username (pseudogenerated) passwort>)")
    print("3. Delete entry")
    print("4. Delete all entries")
    print("5. Get a pseudogenerated passwort")
    print("6. Exit")

    choice = input("Enter your choice (1-5): ")
    print("\n---------------------------------------------")
    return choice

def get_input():
    website = input("Enter the name of the website: ")
    username = input("Enter your username: ")
    choice = input("Would you like to (1) enter your own password or (2) generate a secure password? Enter 1 or 2: ")

    if choice == '1':
        password = getpass.getpass("Enter your password: ")
    elif choice == '2':
        password_length = int(input("Enter the desired password length (minimum 8): "))
        if password_length < 8:
            print("Invalid choice. Please start again.")
            return get_input()
        password = generate_password(password_length)  
    else:
        print("Invalid choice. Please enter 1 or 2.")
        return get_input()
    print(f"Your password: {password}") 

    return website, username, password