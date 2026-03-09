# 2. Task List Manager (with separate module)
# Create a Python module named tasks.py that contains two functions:
# * add_task(task_list, task)
# * remove_task(task_list, task)
# In your main script, import tasks.py.
# Start with an empty list, repeatedly ask the user for input: "add " or "remove ".
# Use the imported functions to modify the list, and print the updated list after each operation.
# Exit when the user types "done".
import tasks

task_list = []
print("WELCOME TO THE TASK LIST MANAGER!\nYou can use these commands:\n* 'add' to add a task to the list.\n* 'remove' to remove a task from the list.\n* 'done' to quit the task list manager.")
command = ""
while not (command == "done"):
  command = input("\nWhat do you want to do?\n")
  if (command == "add"):
    task = input("Which task do you want to add?\n")
    print(tasks.add_task(task_list,task))
  elif (command == "remove"):
    task = input("Which task do you want to remove?\n")
    print(tasks.remove_task(task_list,task))
  elif (command == "done"):
    print("    // \n  _oo\ \n (__/ \ \nThank you for using the task manager..")
  else:
    print("Wrong command, please try again.")


#    //
#  _oo\
# (__/ \ 