import random
import os

# Function to read passwords from file and store in a dictionary
def read_passwords(file_name):
    passwords = {}
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            for line in file:
                data = line.strip().split(' ')
                password = data[0]
                count = int(data[1]) if len(data) > 1 else 1
                passwords[password] = count
    return passwords

# Function to write passwords to the file
def write_passwords(file_name, passwords):
    with open(file_name, 'w') as file:
        for password, count in passwords.items():
            file.write(f"{password} {count}\n")

# Main password generator
def password_generator():
    file_name = "passwords.txt"
    passwords = read_passwords(file_name)

    while True:
        print("\n================== Password Generator App ==================\n\n")

        try:
            passlen = int(input("Enter the length of password (8-15): "))
        except ValueError:
            print("\nPlease enter a valid number.")
            continue

        if 8 <= passlen <= 15:
            s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ@Ł!&#$/\|<>*ł?£&{}[]€;:-_÷^"
            p = "".join(random.sample(s, passlen))

            # Check if the password already exists and increment the count if so
            if p in passwords:
                passwords[p] += 1
                print(f"\n\nYour password is: {p}")
                print(f"This password has been generated {passwords[p]} times.")
            else:
                passwords[p] = 1
                print(f"\n\nYour password is: {p}")

            write_passwords(file_name, passwords)

            if passlen == 15:
                print("\nWarning: Password should not have 15 or more characters.\n")
        else:
            print("\nPassword length should be between 8 and 15 characters.")
            continue

        opt = input("\nDo you want to try again? (da/ne): ")

        if opt.lower() == 'da':
            continue
        elif opt.lower() == 'ne':
            print("Exiting program....")
            break
        else:
            print("Please enter da/ne:")

# Run the password generator
password_generator()
