import random
import string

def validate_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."

    has_digit = False
    has_symbol = False
    has_letter = False

    for char in password:
        if char.isdigit():
            has_digit = True
        if not char.isalnum():
            has_symbol = True
        if char.isalpha():
            has_letter = True

    if not has_digit:
        return False, "Password must contain at least one digit."
    if not has_letter:
        return False, "Password must contain at least one letter."
    if not has_symbol:
        return False, "Password must contain at least one symbol."

    return True, "Password is valid"

def validate_ip(ip):
    ip = ip.strip()

    if ip.count('.') != 3:
        return False, "IP address must contain three dots."

    parts = ip.split('.')

    if len(parts) != 4:
        return False, "IP address must have four parts"

    for part in parts:
        if not part.isdigit():
            return False, "Each part of the IP address must be a number."

        num = int(part)
        if num < 0 or num > 255:
            return False, "Each part of the IP address must be between 0 and 255"

    return True, "IP address is valid"

def generate_password():
    length = random.randint(10, 16)

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""
    password += random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)

    while len(password) < length:
        password += random.choice(characters)

    password_list = list(password)
    random.shuffle(password_list)

    return ''.join(password_list)