# 2. Task List Manager (with separate module)
import tasks

task_list = []

# welcome message
print("WELCOME TO THE TASK LIST MANAGER!\nYou can use these commands:\n* 'add' to add a task to the list.\n* 'remove' to remove a task from the list.\n* 'done' to quit the task list manager.")

# handling commands
command = ""
while not (command == "done"):
  command = input("\nWhat do you want to do?\n")
  if (command == "add"): # add task
    task = input("Which task do you want to add?\n")
    print(f"{tasks.add_task(task_list,task)}\nCurrent task list: {task_list}")
  elif (command == "remove"): # remove task
    task = input("Which task do you want to remove?\n")
    print(f"{tasks.remove_task(task_list,task)}\nCurrent task list: {task_list}")
  elif (command == "done"): # quit
    print("    // \n  _oo\ \n (__/ \ \nThank you for using the task manager.")
  else: # command not recognized
    print("Wrong command, please try again.")