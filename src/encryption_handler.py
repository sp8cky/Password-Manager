import secrets
import string

# generate a pseudo-random password with length greater 7
def generate_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    
    return password