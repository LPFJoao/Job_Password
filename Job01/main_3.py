import string
import hashlib
import json
import os

PASSWORD_FILE = "mot_pass.json"

def load_passwords():

    if not os.path.exists(PASSWORD_FILE):
        return {}
    with open(PASSWORD_FILE, 'r') as file:
        return json.load(file)
    
def save_passwords(passwords):
    with open(PASSWORD_FILE, 'a') as file:
        json.dump(passwords, file, indent=4)


def mot_pass_valid(mot_pass):
    
    mot_pass_ok = True

    
    if len(mot_pass) < 8:
        print("Length of password needs to be 8 or more characters.")
        mot_pass_ok = False
    
    if not any(character.isupper() for character in mot_pass):
        print("Password needs at least one uppercase letter.")
        mot_pass_ok = False
    
    if not any(character.islower() for character in mot_pass):
        print("Password needs at least one lowercase letter.")
        mot_pass_ok = False
   
    if not any(character.isdigit() for character in mot_pass):
        print("Password needs at least one number.")
        mot_pass_ok = False
    
    if not any(character in string.punctuation for character in mot_pass):
        print("Password needs at least one special character.")
        mot_pass_ok = False
        
    return mot_pass_ok





while True:
    mot_pass = input("Veuillez entrer votre mot de passe : ")

    if mot_pass_valid(mot_pass):
        print("Mot de passe valide!")
        break
    else:
        print("Essayez encore.")


hash_object = hashlib.sha256(mot_pass.encode())
print("SHA-256 hash of the password:", hash_object.hexdigest())

label = input("Enter a label for this password (Email, Bank Account, etc): ").strip()
passwords = load_passwords()
password_hash = hash_object.hexdigest()
passwords[label] =  {"password" : mot_pass, "hash" :  password_hash}
save_passwords(passwords)
print(f"Password saved under the label '{label}'.")
