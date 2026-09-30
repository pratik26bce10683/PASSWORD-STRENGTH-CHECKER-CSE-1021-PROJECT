# Password Security Tool

A modular Python command-line application for analyzing password
strength, generating passwords, providing recommendations, and
validating passwords against basic security requirements.

## Project Overview

The **Password Security Tool** was developed as a CSE-1021 programming
project to apply Python concepts to a practical problem.

The application provides four main operations:

1.  **Check Password Strength** -- analyzes a password against five
    basic criteria and calculates a score out of 5.
2.  **Generate Password** -- generates a password containing uppercase
    letters, lowercase letters, digits, and special characters.
3.  **Get Recommendations** -- identifies missing password requirements
    and suggests improvements.
4.  **Validate Password** -- checks whether a password satisfies all
    five required criteria.

The project uses a modular structure with separate Python modules for
analysis, generation, validation, recommendations, reporting, and user
interaction.

> **Note:** This is an educational password-strength tool. It is not a
> complete security audit and does not guarantee that a password is
> resistant to real-world attacks.

------------------------------------------------------------------------

## Features

### Password Strength Analysis

The program checks:

-   Minimum length of 8 characters
-   At least one uppercase letter
-   At least one lowercase letter
-   At least one digit
-   At least one special character

Each satisfied criterion contributes one point.

### Strength Classification

    Score Strength
  ------- -------------
     0--2 WEAK
        3 MEDIUM
        4 STRONG
        5 VERY STRONG

### Password Generation

The generator creates passwords containing the required character types
and shuffles the resulting characters.

### Recommendations

The application identifies missing password requirements and provides
suggestions for improvement.

### Password Validation

The validator checks all five mandatory requirements and returns a
valid/invalid result.

### Security Report

The report displays the password-analysis results, including:

-   Individual criteria
-   PASS/FAIL status
-   Score
-   Strength category
-   Recommendations

Passwords are masked in the security report.

------------------------------------------------------------------------

## Project Structure

The repository is organized into separate documentation, source-code,
and testing folders:

``` text
PASSWORD_SECURITY_TOOL-CSE-1021-PROJECT/
│
├── docs/
│   └── Project documentation / supporting files
│
├── src/
│   ├── main.py
│   ├── password_checker.py
│   ├── password_generator.py
│   ├── recommendations.py
│   ├── password_validator.py
│   └── security_report.py
│
├── tests/
│   └── test_password.py
│
├── .gitignore
├── README.md
└── statement.md
```

### Source Modules

  -----------------------------------------------------------------------
  Module                              Responsibility
  ----------------------------------- -----------------------------------
  `main.py`                           Menu, user interaction, input
                                      handling, and application flow

  `password_checker.py`               Analyzes password characteristics
                                      and calculates the score

  `password_generator.py`             Generates passwords with the
                                      required character types

  `recommendations.py`                Generates recommendations based on
                                      missing criteria

  `password_validator.py`             Validates passwords against all
                                      required rules

  `security_report.py`                Displays the formatted
                                      password-security report

  `test_password.py`                  Contains automated tests for the
                                      project
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## Functional Requirements

  -----------------------------------------------------------------------
  ID                Function          Input             Output
  ----------------- ----------------- ----------------- -----------------
  FR1               Check password    Password          Score and
                    strength                            strength

  FR2               Generate password Desired length    Generated
                                                        password

  FR3               Get               Password          Improvement
                    recommendations                     recommendations

  FR4               Validate password Password          VALID / INVALID

  FR5               Display security  Password and      Detailed report
                    report            analysis          

  FR6               Menu-based        User choice       Selected
                    interaction                         operation
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## Password Analysis Rules

A password receives one point for each satisfied criterion:

1.  Length is at least 8 characters.
2.  Contains an uppercase letter.
3.  Contains a lowercase letter.
4.  Contains a digit.
5.  Contains a special character.

The total score is between **0 and 5**.

------------------------------------------------------------------------

## Non-Functional Requirements

### Usability

-   Simple numbered command-line menu
-   Clear output and labels
-   Easy-to-understand password-strength results

### Maintainability

-   Separate modules for separate responsibilities
-   Reusable functions
-   Modular folder structure

### Reliability

-   Handles empty password input
-   Handles invalid numeric input
-   Validates password requirements consistently

### Security

-   Passwords are not persisted by the application
-   Passwords are masked in the security report
-   The current educational generator uses Python's `random` module

> For production-grade credential generation, Python's `secrets` module
> would be preferable.

### Resource Efficiency

-   Runs locally
-   Uses lightweight Python operations
-   Does not require a database or network service

### Error Handling

-   Invalid menu choices are handled
-   Invalid password lengths are handled
-   Non-numeric length input is handled using exception handling

------------------------------------------------------------------------

## Technologies Used

-   **Python 3**
-   **Python standard libraries:** `random`, `string`
-   **pytest** -- automated testing
-   **Command Line Interface (CLI)**
-   **Git**
-   **GitHub**
-   **Markdown**

The application itself uses Python standard libraries only. `pytest` is
used separately for automated testing.

------------------------------------------------------------------------

## Requirements

### Python

Check that Python is installed:

``` bash
python --version
```

### pytest

The application does not require external packages, but `pytest` is
required to run the automated tests.

Check pytest:

``` bash
python -m pytest --version
```

If pytest is not installed:

``` bash
python -m pip install pytest
```

------------------------------------------------------------------------

## Installation

### 1. Clone the repository

``` bash
git clone https://github.com/pratik26bce10683/PASSWORD_SECURITY_TOOL-CSE-1021-PROJECT.git
```

### 2. Open the project folder

``` bash
cd PASSWORD_SECURITY_TOOL-CSE-1021-PROJECT
```

