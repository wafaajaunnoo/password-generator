import random
import string

def generate_password():
    # Define the characters to be included in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password by selecting random characters from the defined set
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

length = int(input("Enter the desired length of the password: "))

password = generate_password()
print("Generated Password:", password)
