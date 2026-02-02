# regex_validation.py

import re


# ---------------- EMAIL VALIDATION ----------------
def validate_email(email):
    if not email:
        return "Email cannot be empty"

    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.fullmatch(pattern, email):
        return "Valid Email ✅"
    else:
        return "Invalid Email ❌"


# ---------------- MOBILE NUMBER VALIDATION ----------------
def validate_mobile(mobile):
    if not mobile:
        return "Mobile number cannot be empty"

    pattern = r'^(?:\+91|91)?[6-9]\d{9}$'

    if re.fullmatch(pattern, mobile):
        return "Valid Indian Mobile Number ✅"
    else:
        return "Invalid Mobile Number ❌"


# ---------------- PASSWORD VALIDATION ----------------
def validate_password(password):
    if not password:
        return "Password cannot be empty"

    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

    if re.fullmatch(pattern, password):
        return "Strong Password ✅"
    else:
        return (
            "Invalid Password ❌\n"
            "Password must contain:\n"
            "- Minimum 8 characters\n"
            "- At least 1 uppercase letter\n"
            "- At least 1 lowercase letter\n"
            "- At least 1 digit\n"
            "- At least 1 special character (@$!%*?&)"
        )


# ---------------- MAIN PROGRAM ----------------
def main():
    print("\n--- REGEX DATA VALIDATION ---")

    email = input("\nEnter Email: ").strip()
    print(validate_email(email))

    mobile = input("\nEnter Indian Mobile Number: ").strip()
    print(validate_mobile(mobile))

    password = input("\nEnter Password: ").strip()
    print(validate_password(password))


# Run program
if __name__ == "__main__":
    main()
