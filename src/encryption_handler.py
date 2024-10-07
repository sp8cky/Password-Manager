import secrets, string, bcrypt
from cryptography.fernet import Fernet

# generate a pseudo-random password with length greater 7
def generate_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

# generates a new Fernet key and saves it to a file named to the database name
def generate_key():
    key = Fernet.generate_key()
    key_filename = "secret.key" 
    with open(key_filename, "wb") as key_file:
        key_file.write(key)
    return key

# loads the secret key file from the current directory
def load_key():
    key_filename = "secret.key"
    return open(key_filename, "rb").read()

# encrypts the password using the loaded key
def encrypt_password(password):
    key = load_key()
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password

# decrypts the encrypted password using the loaded key
def decrypt_password(encrypted_password):
    key = load_key()
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password).decode()
    return decrypted_password

# hash the password using bcrypt
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password

# check if the user input password matches the hashed password
def check_password(hashed_password, user_input_password):
    return bcrypt.checkpw(user_input_password.encode(), hashed_password)

# set the master password and store it in the database
def set_master_password(connection):
    while True:
        master_password = input("Set your master password: ")
        confirm_password = input("Confirm your master password: ")
        
        if master_password == confirm_password:
            hashed_password = hash_password(master_password)
            with connection:
                cursor = connection.cursor()
                cursor.execute('INSERT INTO master (master_password) VALUES (?)', (hashed_password,))
            print("Master password set successfully!")
            break
        else:
            print("Passwords do not match. Try again.")

# verify the master password when the user tries to access the database, exit if too many (3) failed attempts
def verify_master_password(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT master_password FROM master WHERE id = 1')
    stored_hashed_password = cursor.fetchone()[0]

    attempts = 3
    while attempts > 0:
        user_password = input("Enter the master password: ")
        
        if check_password(stored_hashed_password, user_password):
            print("Master password verified!")
            return True
        else:
            attempts -= 1
            print(f"Incorrect password. {attempts} attempts left.")
    
    print("Too many failed attempts. Exiting.")
    exit()