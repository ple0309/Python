#Author: Jaden Le, Peter Tawfik
#Date: 09/04/24
#Decription: Gaming with Rock,Paper and Scissors.
#Rock crushes Scissors. Paper covers Rock. Scissors cut Paper.
#If the same weapon will be tie.
#This program allows the user to play against the computer.
#It keeps track of the score and allows the user to quit when desired.
import check_input
import random


def player():
  """
  Displays the weapon menu.
  Checks the input for validity and returns the valid input.

  Returns:
    str: The choice of player (R,P,S or B)
  """
  while True:
    print("Choose your weapon:")
    print("R. Rock")
    print("P. Paper")
    print("S. Scissors")
    print("B. Back")
    choice_weapon = input("").upper()
    if choice_weapon in ['R', 'P', 'S', 'B']:
      return choice_weapon
    else:
      print("Invalid weapon! Choosing again!")


def comp():
  """
  Randomly selects the computer's weapon

  Return:
    str: The choice of computer(R,P or S)
  """
  return random.choice(['R', 'P', 'S'])


def find_winner(player, comp):
  """
  Determines the winner of a round based on the player's and computer's weapons.
  
  Args:
    player(str): The player's weapon choice(R,P or S)
    comp (str) : The computer's weapon choice(R,P or S)

  Return:
    int: The result of the round(0 = Tie, 1 = Players wins, 2 = Computer wins)
  """
  if player == comp:
    print("Tie")
    return 0
  elif (player == 'R' and comp == 'S' or player == 'P' and comp == 'R'
        or player == 'S' and comp == 'P'):
    print("Player wins")
    return 1
  else:
    print("Computer wins")
    return 2


def display_scores(player, comp):
  """
  Displays the current scores of the player and the computer.

  Args:
    player (int): The player's current score.
    comp_score(int): The computer's current score.
  """
  print("Player = ", player)
  print("Computer = ", comp)


def main():
  """
  Main function to run the Rock-Paper-Scissors game. It displays a menu, allows the user
  to play, and keeps track of scores until the user decides to quit.
  """
  weapon = {
      'R': "Rock",
      'P': "Paper",
      'S': "Scissors"
  }  #Dictionary to simplify the line code.
  player_count = 0
  comp_count = 0

  while True:
    choice = check_input.get_int("RPS Menu:\n"
                                 "1.Play game\n"
                                 "2.Show Scores\n"
                                 "3.Quit\n")
    #Play games.
    if choice == 1:
      while True:
        player_choice = player()
        if player_choice == 'B':  #Back to the menu.
          break
        else:
          if player_choice in weapon:
            print(f"Player chose {weapon[player_choice]}")
          comp_choice = comp()
          if comp_choice in weapon:
            print(f"Computer chose {weapon[comp_choice]}")
          winner = find_winner(player_choice, comp_choice)
          if winner == 1:
            player_count += 1
          if winner == 2:
            comp_count += 1

    #Show Score.
    elif choice == 2:
      display_scores(player_count, comp_count)

    #Quit Game and Show the final scores.
    elif choice == 3:
      print("Final Score:")
      display_scores(player_count, comp_count)

      break
    #Input again
    else:
      print("Invalid input - should be within range 1-3.")


main()
