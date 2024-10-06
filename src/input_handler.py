import getpass

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
    password = getpass.getpass("Enter your password: ")
    return website, username, password