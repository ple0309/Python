#Author: Jaden Le, Peter Tawfik
#Student's ID: Jaden Le: 032592883, Peter Tawfik: 033266933
#Date: 09/30/2024
#Description: This game will roll 3 dices.
#The game will automatically add points if it has pair, three kind or series.

import check_input
import player
def take_turn(player):
  """Rolling player's dice and display numbers of 3 dies.
  If it has pair, series or three of a kinds.
  Display the updated the score.
  """
  player.roll_dice()
  print()
  print(player)
  if player.has_three_of_a_kind():
    print("You got 3 of a kind.")
  elif player.has_pair():
    print("You got a pair!")
  elif player.has_series():
    print(f"You got a series of 3 !")
  else:
    print("Aww. Too bad.")
  print(f'Score = {player.get_points()}')

def main():
  player_dice = player.Player() #Create player object with 3 defaul dies.
  yes_no = True
  print("-Yahtzee-")
  take_turn(player_dice) #Rolling dice and display the numbers.

  #Loop of game with yes or no option.
  while yes_no:
    yes_no = check_input.get_yes_no("Play again? (Y/N): ")
    if yes_no == False:
      print("\nGame Over.")
      print(f'Final Score = {player_dice.get_points()}')
      break
    take_turn(player_dice)
main()