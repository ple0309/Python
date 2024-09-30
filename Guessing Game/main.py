#Author: Jaden Le, Peter Tawfik, James Flores
#Date: Aug 26 2024
#Description: Guessing a number between 1-100
import check_input
import random


def main():
  done = False
  count = 1
  val = random.randint(1, 100)
  print("- Guessing Game -")
  print("I'm thinking of a number. Make a guess (1-100): ", end="")
  guess = int(input(""))

  #The loop for checking the val number by inputting the guess number.
  #The loop will stop when the guess number is equal to the val number.
  #Then the variable done will return True to stop the loop.
  while not done:
    if guess == val:
      print("Correct! You got it in " + str(count) + " tries.")
      done = True
    elif (guess < 1 or guess > 100):
      print("Invalid input - should be within range 1-100.")
      guess = check_input.get_int_range("Guess again (1-100): ", 1, 100)
    else:
      print("Too low! " if guess < val else "Too high! ", end="")
      guess = check_input.get_int("Guess Again (1-100): ")
      count += 1


main()
