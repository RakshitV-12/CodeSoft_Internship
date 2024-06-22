# Created by - Rakshit Verma
# Here is the Python code to generate a strong password 

import string
import random

# Prompt the user to specify the desired length of the password
password_length = int(input("Enter the desired length of the password: "))

# Define possible characters for the password
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password using a combination of random characters
password = ''.join(random.choice(characters) for i in range(password_length))

# Display the generated password
print("Your generated password is:", password)
    
    
