# Required libraries
import re

# Valid usernames and their passwords
valid_users = {
    "user": "hacker",
    "asim": "Treasure Hunt",
    "John": "hacker",
    "Alice": "hacker",
    "Michael": "hacker",
    "Sophia": "hacker",
    "David": "hacker",
    "Emma": "hacker",
    "James": "hacker",
    "Olivia": "hacker",
    # Add more users as needed
}

saved_bank_password = ""
bank_balance = 100000000000000000000
attempts = 0

def authenticate(username, password):
    global attempts
    if username in valid_users and valid_users[username] == password:
        return True
    else:
        attempts += 1
        return False

def handle_incorrect_attempt():
    global attempts
    if attempts >= 3:
        print("Too many incorrect attempts. Your account is locked.")
        return True
    else:
        print("Incorrect username or password. Please try again.")
        return False

def check_password_strength(password):
    strong_password = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')
    return strong_password.match(password) is not None

def save_new_password(new_password):
    global saved_bank_password
    if check_password_strength(new_password):
        saved_bank_password = new_password
        return True
    else:
        print("Password is too weak. Please try again.")
        return False

def verify_bank_password(bank_password):
    global saved_bank_password
    return bank_password == saved_bank_password

def select_car(car):
    if car == "Scammer Car":
        print("You have successfully purchased the Scammer Car!")
        return True
    else:
        print("You need to purchase the right Car to proceed.")
        return False

# Simulation of the interaction

print("Welcome to the Password Protected Treasure Hunt")

while True:
    username = input("Username: ")
    password = input("Password: ")

    if authenticate(username, password):
        print("Login successful!")
        break
    elif handle_incorrect_attempt():
        break

while True:
    action = input("What would you like to do?\n1. Create a new password for your bank\n2. Exit\n")

    if action == "1":
        new_password = input("Enter a new password: ")
        if save_new_password(new_password):
            print("New password saved successfully.")
            break
    elif action == "2":
        print("Exiting the program.")
        break

while True:
    bank_password = input("Enter your bank password to access your bank: ")

    if verify_bank_password(bank_password):
        print("Bank access granted!")
        car_choice = input("Select a car to proceed: Economy Car, Luxury Car, Scammer Car\n")
        if select_car(car_choice):
            print("Congratulations, you've successfully completed the game!")
            break
    else:
        print("Incorrect bank password. Please try again.")
# Rest of the Python code to simulate the treasure hunt game

def main():
    print("Welcome to the Password Protected Treasure Hunt")

    while True:
        username = input("Username: ")
        password = input("Password: ")

        if authenticate(username, password):
            print("Login successful!")
            break
        elif handle_incorrect_attempt():
            return

    while True:
        action = input("What would you like to do?\n1. Create a new password for your bank\n2. Exit\n")

        if action == "1":
            new_password = input("Enter a new password: ")
            if save_new_password(new_password):
                print("New password saved successfully.")
                break
        elif action == "2":
            print("Exiting the program.")
            return

    while True:
        bank_password = input("Enter your bank password to access your bank: ")

        if verify_bank_password(bank_password):
            print("Bank access granted!")
            car_choice = input("Select a car to proceed: Economy Car, Luxury Car, Scammer Car\n")
            if select_car(car_choice):
                print("Congratulations, you've successfully completed the game!")
                break
        else:
            print("Incorrect bank password. Please try again.")

if __name__ == "__main__":
    main()
