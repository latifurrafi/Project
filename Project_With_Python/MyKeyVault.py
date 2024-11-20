import csv

def add():
    username = input("Enter Username: ").strip().capitalize()

    passwords = {}
    try:
        with open("Passwords.csv", 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) == 2:
                    passwords[row[0].strip().capitalize()] = row[1].strip()
    except FileNotFoundError:
        pass
    if username in passwords:
        raise Exception(f"\t\t\tError: Username '{username}' already exists!")
    password = input("Enter Password: ")
    
    with open("Passwords.csv", 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([username, password])
    print("Password added successfully!")

def get():
    username = input("Enter Username: ").capitalize()

    passwords = {}
    try:
        with open("Passwords.csv", 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) == 2:
                    passwords[row[0]] = row[1]
    except FileNotFoundError:
        print("Error: No passwords found!")
        return

    if username in passwords:
        print(f"\t\t\tPassword for {username} is {passwords[username]}")
    else:
        print("No such username exists!")

def getlist():
    passwords = {}
    try:
        with open("Passwords.csv", 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) == 2:
                    passwords[row[0]] = row[1]
    except FileNotFoundError:
        print("Error: No passwords found!")
        return

    if passwords:
        print("\t\t\tList of passwords:")
        for username, password in passwords.items():
            print(f"\t\t\t{username} : {password}")
    else:
        print("Password list is empty.")

def delete():
    username = input("Enter Username to delete: ")

    temp_passwords = []
    found = False

    try:
        with open("Passwords.csv", 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) == 2:
                    if row[0] != username:
                        temp_passwords.append(row)
                    else:
                        found = True
        if not found:
            print(f"\t\t\tNo such user '{username}' exists!")
            return

        with open("Passwords.csv", 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(temp_passwords)

        print(f"\t\t\tUser '{username}' deleted successfully!")
    except Exception as e:
        print(f"Error deleting user {username}: {e}")

if __name__ == "__main__":
    while True:
        print("\nPassword Manager")
        print("1. Add a new password")
        print("2. Get a password")
        print("3. List all passwords")
        print("4. Delete a password")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                add()
            except Exception as e:
                print(e)
        elif choice == "2":
            get()
        elif choice == "3":
            getlist()
        elif choice == "4":
            delete()
        elif choice == "5":
            print("Exiting Password Manager.")
            break
        else:
            print("Invalid choice. Please try again.")