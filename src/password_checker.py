def analyze_password(password):

    is_length = len(password) >= 8
    is_upper = any(ch.isupper() for ch in password)
    is_lower = any(ch.islower() for ch in password)
    is_digit = any(ch.isdigit() for ch in password)
    is_special = any(not ch.isalnum() for ch in password)

    score = sum([
        is_length,
        is_upper,
        is_lower,
        is_digit,
        is_special
    ])

    if score <= 2:
        strength = "WEAK"
    elif score == 3:
        strength = "MEDIUM"
    elif score == 4:
        strength = "STRONG"
    else:
        strength = "VERY STRONG"

    return {
        "length": is_length,
        "uppercase": is_upper,
        "lowercase": is_lower,
        "digit": is_digit,
        "special": is_special,
        "score": score,
        "strength": strength
    }