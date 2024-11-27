import string
import hashlib
import random
import hashlib


lower_string = string.ascii_lowercase
upper_string = string.ascii_uppercase
spc_char = string.punctuation
number_int = string.digits

lower = list(lower_string)
upper = list(upper_string)
special = list(spc_char)
numbers = list(number_int)


print("Please enter the following desired amount regarding the charecteristics of your password")
n_lower = int(input("Number of lower case letters : "))
n_upper = int(input("Number of upper case letters : "))
n_numbers = int(input("Number of numbers : "))
n_spc_chars = int(input("Number of special charcters: "))

def valid_pw(n_chars):

    pw_ok = True

    if n_lower >= 3:
        pass
    else:
        print("The number of lower case letter needs to be 3 or greater")

    if n_upper >= 3:
        pass
    else:
        print("The number of upper case letter needs to be 3 or greater")

    if n_numbers >= 2:
        pass
    else:
        print("The number of Numbers in the password needs to be 2 or greater")

    if n_spc_chars >= 1:
        pass
    else:
        print("The number of special characters in the password needs to be 1 or greater")

    if n_chars < 9:
        print("Length of password needs to be 9 or more characters.")
        pw_ok = False

    return pw_ok


while True:

    n_chars = n_lower + n_upper + n_numbers + n_spc_chars
    
    if valid_pw(n_chars):
        print("Password is valid")
        break

    else:
        print("Essayez encore.")


pw_lower = random.sample(lower, n_lower)
pw_upper = random.sample(upper, n_upper)
pw_numbers = random.sample(numbers, n_numbers)
pw_specials = random.sample(special, n_spc_chars)

pw_chars = pw_upper + pw_lower + pw_numbers + pw_specials

random.shuffle(pw_chars)

final_pw = ''.join(pw_chars)


print("Your auto generated password is : ", final_pw)


hash_object = hashlib.sha256(final_pw.encode())
print(hash_object.hexdigest())