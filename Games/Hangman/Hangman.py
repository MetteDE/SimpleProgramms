# Hangman
# by Mathis 

import random
from wordlist import word_list

class bcolors:
    RED = "\u001b[31m"
    GREEN = "\u001b[32m"
    DEFAULT = "\033[0m"

hang = ["""
H A N G M A N 

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""
,
"""
H A N G M A N 

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========="""
,
"""
H A N G M A N 

  +---+
  |   |
  O   |
 /|\  |
      |
      |
========="""
,
"""
H A N G M A N 

  +---+
  |   |
  O   |
 /|   |
      |
      |
========="""
,
"""
H A N G M A N 

  +---+
  |   |
  O   |
  |   |
      |
      |
========="""
,
"""
H A N G M A N 

  +---+
  |   |
  O   |
      |
      |
      |
========="""
,
"""
H A N G M A N 

   +---+
   |   |
       |
       |
       |
       |
========="""]



def welcome(): 
    name = input("> Welcome to the game! Please enter a username -> ")
    print(F" >>> Hi {name}! Glad to have you here! <<<")
    print("Today, you will be playing a little game of hangman.")
    print("First, the programm will generate a random word which you have to find by entering single letters.")
    print(F"Keep in mind that you only have {len(hang)} tries so be careful with your predictions.")

def get_word():
    word = random.choice(word_list).lower()
    return word

def play_again(): 
    again = str(input(F"Do you want to play again? {bcolors.GREEN} Yes {bcolors.DEFAULT} or {bcolors.RED} No? {bcolors.DEFAULT} -> ")).lower()
    if again == "yes":
        print("Have fun!")
        game()
    elif again == "no": 
        print(bcolors.GREEN + "Hope you had fun playing the game. See you next time" + bcolors.DEFAULT)
        exit()

def game():

    welcome()
    word = get_word()
    letters_guessed = []
    tries = len(hang)
    guessed = False

    print()
    print(F"The word contains {len(word)} letters!")
    print(len(word) * "_")



    while guessed == False and tries > 0: 
        print(F"You have {tries} tries.")
        guess = input("Guess a letter or a word! -> ").lower()


        # if user enters only a letter 
        if len(guess) == 1: 

            if guess.isalpha == False: 
                print(bcolors.RED + "Please enter a valid character! (Only letters) " + bcolors.DEFAULT)

            elif guess not in word: 
                print(bcolors.RED +"That letter is not part of the word :C" + bcolors.DEFAULT)
                letters_guessed.append(guess)
                tries -= 1
                print(hang[tries])

            elif guess in word: 
                print(bcolors.GREEN + "Great! That letter is part of the word :D " + bcolors.DEFAULT)
                letters_guessed.append(guess)

            elif guess in letters_guessed:
                print(bcolors.RED + F"You already tried the letter {guess} " + bcolors.DEFAULT)

            else: 
                print(bcolors.RED + "There seems to be a problem with your entry! Try it again!" + bcolors.DEFAULT )

        elif len(guess) == len(word): 
            
            if guess == word: 
                print(bcolors.GREEN + "Good job! You guess the correct word " + bcolors.DEFAULT)
            else: 
                print(bcolors.RED +"Thats the wrong word! Try again!" + bcolors.DEFAULT)
                tries -= 1
                print(hang[tries])
        else: 
            print(bcolors.RED + "The length of your guess does not match the length of the final word." + bcolors.DEFAULT)


        status = ""

        if guessed == False: 
            for letter in word:
                if letter in letters_guessed:
                    status += letter
                else: 
                    status += "_"
            print(status.upper())

        if status == word: 
            print(bcolors.GREEN + "Good job! You guess the correct word " + bcolors.DEFAULT)
            guessed = True

        elif tries == 0: 
            print(bcolors.RED + "You ran out of guesses and you couldn't guess the word." + bcolors.DEFAULT)


    play_again()

game()