### 3. Install pytest for testing

``` bash
python -m pip install pytest
```

> This step is only required if pytest is not already installed.

------------------------------------------------------------------------

## How to Run the Application

Because the source code is stored in the `src` folder, run the main
program from the repository root with:

``` bash
python src/main.py
```

The application provides a menu similar to:

``` text
===================================
       PASSWORD SECURITY TOOL
===================================
1. Check Password Strength
2. Generate Password
3. Get Recommendations
4. Validate Password
5. Exit
Enter your choice:
```

Enter `1`, `2`, `3`, `4`, or `5` to select an operation.

------------------------------------------------------------------------

## Testing

Automated tests are stored in the `tests` folder.

### Run all tests

From the repository root:

``` bash
python -m pytest
```

### Current Test Result

The current test suite successfully passes all **6 collected tests**:

``` text
6 passed in 0.10s
```

This confirms that the current automated test run completed
successfully.

### Testing Areas

The test suite covers important password-tool functionality, including:

-   Password analysis
-   Password validation
-   Password-generation behaviour
-   Password requirements
-   Different password inputs
-   Expected function results

Testing should also consider:

-   Weak passwords
-   Medium passwords
-   Strong passwords
-   Very strong passwords
-   Minimum password length
-   Empty input
-   Invalid numeric input

------------------------------------------------------------------------

## System Architecture

The application follows a modular architecture:

``` text
                         +----------------+
                         |    main.py     |
                         |  Menu / CLI    |
                         +-------+--------+
                                 |
              +------------------+------------------+
              |          |          |       |       |
              v          v          v       v       v
        +----------+ +----------+ +------+ +------+ +----------------+
        | Checker  | | Generator| | Rec. | |Valid. | | Security Report|
        +----------+ +----------+ +------+ +------+ +----------------+
```

### Module Responsibilities

-   **`main.py`** controls the user interface and program flow.
-   **`password_checker.py`** analyzes password characteristics and
    calculates the score.
-   **`password_generator.py`** creates passwords.
-   **`recommendations.py`** provides improvement suggestions.
-   **`password_validator.py`** checks whether all requirements are
    satisfied.
-   **`security_report.py`** formats and displays the analysis.

------------------------------------------------------------------------

## Workflow

``` text
Start
  |
  v
Display Main Menu
  |
  +----> Check Password Strength
  |             |
  |             v
  |       Analyze Password
  |             |
  |             v
  |       Display Report
  |
  +----> Generate Password
  |             |
  |             v
  |       Enter Length
  |             |
  |             v
  |       Generate Password
  |
  +----> Recommendations
  |             |
  |             v
  |       Analyze Password
  |             |
  |             v
  |       Display Suggestions
  |
  +----> Validate Password
  |             |
  |             v
  |       Check Requirements
  |             |
  |             v
  |       VALID / INVALID
  |
  +----> Exit
                |
                v
               End
```

------------------------------------------------------------------------

## Design Decisions

### Modular Programming

Separate modules were used so each part of the program has a clear
responsibility. This makes the project easier to understand, test,
maintain, and extend.

### Boolean Criteria

Each password requirement is represented using Boolean conditions such
as:

``` python
is_length
is_upper
is_lower
is_digit
is_special
```

### Score-Based Classification

The program calculates a score from 0 to 5 and maps the score to a
strength category.

### Standard Libraries

The application uses Python's standard `random` and `string` libraries,
keeping the main application lightweight.

### Command-Line Interface

A CLI was selected to demonstrate core Python programming concepts
without requiring an additional graphical framework.

------------------------------------------------------------------------

## Scope

### In Scope

-   Password length checking
-   Uppercase checking
-   Lowercase checking
-   Digit checking
-   Special-character checking
-   Password scoring
-   Strength classification
-   Password generation
-   Recommendations
-   Password validation
-   Command-line reporting
-   Basic input/error handling

### Out of Scope

The current version does not:

-   Store passwords in a database
-   Send passwords over a network
-   Check passwords against leaked-password databases
-   Perform password-cracking simulations
-   Implement multi-factor authentication
-   Manage user accounts

------------------------------------------------------------------------

## Limitations

This project uses a basic rule-based password-strength system.

A password classified as **VERY STRONG** by this program is only strong
according to the five rules implemented in this project. The
classification does not represent a complete real-world security
assessment.

The current password generator uses `random`, which is suitable for
demonstrating Python programming concepts but is not intended for
production credential generation.

------------------------------------------------------------------------

## Future Enhancements

Possible improvements include:

-   Replace `random` with Python's `secrets` module
-   Add password entropy estimation
-   Add checks for common passwords
-   Add compromised-password checking through an appropriate security
    service
-   Add a graphical user interface
-   Improve security-report visualization
-   Expand automated test coverage
-   Add continuous integration using GitHub Actions

------------------------------------------------------------------------

## Learning Outcomes

This project demonstrates practical use of:

-   Python functions
-   Modular programming
-   Conditional statements
-   `for` and `while` loops
-   Lists and dictionaries
-   String methods
-   Boolean expressions
-   `any()`
-   Exception handling
-   Random password generation
-   Automated testing with pytest
-   Git and GitHub version control

------------------------------------------------------------------------

## Documentation

Additional project documentation is available in:

-   `statement.md` -- problem statement, scope, target users, and
    high-level features
-   `docs/` -- supporting project documentation

------------------------------------------------------------------------

## Author

**Pratik Yadav**

CSE-1021 Project

------------------------------------------------------------------------

## Repository

**GitHub Repository:**\
https://github.com/pratik26bce10683/PASSWORD_SECURITY_TOOL-CSE-1021-PROJECT
