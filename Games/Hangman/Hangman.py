import random
from wordlist import word_list

hang = ["""
H A N G M A N 

   +---+
   |   |
       |
       |
       |
       |
=========""", """
H A N G M A N 

  +---+
  |   |
  O   |
      |
      |
      |
=========""", """
H A N G M A N 

  +---+
  |   |
  O   |
  |   |
      |
      |
=========""", """
H A N G M A N 

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""", """
H A N G M A N 

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""", """
H A N G M A N 

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""", """
H A N G M A N 

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""]



def welcome(): 
    name = input("> Welcome to the game! Please enter a username -> ")
    print(F" >>> Hi {name}! Glad to have you here! <<<")
    print("Today, you will be playing a little game of hangman.")
    print("First, the programm will generate a random word which you have to find by entering single letters.")
    print("Keep in mind that you only have 6 tries so be careful with your predictions.")

def get_word():
    word = random.choice(word_list).lower()
    return word

def play_again(): 
    again = str(input("Do you want to play again? Yes or No? -> ")).lower()
    if again == "yes":
        print("Have fun!")
        pass
    elif again == "no": 
        print("Hope you had fun playing the game. See you next time")
        exit()

def game():

    word = get_word()
    letters_guessed = []
    tries = 6 
    guessed = False

    print()
    print(F"The word contains {len(word)} letters!")
    print(len(word) * "_")



    while guessed == False and tries > 0: 
        print(F"You have {tries} tries.")
        guess = input("Guess a letter or a word!").lower()

        if len(guess) == 1: 

            if guess.isalpha == False: 
                print("Please enter a valid character! (Only letters) ")
            elif guess not in word: 
                print("That letter is not part of the word :C")





game()
