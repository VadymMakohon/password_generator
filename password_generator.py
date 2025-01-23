import re
import secrets
import string

def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    # Define the possible character groups
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Ensure the total required characters do not exceed the password length
    total_constraints = nums + special_chars + uppercase + lowercase
    if total_constraints > length:
        raise ValueError("The sum of required character types exceeds the password length")

    
    password_parts = (
        [secrets.choice(digits) for _ in range(nums)] +
        [secrets.choice(symbols) for _ in range(special_chars)] +
        [secrets.choice(string.ascii_uppercase) for _ in range(uppercase)] +
        [secrets.choice(string.ascii_lowercase) for _ in range(lowercase)]
    )

    # Fill the rest of the password with random characters from all groups
    remaining_length = length - len(password_parts)
    all_characters = letters + digits + symbols
    password_parts.extend(secrets.choice(all_characters) for _ in range(remaining_length))

    # Shuffle the characters to avoid predictable patterns
    secrets.SystemRandom().shuffle(password_parts)

    # Join and return the password
    return ''.join(password_parts)

if __name__ == '__main__':
    try:
        new_password = generate_password(length=16, nums=2, special_chars=2, uppercase=2, lowercase=2)
        print('Generated password:', new_password)
    except ValueError as e:
        print(f"Error: {e}")
