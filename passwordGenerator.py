import random
import string

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")
    
    # Ensure password has at least one of each type
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice("!@#$%^&*()")
    ]
    
    # Fill the rest randomly
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    password += random.choices(characters, k=length - 4)
    
    random.shuffle(password)
    return "".join(password)

if __name__ == "__main__":
    length = int(input("Enter password length: "))
    print("Generated Password:", generate_password(length))
