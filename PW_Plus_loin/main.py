import string
import random
import hashlib
import json
import os

PASSWORD_FILE = "passwords.json"

def load_passwords():
    if not os.path.exists(PASSWORD_FILE):
        return {}  
    with open(PASSWORD_FILE, 'r') as file:
        return json.load(file)

def save_passwords(passwords):
    with open(PASSWORD_FILE, 'w') as file:
        json.dump(passwords, file, indent=4)

while True:
    print("What would you like to do?")
    print("1. Generate a new password")
    print("2. Display stored passwords")
    print("3. Exit")
    
    choice = input("Enter your choice (1, 2, or 3): ").strip()
    
    if choice == "1": 
        lower_string = string.ascii_lowercase
        upper_string = string.ascii_uppercase
        spc_char = string.punctuation
        number_int = string.digits

        lower = list(lower_string)
        upper = list(upper_string)
        special = list(spc_char)
        numbers = list(number_int)

        print("Please enter the desired amount for each characteristic of your password.")
        
        while True:
            try:
                n_lower = int(input("Number of lowercase letters: "))
                n_upper = int(input("Number of uppercase letters: "))
                n_numbers = int(input("Number of numbers: "))
                n_spc_chars = int(input("Number of special characters: "))
                
                
                if n_lower < 0 or n_upper < 0 or n_numbers < 0 or n_spc_chars < 0:
                    print("Error: Numbers cannot be negative. Try again.")
                    continue
                
                n_chars = n_lower + n_upper + n_numbers + n_spc_chars
                if n_chars < 9:
                    print("Error: The total length of the password must be at least 9 characters. Try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        
        pw_lower = random.choices(lower, k=n_lower)
        pw_upper = random.choices(upper, k=n_upper)
        pw_numbers = random.choices(numbers, k=n_numbers)
        pw_specials = random.choices(special, k=n_spc_chars)

        pw_chars = pw_upper + pw_lower + pw_numbers + pw_specials
        random.shuffle(pw_chars)

        final_pw = ''.join(pw_chars)
        print("Your auto-generated password is:", final_pw)

        
        hash_object = hashlib.sha256(final_pw.encode())
        print("SHA-256 hash of the password:", hash_object.hexdigest())

        label = input("Enter a label for this password (Email, Bank Account, etc): ").strip()
        passwords = load_passwords()
        passwords[label] = final_pw  
        save_passwords(passwords)
        print(f"Password saved under the label '{label}'.")

    elif choice == "2": 
        passwords = load_passwords()
        if passwords:
            print("Stored Passwords:")
            for label, password in passwords.items():
                print(f"- {label}: {password}")
        else:
            print("No passwords stored yet.")

    elif choice == "3":  
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

