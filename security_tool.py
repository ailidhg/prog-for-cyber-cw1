# Security Tool
def security_event_counter():
    password = "Prog4Cyber"
    correct = 0
    incorrect = 0

# prompt the user to enter the password 10 times and count correct and incorrect attempts
    for i in range(10):
        user_input = input("Enter the password: ")
        if user_input == password:
            print("Access granted.")
            correct += 1
        else:
            print("Access denied.")
            incorrect += 1
    print(f"Correct attempts: {correct}")
    print(f"Incorrect attempts: {incorrect}")

    #then calculate the percentage of incorrect attempts
    total_attempts = correct + incorrect
    percentage = (incorrect / total_attempts) * 100

    print("Total attempts:", total_attempts)
    print("Incorrect percentage:", percentage, "%")

    if percentage > 50:
        print("Warning: More than 50% of attempts were incorrect.")
    else:
        print("Access attempts are within acceptable limits.")

# Brute-Force Simulation
def brute_force_simulation():
    password = "UWS242"
    max_attempts = 5
    attempts = 0

# prompt the user to enter the password and simulate a brute-force attack
    while attempts < max_attempts:
        user_input = input("Enter the password: ")
        if user_input == password:
            print("Access granted.")
            return
        else:
            print("Access denied.")
            attempts += 1

    print("Simulation failed. Maximum attempts reached.")

# Login Authentication
def login_authentication():
    username = "admin"
    password = "06LK"
    attempts = 0
    max_attempts = 3

# prompt the user to enter the username and password and simulate a login authentication
    while attempts < max_attempts:
        username_input = input("Enter the username: ")
        if username_input != username:
            print("Incorrect username.")
            attempts += 1
            continue
        password_input = input("Enter the password: ")
        if username_input == username and password_input == password:
            print("Access granted.")
            return
        else:
            print("Access denied.")
            attempts += 1

    print("Account locked for 24 hours.")

# Main function to run the security tool
def main():
    while True:
        print("\n===== SECURITY TOOL =====")
        print("1. Security Event Counter")
        print("2. Brute-Force Simulation")
        print("3. Login Authentication")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            security_event_counter()
        elif choice == "2":
            brute_force_simulation()
        elif choice == "3":
            login_authentication()
        elif choice == "4":
            print("Exiting security tool.")
            break
        else:
            print("Invalid choice. Please try again.")

main()