# Password Policy Validation Engine

import re

MIN_LENGTH = 8

PROHIBITED_SUBSTRINGS = [
    "password",
    "admin",
    "123456"
]


def validate_password(password):
    errors = []

    if len(password) < MIN_LENGTH:
        errors.append(
            "Password must contain at least 8 characters."
        )
    if not any(ch.isupper() for ch in password):
        errors.append(
            "Missing uppercase letter (A-Z)."
        )

    if not any(ch.islower() for ch in password):
        errors.append(
            "Missing lowercase letter (a-z)."
        )

    if not any(ch.isdigit() for ch in password):
        errors.append(
            "Missing digit (0-9)."
        )

    if not any(not ch.isalnum() for ch in password):
        errors.append(
            "Missing special character (e.g., !, @, #)."
        )
    if re.search(r"(.)\1{2,}", password):
        errors.append(
            "Same character must not repeat 3 or more times consecutively."
        )
    password_lower = password.lower()

    for word in PROHIBITED_SUBSTRINGS:
        if word in password_lower:
            errors.append(
                f"Contains prohibited substring: '{word}'."
            )

    return errors
try:
    count = int(input("How many passwords to test? "))

    if count <= 0:
        print("Error: Enter a positive number.")
    else:
        for i in range(count):
            password = input(
                f"\nEnter sample password {i + 1}: "
            )

            errors = validate_password(password)

            print("\nPassword:", password)

            if not errors:
                print("Result: VALID PASSWORD")
                print("All policy rules passed.")
            else:
                print("Result: INVALID PASSWORD")
                print("Failed conditions:")

                for error in errors:
                    print("-", error)

            print("-" * 45)

except ValueError:
    print("Error: Enter a valid integer.")
