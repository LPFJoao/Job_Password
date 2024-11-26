import string

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
