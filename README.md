# Password Security Tool

A Python-based command-line application that analyzes password strength,
generates secure passwords, validates passwords, and provides
recommendations for improving password security.

## Overview

The **Password Security Tool** is an educational Python project
developed to demonstrate programming concepts such as:

-   Functions and modular programming
-   Conditional statements and loops
-   String processing
-   Lists and dictionaries
-   Input validation and error handling
-   Password analysis
-   Random password generation
-   Testing with `pytest`

The application provides a simple menu-driven interface so that users
can check password strength, generate passwords, receive
recommendations, and validate passwords.

> **Note:** This project is intended for educational purposes. It uses
> basic password-strength rules and is not a complete password security
> audit or password-cracking resistance test.

------------------------------------------------------------------------

## Features

### 1. Password Strength Checker

Analyzes a password using five basic criteria:

-   Minimum length of 8 characters
-   At least one uppercase letter
-   At least one lowercase letter
-   At least one digit
-   At least one special character

Each satisfied criterion contributes one point.

### 2. Password Generator

Generates a password according to the requested length and includes:

-   Uppercase letters
-   Lowercase letters
-   Numbers
-   Special characters

### 3. Password Recommendations

Identifies missing password requirements and provides suggestions for
improvement.

### 4. Password Validator

Checks whether a password satisfies all five required criteria and
returns a valid/invalid result.

### 5. Security Report

Displays a formatted password-security report containing:

-   Individual criteria results
-   Total score
-   Strength category
-   Recommendations

Passwords should be displayed in masked form in reports where
appropriate.

### 6. Menu-Based Interface

The application provides a simple command-line menu for accessing the
different functions.

------------------------------------------------------------------------

## Password Strength Rules

    Score Strength
  ------- -------------
     0--2 WEAK
        3 MEDIUM
        4 STRONG
        5 VERY STRONG

### Criteria

  Criterion           Requirement
  ------------------- --------------------------------
  Length              At least 8 characters
  Uppercase           At least one uppercase letter
  Lowercase           At least one lowercase letter
  Digit               At least one number
  Special Character   At least one special character

------------------------------------------------------------------------

## Project Structure

``` text
Password-Security-Tool/
│
├── src/
│   ├── main.py
│   ├── password_checker.py
│   ├── password_generator.py
│   ├── password_validator.py
│   ├── recommendations.py
│   └── security_report.py
│
├── tests/
│   └── test_password.py
│
├── README.md
├── statement.md
└── .gitignore
```

### Module Description

  -----------------------------------------------------------------------
  File                                Purpose
  ----------------------------------- -----------------------------------
  `main.py`                           Provides the menu and controls
                                      program flow

  `password_checker.py`               Analyzes password criteria and
                                      calculates the score

  `password_generator.py`             Generates passwords

  `password_validator.py`             Checks whether a password meets all
                                      required criteria

  `recommendations.py`                Provides recommendations based on
                                      missing criteria

  `security_report.py`                Creates a formatted security report

  `test_password.py`                  Contains automated tests for the
                                      project
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## Technologies Used

-   **Python 3**
-   **pytest** for automated testing
-   Python standard libraries such as `random` and `string`
-   Command Line Interface (CLI)
-   Git and GitHub
-   Markdown

------------------------------------------------------------------------

## Requirements

### Python

Python 3 is required.

Check your Python installation:

``` bash
python --version
```

### pytest

The project uses `pytest` for automated testing.

Check whether pytest is installed:

``` bash
python -m pytest --version
```

If it is not installed:

``` bash
python -m pip install pytest
```

------------------------------------------------------------------------

## How to Run

### 1. Clone the repository

``` bash
git clone https://github.com/pratik26bce10683/PASSWORD_SECURITY_TOOL-CSE-1021-PROJECT.git
```

### 2. Open the project folder

``` bash
cd PASSWORD_SECURITY_TOOL-CSE-1021-PROJECT
```

### 3. Run the application

If the source files are inside `src`:

``` bash
python src/main.py
```

