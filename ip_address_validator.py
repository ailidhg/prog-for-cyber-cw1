# for validating an IP address
def validate_ip(ip):
    ip = ip.strip()
    # Check if the IP address is in the correct format
    if ip.count(".") != 3:
        return False

    parts = ip.split(".")
    if len(parts) != 4:
        return False

    # Check if each part is a valid number between 0 and 255
    for part in parts:
        if not part.isdigit():
            return False
        num = int(part)
        if num < 0 or num > 255:
            return False

    return True

# get user input and validate the IP address
ip_input = input("Enter an IP address to validate: ")
result = validate_ip(ip_input)
if result:
    print("This is a valid IP address.") 
else:
    print("This is not a valid IP address.")