from .password_checker import analyze_password
from .password_generator import generate_password
from .recommendations import get_recommendations
from .password_validator import validate_password
from .security_report import display_report


def check_password():
    password = input("Enter your password: ")

    if password == "":
        print("Password cannot be empty.")
        return

    result = analyze_password(password)
    display_report(password, result)

    recommendations = get_recommendations(result)

    if recommendations:
        print("\nRecommendations:")
        for item in recommendations:
            print("-", item)


def create_password():
    length = input("Enter password length (minimum 8): ")

    if length.isdigit():
        length = int(length)

        if length < 8:
            print("Length must be at least 8.")
            return

        password = generate_password(length)

        print("\nGenerated password:", password)

        result = analyze_password(password)

        print("Generated password score:", result["score"], "/5")
        print("Strength:", result["strength"])

    else:
        print("Please enter a valid number.")


def show_recommendations():
    password = input("Enter your password: ")

    if not password:
        print("Password cannot be empty.")
        return

    result = analyze_password(password)
    recommendations = get_recommendations(result)

    if recommendations:
        print("\nRecommendations:")
        for item in recommendations:
            print("-", item)
    else:
        print("No recommendations. Your password meets all basic requirements.")


def validate():
    password = input("Enter your password: ")

    if validate_password(password):
        print("Password Status: VALID")
    else:
        print("Password Status: INVALID")


def main():
    while True:
        print("\n===================================")
        print("      PASSWORD SECURITY TOOL")
        print("===================================")
        print("1. Check Password Strength")
        print("2. Generate Password")
        print("3. Get Recommendations")
        print("4. Validate Password")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_password()
        elif choice == "2":
            create_password()
        elif choice == "3":
            show_recommendations()
        elif choice == "4":
            validate()
        elif choice == "5":
            print("Thank you for using Password Security Tool!")
            break
        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()