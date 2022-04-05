# PasswordGenerator
# by Mathis 
import random 
import string

print()
print("Welcome to the Passwort Generator!")
print()
length = int(input("How many characters should be included? -> "))
check_type = int(input("Which characters should be included?\n all characters: 1\n only numbers: 2 \n only letters: 3 \n -> "))

def generate(check_type, length):
    letters = string.ascii_letters
    numbers = string.ascii_letters + string.digits
    allcharacterss = string.ascii_letters + string.digits + string.punctuation

    match check_type: 
        case 1: 
            passwort = "".join(random.choice(allcharacterss) for i in range (length))
            print(passwort)          
        case 2: 
            passwort = "".join(random.choice(numbers) for i in range (length))
            print(passwort)
        case 3: 
            passwort = "".join(random.choice(letters) for i in range (length))
            print(passwort)

generate(check_type, length)
