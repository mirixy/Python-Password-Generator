#Import Bibliothek
from hashlib import pbkdf2_hmac

# Ideal for Web Passwords
small_letters = list('abcdefghijklmnopqrstuvwxyz')
big_letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
numbers = list('0123456789')
special_characters = list('#!"$%&/{}[]()=-_+*<>;:.')
password_characters = small_letters + big_letters + numbers + special_characters
salt = "pepper"

# Function to generate Password
def convert_bytes_to_password(hashed_bytes, length):
    number = int.from_bytes(hashed_bytes, byteorder='big')
    password = ''
    while number > 0 and len(password) < length:
        password = password + password_characters[number % len(password_characters)]
        number = number // len(password_characters)
    return password


# First Inputs
master_password = input("Masterpassword: ")

domain = input("Domain: ")
# Check if a domain is entered
while len(domain) < 1:
    print("Please type in a domain to generate your password ")
    domain = input("Domain: ")
# encode
hash_string = domain + master_password
hashed_bytes = pbkdf2_hmac('sha512', hash_string.encode('utf-8'), salt.encode('utf-8'), 4096)
# Finaly print password using the Function we defined
print ('Password: ' + convert_bytes_to_password(hashed_bytes, 10))



