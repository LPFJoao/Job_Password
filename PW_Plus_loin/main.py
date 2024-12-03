import string
import random
import hashlib
import json
import os

PASSWORD_FILE = "passwords.json"

def load_passwords():
    if not os.path.exists(PASSWORD_FILE):
        return {}  
    with open(PASSWORD_FILE, 'r') as file: #'r' is the mode on what the file open for: on this case is open on read mode only

        return json.load(file)

def save_passwords(passwords):
    with open(PASSWORD_FILE, 'w') as file: #'a' is the mode on what the file open for: on this case is open on append mode which doensr overwrite
        json.dump(passwords, file, indent=4)

while True:
    print("What would you like to do?")
    print("a. Generate a new password")
    print("b. Input your own password")
    print("c. Display stored passwords")    
    print("d. Exit")
    
    Option = input("Enter your Option (a, b, c or d): ").strip().lower()
    
    if Option == "a": 
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
        
        
        pw_lower = random.Options(lower, k=n_lower)
        pw_upper = random.Options(upper, k=n_upper)
        pw_numbers = random.Options(numbers, k=n_numbers)
        pw_specials = random.Options(special, k=n_spc_chars)

        pw_chars = pw_upper + pw_lower + pw_numbers + pw_specials
        random.shuffle(pw_chars)

        final_pw = ''.join(pw_chars)
        print("Your auto-generated password is:", final_pw)

        
        hash_object = hashlib.sha256(final_pw.encode())
        print("SHA-256 hash of the password:", hash_object.hexdigest())

        label = input("Enter a label for this password (Email, Bank Account, etc): ").strip()
        passwords = load_passwords()
        password_hash = hash_object.hexdigest()
        passwords[label] = { "password" : final_pw, "hash" :  password_hash}  
        save_passwords(passwords)
        print(f"Password saved under the label '{label}'.")

    elif Option == "b":
        def final_pw_valid(final_pw):
    
            final_pw_ok = True

    
            if len(final_pw) < 8:
                print("Length of password needs to be 8 or more characters.")
                final_pw_ok = False
    
            if not any(character.isupper() for character in final_pw):
                print("Password needs at least one uppercase letter.")
                final_pw_ok = False
    
            if not any(character.islower() for character in final_pw):
                print("Password needs at least one lowercase letter.")
                final_pw_ok = False
   
            if not any(character.isdigit() for character in final_pw):
                print("Password needs at least one number.")
                final_pw_ok = False
    
            if not any(character in string.punctuation for character in final_pw):
                print("Password needs at least one special character.")
                final_pw_ok = False
        
            return final_pw_ok

        while True:
            final_pw = input("Veuillez entrer votre mot de passe : ")

            if final_pw_valid(final_pw):
                print("Mot de passe valide!")
                break
            else:
                print("Essayez encore.")

            print("Your auto-generated password is:", final_pw)

        
        hash_object = hashlib.sha256(final_pw.encode())
        print("SHA-256 hash of the password:", hash_object.hexdigest())

        label = input("Enter a label for this password (Email, Bank Account, etc): ").strip()
        passwords = load_passwords()
        password_hash = hash_object.hexdigest()
        
        if any(entry.get("hash") == password_hash for entry in passwords.values()):
            print("This password already exists in the database. Please try a different one.")

        else:
           passwords[label] =  {"password" : final_pw, "hash" :  password_hash}
           save_passwords(passwords)
           print(f"Password saved under the label '{label}'.")

     
    elif Option == "c": 
        passwords = load_passwords()
        if passwords:
            print("Stored Passwords:")
            for label, password in passwords.items():
                print(f"- {label}: {password}")
        else:
            print("No passwords stored yet.")

    
    elif Option == "d":  
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid Option. Please enter a, b, or c.")

