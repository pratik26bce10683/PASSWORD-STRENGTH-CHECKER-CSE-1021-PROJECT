def validate_password(password):

    if len(password) < 8:
        return False

    if not any(ch.isupper() for ch in password):
        return False

    if not any(ch.islower() for ch in password):
        return False

    if not any(ch.isdigit() for ch in password):
        return False

    if not any(not ch.isalnum() for ch in password):
        return False

    return True