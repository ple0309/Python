#Author: Jaden Le, Peter Tawfik
#Date: 9/9/2024
#Description:
import check_input
import random
from dictionary import words
#try to change


def display_gallows(num_incorrect):

  row = [['|', '|', ' ', ' ', ' ', ' ', ' ', ' '],
         ['|', '|', ' ', ' ', ' ', ' ', ' ', ' '],
         ['|', '|', ' ', ' ', ' ', ' ', ' ', ' '],
         ['|', '|', ' ', ' ', ' ', ' ', ' ', ' ']]
  print("========")
  print("||/   |")

  if num_incorrect >= 1:
    row[0][6] = 'o'
  if num_incorrect >= 2:
    row[1][6] = '|'
  if num_incorrect >= 3:
    row[2][5] = '/'
  if num_incorrect >= 4:
    row[2][7] = "\\"
  if num_incorrect >= 5:
    row[0][5] = "\\"
  if num_incorrect >= 6:
    row[0][7] = '/'
  for i in row:
    for j in i:
      print(j, end="")
    print()


def display_letters(letters):
  for i in letters:
    print(i, end=" ")
  print("\n")


def get_letters_remaining(incorrect, correct):
  list = []
  list.append(incorrect)
  list.append(correct)
  return list


def main():
  print("-Hangman-\n")
  repeat = True
  while repeat is True:
    letters = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    random_words = random.choice(words)
    num_incorrect = 0
    num_correct = 0
    incorrect_guess = []
    correct_guess = ['_', '_', '_', '_', '_']
    while True:
      print("Incorrect selection: ", end="")
      display_letters(incorrect_guess)
      display_gallows(num_incorrect)
      print()
      display_letters(correct_guess)
      print("\nLetter remaining: ", end="")
      list = get_letters_remaining(incorrect_guess, correct_guess)

      for i in list:
        for val in i:
          if val in letters:
            letters.remove(val)
      for i in letters:
        print(i, end=" ")
      print()
      guess_letter = input("\nEnter a letter: ").upper()

      if guess_letter.isalpha() != 1 or len(guess_letter) != 1:
        print("This is not a letter.")
      else:
        if guess_letter in incorrect_guess or guess_letter in correct_guess:
          print("You have already used that letter.")
        elif guess_letter in random_words:
          print("Correct!\n")
          for i in range(len(random_words)):
            if random_words[i] == guess_letter:
              correct_guess[i] = guess_letter
              num_correct += 1
        else:
          print("Incorrect!\n")
          incorrect_guess.append(guess_letter)
          incorrect_guess.sort()
          num_incorrect += 1
      if num_correct == 5:
        display_gallows(num_incorrect)
        print()
        display_letters(correct_guess)
        print("\nYou win!")
        break
      if num_incorrect == 6:
        display_gallows(num_incorrect)
        print()
        display_letters(random_words)
        print("\nYou lose!")
        break
    repeat = check_input.get_yes_no("Play again (Y/N) ? ")
    print()
    if repeat in ['y', 'Y', 'n', 'N']:
      repeat = True


main()