If your VS Code project is already configured to run from the `src`
directory:

``` bash
python main.py
```

------------------------------------------------------------------------

## Testing

Automated tests are included in the `tests` folder.

Run all tests using:

``` bash
python -m pytest
```

### Current Test Result

The project currently contains **6 automated test cases**.

Latest test execution:

``` text
6 passed in 0.10s
```

This confirms that all six collected tests passed successfully.

### Testing Coverage

The tests are designed to check important project functionality,
including:

-   Password analysis
-   Password validation
-   Password generation
-   Password-strength conditions
-   Different password inputs
-   Expected program behaviour

------------------------------------------------------------------------

## Functional Requirements

  -----------------------------------------------------------------------
  ID                Requirement       Input             Output
  ----------------- ----------------- ----------------- -----------------
  FR1               Check password    Password          Score and
                    strength                            strength

  FR2               Generate password Desired length    Generated
                                                        password

  FR3               Give              Password          Improvement
                    recommendations                     suggestions

  FR4               Validate password Password          Valid/Invalid

  FR5               Display security  Password and      Detailed report
                    report            analysis          

  FR6               Menu interaction  User choice       Selected
                                                        operation
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## Non-Functional Requirements

### 1. Usability

The application should be simple to operate through a clear command-line
menu.

### 2. Maintainability

The project is divided into separate modules so that individual features
can be modified and maintained easily.

### 3. Reliability

The program validates inputs and handles invalid entries where
appropriate.

### 4. Security

Passwords should not be unnecessarily displayed in plain text in
security reports.

### 5. Performance

The application performs password checks and generation quickly using
lightweight Python operations.

### 6. Error Handling

Invalid menu choices, invalid lengths, and other incorrect inputs are
handled appropriately.

------------------------------------------------------------------------

## System Architecture

The project follows a modular architecture:

``` text
                 +----------------+
                 |    main.py     |
                 +-------+--------+
                         |
          +--------------+--------------+
          |              |              |
          v              v              v
 +----------------+ +-----------+ +----------------+
 | Password       | | Generator | | Validator      |
 | Checker        | |           | |                |
 +-------+--------+ +-----------+ +----------------+
         |
         v
 +-------------------+
 | Recommendations   |
 +-------------------+
         |
         v
 +-------------------+
 | Security Report   |
 +-------------------+
```

The `main.py` module manages user interaction and connects the different
functional modules.

------------------------------------------------------------------------

## Design Decisions

### Modular Design

Different responsibilities are separated into different Python files.
This improves readability, maintainability, and reusability.

### Boolean Password Criteria

Password requirements are represented using Boolean conditions such as:

``` python
is_upper
is_lower
is_digit
is_special
```

This makes the password analysis straightforward.

### Score-Based Strength

Each satisfied requirement contributes one point. The final score is
used to classify the password.

### Standard Python Libraries

The project uses Python's standard libraries where possible, keeping the
application lightweight and easy to run.

------------------------------------------------------------------------

## Limitations

This project uses a basic rule-based password-strength system.

It does **not**:

-   Check passwords against leaked-password databases
-   Estimate complete password entropy
-   Test resistance against real password-cracking attacks
-   Provide multi-factor authentication
-   Store or manage user accounts
-   Connect to an online security service

Therefore, the strength category should be treated as an educational
assessment rather than a complete security guarantee.

------------------------------------------------------------------------

## Future Enhancements

Possible future improvements include:

-   Use Python's `secrets` module for stronger password generation
-   Add password entropy estimation
-   Add a graphical user interface (GUI)
-   Add more advanced password rules
-   Add support for checking common or compromised passwords
-   Improve reporting and visualization
-   Add more automated test cases

------------------------------------------------------------------------

## Learning Outcomes

This project demonstrates practical use of:

-   Python functions
-   Modular programming
-   Conditional statements
-   Loops
-   Lists and dictionaries
-   String operations
-   Input validation
-   Exception handling
-   Random password generation
-   Automated testing
-   Git and GitHub version control

------------------------------------------------------------------------

