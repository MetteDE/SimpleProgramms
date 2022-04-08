import random

class bcolors:
    RED = "\u001b[31m"
    GREEN = "\u001b[32m"
    DEFAULT = "\033[0m"

def game():
    attemps = 0
    print("Try to find the number between 0 and 100")
    goal = random.randint(0, 101)
    while True:
        guess = int(input("Enter your guess! -> "))
        attemps += 1
        if guess == goal: 
            print(bcolors.GREEN+ F"Congratulations! You found the number after {attemps} attemps!" + bcolors.DEFAULT)
            break
        elif guess < goal: 
            print(bcolors.RED + "Too low! Chose a HIGHER number!\n" + bcolors.DEFAULT)

        elif guess > goal: 
            print(bcolors.RED + "Too high! Chose a LOWER number!\n" + bcolors.DEFAULT)

print("Welcome to the number guessing game!")
game()


        
