def display_report(password, result):

    print("\n========== PASSWORD SECURITY REPORT ==========")
    print("Password:", "*" * len(password))

    if result["length"]:
        print("Length requirement :", "PASS")
    else:
        print("Length requirement :", "FAIL (Minimum 8 characters)")

    if result["uppercase"]:
        print("Uppercase letter   :", "PASS")
    else:
        print("Uppercase letter   :", "FAIL")

    if result["lowercase"]:
        print("Lowercase letter   :", "PASS")
    else:
        print("Lowercase letter   :", "FAIL")

    if result["digit"]:
        print("Digit              :", "PASS")
    else:
        print("Digit              :", "FAIL")

    if result["special"]:
        print("Special character  :", "PASS")
    else:
        print("Special character  :", "FAIL")

    print("----------------------------------------------")
    print("Score              :", result["score"], "/5")
    print("Strength           :", result["strength"])
    print("==============================================")