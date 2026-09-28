import random
import string


def generate_password(length=12):

    if length < 8:
        print("Password length must be at least 8.")

    uppercase = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    lowercase = random.choice("abcdefghijklmnopqrstuvwxyz")
    digit = random.choice("0123456789")
    special = random.choice("!@#$%^&*()_+")

    characters = uppercase + lowercase + digit + special

    all_characters = (
        string.ascii_letters
        + string.digits
        + "!@#$%^&*()_+"
    )

    while len(characters) < length:
        characters += random.choice(all_characters)

    password = list(characters)
    random.shuffle(password)

    return "".join(password)