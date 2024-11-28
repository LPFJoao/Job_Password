import string


def mot_pass_valid (mot_pass):
        
        mot_pass_ok = True
    
        if len(mot_pass) >= 8:
            pass

        else:
            mot_pass_ok = False
            print("Lenght of Password needs to be 8 or above characters")
            
        if any(character.isupper() for character in mot_pass):
            pass

        else:
            mot_pass_ok = False             
            print ("Password need atleast 1 capital letter")
        if any(character.islower() for character in mot_pass):

            pass

        else:
            mot_pass_ok = False
            print ("Password need atleast 1 Lower letter")

        if any(character.isdigit() for character in mot_pass):
            pass

        else:
             print ("Password need atleast 1 number")
        if any(character in string.punctuation for character in mot_pass):
            pass

        else:
            mot_pass_ok = False
            print ("Password need atleast 1 special character")

        return mot_pass_ok 
while True:
    mot_pass = input(" Veuillez entrer votre mot de pass : ")

    if mot_pass_valid(mot_pass):
        print("mot pass ok")
        break
    else:
        print("try again")

import hashlib

hash_object = hashlib.sha256(mot_pass.encode())
print(hash_object.hexdigest())
