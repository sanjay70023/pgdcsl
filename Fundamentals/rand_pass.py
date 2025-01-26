# Write a Python script to generate a random password with customizable length and 
# complexity, including uppercase, lowercase, numbers, and special characters.


import random
import string

def generate_password(length=12, include_uppercase=True, include_numbers=True, include_special_chars=True):
    if length < 4:
        raise ValueError("Password length must be at least 4 to include all character types.")

    # Define character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase else ""
    numbers = string.digits if include_numbers else ""
    special_chars = string.punctuation if include_special_chars else ""

    # Ensure at least one character from each selected pool
    password = [
        random.choice(lowercase),
        random.choice(uppercase) if include_uppercase else "",
        random.choice(numbers) if include_numbers else "",
        random.choice(special_chars) if include_special_chars else ""
    ]

    # Fill the rest of the password length with random characters from all pools
    all_chars = lowercase + uppercase + numbers + special_chars
    if not all_chars:
        raise ValueError("No character pools selected for password generation.")
    
    password += random.choices(all_chars, k=length - len(password))

    # Shuffle the password to randomize the character order
    random.shuffle(password)
    
    return ''.join(password)

# Example usage
length = int(input("Enter password length: "))
include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
include_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

password = generate_password(length, include_uppercase, include_numbers, include_special_chars)
print(f"Generated Password: {password}")
