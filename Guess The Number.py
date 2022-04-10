#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

# from art import logo
logo=''' 
                           ('-.    .-')     .-')                   .-') _   ,---. 
                         _(  OO)  ( OO ).  ( OO ).                (  OO) )  |   | 
  ,----.    ,--. ,--.   (,------.(_)---\_)(_)---\_)        ,-.-') /     '._ |   | 
 '  .-./-') |  | |  |    |  .---'/    _ | /    _ |         |  |OO)|'--...__)|   | 
 |  |_( O- )|  | | .-')  |  |    \  :` `. \  :` `.         |  |  \'--.  .--'|   | 
 |  | .--, \|  |_|( OO )(|  '--.  '..`''.) '..`''.)        |  |(_/   |  |   |  .' 
(|  | '. (_/|  | | `-' / |  .--' .-._)   \.-._)   \       ,|  |_.'   |  |   `--'  
 |  '--'  |('  '-'(_.-'  |  `---.\       /\       /      (_|  |      |  |   .--.  
  `------'   `-----'     `------' `-----'  `-----'         `--'      `--'   '--'  

'''
 
  
print(logo)
import random

print("Welcome to the number guessing game!\nI am thinking of a number between 1 to 100\nChose a difficulty mode and start guessing. Type 'easy' or 'hard':")
number=random.randint(1,100)
level=input()
if level=="easy":
  attempt=10
else:
  attempt=5
print(f"You have {attempt} attempts remaining to guess the number\nMake a guess:")  
guess=int(input())

def compare(guess,number,attempt):
 
  if guess == number:
    print(f"You got it! The answer was {number}.")
    return 0
    
  elif guess>number:
    attempt-=1
    print("Too high.")
    if attempt>0:
      print(f"Guess again.\nYou have {attempt} attempts remaining to guess the number.\nMake a guess:")
    else:
      print("You've run out of guesses. You lose.")
      return 0
    guess1=int(input())
    compare(guess1,number,attempt)
  else:
    attempt-=1
    print("Too low.")
    if attempt>0:
      print(f"Guess again.\nYou have {attempt} attempts remaining to guess the number.\nMake a guess:")
    else:
      print("You've run out of guesses. You lose.")
      return 0
    guess1=int(input())
    compare(guess1,number,attempt)
m=compare(guess,number,attempt)