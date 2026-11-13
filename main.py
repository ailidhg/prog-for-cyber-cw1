import security_tools

# get password from user input
password = input("Enter a password: ")

# validate the password
is_valid, message = security_tools.validate_password(password)
print(message)

# suggest a stronger password if the entered password is not valid
if not is_valid:
    print("Suggested password: ", security_tools.generate_password())

# get IP address from user input
ip = input("Enter an IP address: ")

# validate the IP address
is_valid, message = security_tools.validate_ip(ip)
print(message)