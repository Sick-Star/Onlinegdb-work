#!/home/codespace/.python/current/bin/python


import csv

filename = "users.csv"

# Sign up
def sign_up():
    username = input("Enter a username: ")

    with open(filename, "a+", newline="") as file:
        file.seek(0)
        reader = csv.reader(file)

        for row in reader:
            if row[0] == username:
                print("Username already exists!")
                return

        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Choose a password: ")
        memorable = input("Choose a memorable word: ")

        writer = csv.writer(file)
        writer.writerow([username, name, email, password, memorable])

        print("Account created successfully!")


# Log in
def log_in():
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open(filename, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0] == username and row[3] == password:
                print("Login successful!")
                return username

    print("Incorrect username or password.")
    return None


# Recover password
def recover_password():
    username = input("Enter username: ")
    memorable = input("Enter your memorable word: ")

    rows = []

    with open(filename, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)

    for row in rows:
        if row[0] == username and row[4] == memorable:
            row[3] = input("Enter your new password: ")

            with open(filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(rows)

            print("Password reset successfully!")
            return

    print("Incorrect details.")


# Change password
def change_password(username):
    rows = []

    with open(filename, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)

    for row in rows:
        if row[0] == username:
            old_password = input("Enter your current password: ")

            if row[3] == old_password:
                row[3] = input("Enter your new password: ")

                with open(filename, "w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerows(rows)

                print("Password changed!")
            else:
                print("Incorrect password.")
            return


# Edit contact details
def edit_details(username):
    rows = []

    with open(filename, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)

    for row in rows:
        if row[0] == username:
            row[1] = input("Enter your new name: ")
            row[2] = input("Enter your new email: ")

            with open(filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(rows)

            print("Details updated!")
            return


# Main menu
logged_in = None

while True:
    print("\nUSER CREDENTIALS MENU")
    print("1. Sign up as a new user")
    print("2. Log in as an existing user")
    print("3. Recover forgotten password")
    print("4. Change password")
    print("5. Edit contact details")
    print("6. Finish and log off")

    choice = input("Choose an option: ")

    if choice == "1":
        sign_up()

    elif choice == "2":
        logged_in = log_in()

    elif choice == "3":
        recover_password()

    elif choice == "4":
        if logged_in:
            change_password(logged_in)
        else:
            print("Please log in first.")

    elif choice == "5":
        if logged_in:
            edit_details(logged_in)
        else:
            print("Please log in first.")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
