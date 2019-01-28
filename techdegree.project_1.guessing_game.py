"""
lmapple
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
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
  elif high_score[0] = high_score[1]:
    high_score.pop(1)
    
    
def start_game():
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
  start_game() 
