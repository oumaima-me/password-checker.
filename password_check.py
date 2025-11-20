# Simple Password Strength Checker
# This is a small beginner-friendly project I built to practice
# Python and understand how basic security rules work.
# It checks how strong a password is based on common criteria.

def check_password(password):
    """Evaluate the strength of a password and return details."""

    strength_points = 0
    missing = []

    # Rule 1: Length should be at least 8 characters
    if len(password) >= 8:
        strength_points += 1
    else:
        missing.append("at least 8 characters")

    # Rule 2: At least one uppercase letter
    if any(c.isupper() for c in password):
        strength_points += 1
    else:
        missing.append("an uppercase letter")

    # Rule 3: At least one lowercase letter
    if any(c.islower() for c in password):
        strength_points += 1
    else:
        missing.append("a lowercase letter")

    # Rule 4: At least one number
    if any(c.isdigit() for c in password):
        strength_points += 1
    else:
        missing.append("a number")

    # Rule 5: At least one special character
    special_characters = "!@#$%^&*()_-+=[]{}|:;,.?/<>"
    if any(c in special_characters for c in password):
        strength_points += 1
    else:
        missing.append("a special character")

    # Determine the final strength label
    if strength_points == 5:
        strength = "Strong"
    elif strength_points >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, missing


# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------

print("Password Strength Checker")
password = input("Enter a password to analyze: ")

strength, missing = check_password(password)

print("\nPassword Strength:", strength)

if missing:
    print("Missing:", ", ".join(missing))
else:
    print("Your password meets all the requirements! 🎉")
