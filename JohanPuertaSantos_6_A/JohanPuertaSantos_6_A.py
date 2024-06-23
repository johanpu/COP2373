# This program take's a user's phone numbers, social security numbers, or zip codes and validates
# them using regular expressions. It will then print whether they are valid or not.

import re
# Checks validity of SSN using regular expression.
def is_valid_ssn(ssn):
    pattern = r'^\d{3}-\d{2}-\d{4}$'
    return re.match(pattern, ssn) is not None

# Checks validity of zip code using regular expression.
def is_valid_zip_code(zip_code):
    pattern = r'^\d{5}(?:-\d{4})?$'
    return re.match(pattern, zip_code) is not None

# Checks validity of phone number using regular expression.
def is_valid_phone_number(phone_number):
    pattern = r'^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$'
    return re.match(pattern, phone_number) is not None

# Function takes user's input and validates it.
def main():
    # Take's user's input and stores it.
    ssn = input("Please enter your social security number (or enter NONE): ")
    zip_code = input("Please enter your zip code (or enter NONE): ")
    phone_number = input("Please enter your phone number (or enter NONE): ")
    print()

    # Validates user's SSN.
    if ssn != "NONE":
        if is_valid_ssn(ssn):
            print("Social security number is valid.")
        else:
            print("Social security number is invalid.")
            print("Try formatting it like this: XXX-XX-XXXX.\n")

    if ssn == "NONE":
        print("No SSN was provided.")

    # Validates user's zip code.
    if zip_code != "NONE":
        if is_valid_zip_code(zip_code):
            print("Zip code is valid.")
        else:
            print("Zip code is invalid.")
            print("Try formatting it like this: XXXXX or XXXXX-XXXX.\n")

    if zip_code == "NONE":
        print("No zip code was provided.")

    # Validates user's phone number.
    if phone_number != "NONE":
        if is_valid_phone_number(phone_number):
            print("Phone number is valid.")
        else:
            print("Phone number is invalid.")
            print("Try formatting it like this: XXX-XXX-XXXX, XXXXXXXXXX, or XXX XXX XXXX.\n")

    if phone_number == "NONE":
        print("No phone number was provided.")

# Calls main.
main()