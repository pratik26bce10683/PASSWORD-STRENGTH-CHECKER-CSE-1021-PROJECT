# Password Security Tool - Design

## System Design

The Password Security Tool is divided into separate Python modules. Each module performs a specific task and works together through the main program.

## Modules

main.py

Controls the main menu and program flow. It allows the user to select different password security options.

password_checker.py

Checks the password and gives a score based on password conditions such as:

password_generator.py

Generates a random password using uppercase letters, lowercase letters, numbers, and special characters.

recommendations.py

Provides suggestions to improve the password based on the password check results.

password_validator.py

Checks whether the password satisfies the required password conditions.

security_report.py

Displays the password security information and results in a clear format.

Minimum length

Uppercase letter

Lowercase letter

Number

Special character

It also gives the password a strength level.

Program Flow

User
↓
main.py
↓
Select Option
↓
Password Checker / Password Generator / Recommendations / Password Validator
↓
Display Result
↓
Return to Main Menu

Design Approach

The project uses separate Python files for different tasks. Functions are used to perform the required operations. This makes the program easier to understand, organize, test, and maintain.
