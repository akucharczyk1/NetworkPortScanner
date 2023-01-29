import secrets
import string

def generate_password(length, include_special=True):
    """Generates a cryptographically secure random password of the specified length"""
    characters = string.ascii_letters + string.digits
    if include_special:
        characters += string.punctuation
    password = "".join(secrets.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    length = int(input("Enter the desired password length: "))
    include_special = input("Include special characters? (y/n): ").lower() == "y"
    password = generate_password(length, include_special)
    print(password)