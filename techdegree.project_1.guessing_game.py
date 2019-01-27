"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random

high_score = [0]
def new_high_score(number_of_guesses):
  high_score.append(number_of_guesses)
  if high_score[0] == 0:
    high_score.pop(0)
  elif high_score[0] < high_score[1]:
    high_score.pop(1)
  elif high_score[0] > high_score[1]:
    high_score.pop(0)
    

def start_game():
  """Psuedo-code Hints
  
  When the program starts, we want to:
  ------------------------------------
  1. Display an intro/welcome message to the player.
  2. Store a random number as the answer/solution.
  3. Continuously prompt the player for a guess.
    a. If the guess greater than the solution, display to the player "It's lower".
    b. If the guess is less than the solution, display to the player "It's higher".
  
  4. Once the guess is correct, stop looping, inform the user they "Got it"
       and show how many attempts it took them to get the correct number.
  5. Let the player know the game is ending, or something that indicates the game is over.
  
  ( You can add more features/enhancements if you'd like to. )
  """
  # write your code inside this function.

  print("Welcome to the Number Guessing Game!")
  print("Play by guessing a number between 1 and 10. If you guess right, you win!")
  solution = random.randint(1,10)
  number_of_guesses = int(0)
  if high_score[0] > 0:
    print("This is the current high score: {}".format(high_score[0]))
    print("Can you guess the correct number with fewer guesses?")
  else:
    print("There is currently no high score.")

  while True:
    try:
      guessed_number = int(input("What number would you like to guess?  >>  "))
    except ValueError:
      print("Invalid guess. Please enter a valid number between 1 and 10.")
    else:
      try:
        if guessed_number < 1:
          raise ValueError("You cannot guess a number lower than 1.")
        if guessed_number > 10:
          raise ValueError("You cannot guess a number greater than 10.")
      except ValueError as err:
        print("{} Please enter a valid number between 1 and 10.".format(err))
      else:
        number_of_guesses += 1
        if guessed_number > solution:
          print("Your number is too high! Try again.")
        elif guessed_number < solution:
          print("Your number is too low! Try again.")
        else:
          if number_of_guesses == 1:
            print("Congratulations! You got it! You guessed 1 time. Thanks for playing!")
          else:
            print("Congratulations! You got it! You guessed {} times. Thanks for playing!".format(number_of_guesses))
          break
  play_again = input("Would you like to play again? (Y)es or (N)o >>  ")
  while True:
    if play_again.lower() == "y":
      new_high_score(number_of_guesses)
      start_game()
      break
    elif play_again.lower() == "n":
      print("Too bad. See you next time!")
      break
    else:
      play_again = input("Please choose 'Y' for yes or 'N' for no. >>  ")
      continue
  
if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game() 