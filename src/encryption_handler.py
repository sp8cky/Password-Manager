import secrets, string
from cryptography.fernet import Fernet

# generate a pseudo-random password with length greater 7
def generate_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

# generates a new Fernet key and saves it to a file <secret.key>
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    return key

# loads the secret key from the current directory
def load_key():
    return open("secret.key", "rb").read()

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