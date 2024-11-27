

import string

def mot_pass_valid (mot_pass):
    return (
        len(mot_pass) >= 8 and
        any (character.isupper() for character in mot_pass) and
        any (character.islower() for character in mot_pass) and
        any (character.isdigit() for character in mot_pass) and
        any (character in string.punctuation for character in mot_pass)
    )

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