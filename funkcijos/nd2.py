def validate_email(email):
    # Check if there is exactly one "@" symbol
    if email.count("@") != 1:
        return False

    # Split the email into username and domain
    parts = email.split("@")
    username = parts[0]
    domain = parts[1]

    # Ensure the username is not empty
    if not username:
        return False

    # Ensure the domain contains at least one "."
    if "." not in domain:
        return False

    # Split the domain into parts
    domain_parts = domain.split(".")

    # Check each domain part (except the last one) is not empty
    for part in domain_parts[:-1]:
        if len(part) == 0:
            return False

    # Ensure the domain suffix (last part) is at least 2 characters long
    if len(domain_parts[-1]) < 2:
        return False

    return True


# Get email input from the user
email = input("Enter an email address: ")

# Validate the email and provide feedback
if validate_email(email):
    print("The email address is valid.")
else:
    print("The email address is invalid.")