# Student Email and Identifier Validation System

import re


def validate_email(email):
    errors = []

    if any(ch.isspace() for ch in email):
        errors.append("Email must not contain spaces.")


    if email.count("@") == 0:
        errors.append("Missing '@' separator.")
        return errors

    if email.count("@") > 1:
        errors.append("Email must contain exactly one '@' separator.")
        return errors

    username, domain = email.split("@")


    if not username:
        errors.append("Username is missing.")
    else:
        if not re.fullmatch(r"[A-Za-z0-9._-]+", username):
            errors.append(
                "Username contains invalid characters."
            )

        if username.startswith(".") or username.endswith("."):
            errors.append(
                "Username must not start or end with a dot."
            )

        if ".." in username:
            errors.append(
                "Username must not contain consecutive dots."
            )

  
    if not domain:
        errors.append("Domain is missing.")
    else:
        if "." not in domain:
            errors.append(
                "Domain must contain a name and extension."
            )

        if not re.fullmatch(r"[A-Za-z0-9.-]+", domain):
            errors.append(
                "Domain contains invalid characters."
            )

        if ".." in domain:
            errors.append(
                "Domain must not contain consecutive dots."
            )

        labels = domain.split(".")

        if any(label == "" for label in labels):
            errors.append(
                "Domain contains a missing component."
            )

        for label in labels:
            if label.startswith("-") or label.endswith("-"):
                errors.append(
                    "Domain components must not start or end with a hyphen."
                )
                break

    return errors


def validate_registration(reg_id):
    errors = []

    
    if any(ch.isspace() for ch in reg_id):
        errors.append(
            "Registration ID must not contain spaces."
        )

    
    if not re.fullmatch(r"[A-Za-z0-9-]+", reg_id):
        errors.append(
            "Registration ID contains invalid characters."
        )

    
    if reg_id.count("-") != 2:
        errors.append(
            "Registration ID must contain exactly two hyphens."
        )

    parts = reg_id.split("-")

    if len(parts) != 3:
        errors.append(
            "Registration ID must have department, year, and number."
        )
        return errors

    department, year, number = parts

    if not department:
        errors.append("Department component is missing.")
    elif not re.fullmatch(r"[A-Z]{2,5}", department):
        errors.append(
            "Department must contain 2 to 5 uppercase letters."
        )

  
    if not year:
        errors.append("Year component is missing.")
    elif not re.fullmatch(r"\d{4}", year):
        errors.append(
            "Year must contain exactly four digits."
        )


    if not number:
        errors.append("Student number is missing.")
    elif not re.fullmatch(r"\d{4}", number):
        errors.append(
            "Student number must contain exactly four digits."
        )

    return errors
try:
    count = int(input("Enter number of students to validate: "))

    if count <= 0:
        print("Error: Number of students must be positive.")
    else:
        for i in range(count):
            print(f"\n--- Student {i + 1} ---")

            email = input("Enter student email: ").strip()
            reg_id = input("Enter registration ID: ").strip()

            email_errors = validate_email(email)
            id_errors = validate_registration(reg_id)

            print("\nEmail:", email)

            if email_errors:
                print("Email Status: INVALID")
                for error in email_errors:
                    print("-", error)
            else:
                print("Email Status: VALID")

            print("\nRegistration ID:", reg_id)

            if id_errors:
                print("Registration Status: INVALID")
                for error in id_errors:
                    print("-", error)
            else:
                print("Registration Status: VALID")

            print("-" * 45)

except ValueError:
    print("Error: Enter a valid number of students.")
