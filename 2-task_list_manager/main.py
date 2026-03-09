# 2. Task List Manager (with separate module)
import tasks

task_list = []

# welcome message
print("WELCOME TO THE TASK LIST MANAGER!")
print("You can use these commands:")
print("* 'add' to add a task to the list.")
print("* 'remove' to remove a task from the list.")
print("* 'done' to quit the task list manager.")

# handling commands
command = ""
while not (command == "done"):
  command = input("\nWhat do you want to do?\n")
  if (command == "add"): # add task
    task = input("Which task do you want to add?\n")
    print(f"{tasks.add_task(task_list,task)}\nCurrent task list: {task_list}")
  elif (command == "remove"): # remove task
    task = input("Which task do you want to remove?\n")
    print(f"{tasks.remove_task(task_list,task)}")
    print("Current task list: {task_list}")
  elif (command == "done"): # quit
    print("    // \n  _oo\ \n (__/ \ ")
    print("Thank you for using the task manager.")
  else: # command not recognized
    print("Wrong command, please try again.")