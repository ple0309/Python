#Author: Peter Tawfik, Jaden Le
#ID Numbers: Peter Tawfik's ID-033266933; Jaden Le's ID-032592883
#Date: September 23, 2024
#Description: Helps user keep track of list of tasks to complete

import task
import check_input


def main_menu():
  """Displays the main menu and gets valid user input."""
  while True:
    print("1. Display current task")
    print("2. Mark current task complete")
    print("3. Postpone current task")
    print("4. Add new task")
    print("5. Save and quit")
    user_input = check_input.get_int_range("Enter Choice: ", 1, 5)
    return user_input


def read_file():
  """Reads tasks from 'tasklist.txt' and returns a sorted list of Task objects."""
  file = open("tasklist.txt", 'r')
  list = []
  for i in file:
    desc, date, time = i.strip().split(",")
    each_task = task.Task(desc, date, time)
    list.append(each_task)
  list.sort()
  return list


def write_file(tasklist):
  """Writes the task list to 'tasklist.txt' using the repr() method."""
  file = open("tasklist.txt", 'w')
  for i in tasklist:
    file.write(repr(i) + "\n")
  file.close()


def get_description():
  """Prompts the user for a valid task."""
  while True:
    desc = input("Enter a task: ")
    if ',' in desc:
      print("Invalid input - should not have comma ','")
    elif desc.strip() == "":
      print("Invalid input - should not be an empty.")
    else:
      break
  return desc


def get_date():
  """Prompts the user for a valid date in MM/DD/YYYY format."""
  print("Enter new due date:")
  month = check_input.get_int_range("Enter month: ", 1, 12)
  day = check_input.get_int_range("Enter day: ", 1, 31)
  year = check_input.get_int_range("Enter year: ", 2000, 2100)
  return (f"{month:02d}/{day:02d}/{year:04d}")


def get_time():
  """Prompts the user for a valid time in HH:MM format."""
  print("Enter new time:")
  hour = check_input.get_int_range("Enter hour: ", 0, 23)
  minute = check_input.get_int_range("Enter minute: ", 0, 59)
  return (f"{hour:02d}:{minute:02d}")


def main():
  """Main function to run the task list program."""
  list = read_file()
  while True:
    print("-Tasklist-")
    print(f"You have {len(list)} tasks.")
    user_input = main_menu()

    #Input 1,2,3
    #Showing message when no task.
    if user_input in [1, 2, 3]:
      if len(list) == 0:
        print("All tasks are complete.\n")
      else:
        if user_input == 1:
          print("Current task is: ")
          print(list[0])
          print()
        elif user_input == 2:
          print("Marking current task as complete: ")
          print(list[0])
          list.pop(0)
          if len(list) == 0:
            print("All tasks are complete.\n")
          else:
            print("New current task is: ")
            print(list[0])
            print()
        elif user_input == 3:
            print(f"Postponing task:\n{list[0]}")
            new_date = get_date()
            new_time = get_time()
            new_task = task.Task(list[0].description, new_date, new_time)
            list.pop(0)  # Remove the current task
            list.append(new_task)
            list.sort()  # Re-sort the list


    #Input 4
    #Getting a new task in list.
    elif user_input == 4:
      desc = get_description()
      date = get_date()
      time = get_time()
      new_task = task.Task(desc, date, time)
      list.append(new_task)
      list.sort()

    #Input 5
    else:
      write_file(list)
      print("Saving and exiting.")
      break


main()
