import secrets, string, bcrypt
from cryptography.fernet import Fernet

# generate a pseudo-random password with length greater 7
def generate_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

# generates a new Fernet key and saves it to a file named to the database name
def generate_key(db_name):
    key = Fernet.generate_key()
    key_filename = f"secret-{db_name}" # create a key file based on the database name
    with open(key_filename, "wb") as key_file:
        key_file.write(key)
    return key

# loads the secret key file from the current directory
def load_key(db_name):
    key_filename = f"secret-{db_name}"
    key = open(key_filename, "rb").read()  # Schlüssel laden
    return key

# encrypts the password using the loaded key
def encrypt_password(password, db_name):
    key = load_key(db_name)
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password

# decrypts the encrypted password using the loaded key
def decrypt_password(encrypted_password, db_name):
    key = load_key(db_name)
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
