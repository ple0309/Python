#Author: Jaden Le, Peter Tawfik
#Date: 09/16/2024
#Description: Finding treasures game. There are 7 treasures
#If we find all treasures, we win. In the other, if we caught trap, we lose.
#Using WASD to move, and Q to quit, and L to look around.


def read_map():
  """
  Reads the map from the file and stores it in list2D.
  Returns:
    A list of list2D after reading the file.
  """
  file = open("map.txt", 'r')
  read_line = file.readlines()
  list2D = []
  for row in read_line:
    items = row.strip().split(" ")
    list = []
    for item in items:
      list.append(str(item))
    list2D.append(list)

  return list2D


def display_map(map, player):
  """
  Displays the map and the user's location.
  Args:
    map: A list of list2D with dots to hide treasures and traps.
    player: A list of two integers with the user's location.
  """
  for row in range(len(map)):
    for cols in range(len(map[0])):
      if row == player[0] and cols == player[1]:
        print('P', end=" ")
      else:
        print(map[row][cols], end=" ")
    print()


def move_player(player, direction, upper_bound):
  """
  Moves the player in the specified direction.
  Args:
    player: A list of two integers with the user's location.
    direction: A direction to move with WASD.
    upper_bound: The maximum and minimum value of the row or column.
  Return:
    A list of new two integers as the new location of the user.
  """

  #Check if the direction is out of bound.
  if player[0] == upper_bound[0] and direction in [
      'W'
  ] or player[0] == upper_bound[1] and direction in [
      'S'
  ] or player[1] == upper_bound[0] and direction in [
      'A'
  ] or player[1] == upper_bound[1] and direction in ['D']:
    print("You can't move there")

  #Calculating the user's location and returning new one if the direction is valid.
  else:
    if direction == "W":
      if player[0] > upper_bound[0]:
        player[0] -= 1
    elif direction == "S":
      if player[0] < upper_bound[1]:
        player[0] += 1
    elif direction == "A":
      if player[1] > upper_bound[0]:
        player[1] -= 1
    else:
      if player[1] < upper_bound[1]:
        player[1] += 1

  return player


def count_treasures_traps(map, player, upper_bound):
  """
  Counts the number of treasures and traps when the user's input is L.
  It will display number of treasures and traps surrounding the user's location.
  Args:
    map: A list of list2D with dots to hide treasures and traps.
    player: A list of two integers with the user's location.
    upper_bound: The maximum and minimum value of the row or column.
  Return:
    Two integers as the number of treasures and traps.
  """
  treasure = 0
  trap = 0

  #Check if the user's location is not out of bound.
  if player[0] >= upper_bound[0] and player[1] >= upper_bound[0] and player[
      0] <= upper_bound[1] and player[1] <= upper_bound[1]:

    #Loop for checking each element in the map.
    for row in range(len(map)):
      for cols in range(len(map[0])):

        #Checking if the element is a treasure or trap surrounds the user's location.
        if row == player[0] and cols == player[1] + 1     or \
           row == player[0] and cols == player[1] - 1     or \
           row == player[0] + 1 and cols == player[1]     or \
           row == player[0] - 1 and cols == player[1]     or \
           row == player[0] + 1 and cols == player[1] + 1 or \
           row == player[0] + 1 and cols == player[1] - 1 or \
           row == player[0] - 1 and cols == player[1] + 1 or \
           row == player[0] - 1 and cols == player[1] - 1:
          if map[row][cols] == "T":
            treasure += 1
          if map[row][cols] == "X":
            trap += 1

        #Not count the user's location.
        if row == player[0] and cols == player[1]:
          continue
  return treasure, trap


def main():
  list2D = read_map()
  list2D_dots = [['.' for i in range(7)] for j in range(7)]
  row_and_cols = [0, 0]
  bound = [0, 6]
  count_traps = 0
  count_treasures = 0
  treasure_remain = 7
  treasure_count = 0
  print("Treasure Hunt!")
  print("Find the 7 treasure withou getting")
  print("caugth in a trap. Look around to spot")
  print("nearby traps and treasures.")
  display_map(list2D_dots, row_and_cols)
  while True:
    print("Enter Direction (WASD or L to look around or Q to quit): ", end="")
    direction = input("").upper()

    #Move player and display the map.
    #If it is treasures, add to the treasures count.
    #Win if all treasures are found and if treasures remaining is 0.
    #If it is traps, it will be lose.
    #Looking around.
    if direction == 'L':
      count_treasures, count_traps = count_treasures_traps(
          list2D, row_and_cols, bound)
      for i in list2D_dots:
        if 'T' in i and count_treasures > 0:
          count_treasures -= 1
        if list2D_dots[row_and_cols[0]][row_and_cols[1]] == '.':
          list2D_dots[row_and_cols[0]][row_and_cols[1]] = str(count_traps)
      print(f"You detect {count_treasures} treasures nearby.")
      print(f"You dectect {count_traps} traps nearby.")

      display_map(list2D_dots, row_and_cols)
      continue
    elif direction in ['W', 'S', 'A', 'D']:
      move_player(row_and_cols, direction, bound)
      if list2D[row_and_cols[0]][row_and_cols[1]] == 'T' and list2D_dots[
          row_and_cols[0]][row_and_cols[1]] != 'T':
        treasure_remain -= 1
        treasure_count += 1
        print("You found treasures.")
        print(f"There are {treasure_remain} treasures remaining.")
        list2D_dots[row_and_cols[0]][row_and_cols[1]] = 'T'
        if treasure_remain == 0:
          print("You win!")
          break
      elif list2D[row_and_cols[0]][row_and_cols[1]] == 'X':
        print("You were caugth in a trap.")
        print(f"You found {treasure_count} treasure.")
        display_map(list2D_dots, row_and_cols)
        print("Game Over.")
        break
      else:
        if list2D_dots[row_and_cols[0]][row_and_cols[1]] == 'T':
          list2D_dots[row_and_cols[0]][row_and_cols[1]] = 'T'

      display_map(list2D_dots, row_and_cols)

    #Quit game
    elif direction == 'Q':
      break

    #Invalid input
    else:
      print("Invalid direction")
      display_map(list2D_dots, row_and_cols)


main()
