# Password Security Tool 

## 1. Problem Statement

Passwords are commonly used to protect personal accounts, applications, and digital information. However, users may create passwords that do not satisfy basic security requirements such as sufficient length, uppercase and lowercase characters, digits, and special characters.

The **Password Security Tool** is developed to provide a simple command-line solution for analyzing and improving passwords. The system checks a password against predefined security criteria, calculates a strength score, provides recommendations, generates passwords, and validates whether a password satisfies all required conditions.

The project demonstrates the application of Python programming concepts to a practical problem while following a modular and maintainable software design.

---

## 2. Project Scope

The project covers the development of a Python-based command-line Password Security Tool.

### The project includes:

- Password strength analysis.
- Password scoring based on five predefined criteria.
- Password strength classification.
- Random password generation.
- Recommendations for improving passwords.
- Password validation.
- Security report generation.
- User interaction through a menu-driven command-line interface.
- Input validation and basic error handling.
- Modular implementation using separate Python files.

### Password criteria used by the system:

1. Minimum password length of 8 characters.
2. At least one uppercase letter.
3. At least one lowercase letter.
4. At least one digit.
5. At least one special character.

### The project does not include:

- Database storage.
- User account management.
- Network-based password checking.
- Multi-factor authentication.
- Checking passwords against leaked-password databases.
- Complete real-world password-cracking resistance analysis.

The tool is intended as an educational project demonstrating password evaluation using predefined rules rather than as a complete enterprise password-security system.

---

## 3. Target Users

The target users of this project are:

- Students learning Python programming.
- Beginners learning modular programming.
- Users who want to perform a basic local password check.
- Students demonstrating software development concepts such as functions, modules, validation, and testing.

---

## 4. High-Level Features

### 4.1 Password Strength Analysis

The system analyzes a password using five criteria:

- Length
- Uppercase character
- Lowercase character
- Digit
- Special character

Each satisfied criterion contributes one point to the password's score.

### 4.2 Password Strength Classification

| Score | Strength |
|---:|---|
| 0–2 | WEAK |
| 3 | MEDIUM |
| 4 | STRONG |
| 5 | VERY STRONG |

### 4.3 Password Generator

The system can generate a random password based on a user-specified length.

The generated password includes:

- Uppercase characters
- Lowercase characters
- Digits
- Special characters

The minimum supported password length is 8 characters.

### 4.4 Password Recommendations

The system identifies missing password requirements and provides recommendations such as:

- Use at least 8 characters.
- Add at least one uppercase letter.
- Add at least one lowercase letter.
- Add at least one digit.
- Add at least one special character.

### 4.5 Password Validation

The validation module checks whether all five required conditions are satisfied.

The result is displayed as:

```text
Password Status: VALID
```

or:

```text
Password Status: INVALID
```

### 4.6 Security Report

The system provides a formatted security report showing:

- Password masked with `*`
- Length requirement
- Uppercase requirement
- Lowercase requirement
- Digit requirement
- Special-character requirement
- Score out of 5
- Password strength

### 4.7 Menu-Driven Interface

The main program provides the following options:

```text
1. Check Password Strength
2. Generate Password
3. Get Recommendations
4. Validate Password
5. Exit
```

This provides a simple workflow for interacting with the different modules of the system.

---

## 5. Major Project Modules

| Module | Purpose |
|---|---|
| `main.py` | Controls the application and menu |
| `password_checker.py` | Analyzes password strength |
| `password_generator.py` | Generates passwords |
| `recommendations.py` | Provides password recommendations |
| `password_validator.py` | Validates passwords |
| `security_report.py` | Displays the security report |

This modular structure separates responsibilities and makes the project easier to maintain and test.

---

## 6. Expected Outcome

The expected outcome is a working Python command-line application that allows a user to analyze, generate, improve, and validate passwords using clearly defined security rules.

The project demonstrates the practical use of Python functions, modules, loops, conditional statements, string processing, Boolean expressions, lists, dictionaries, exception handling, and random character generation.

---

## 7. Project Goal

The overall goal of the project is to apply programming and software-development concepts to a practical password-security problem while producing a modular, documented, testable, and maintainable Python application.
