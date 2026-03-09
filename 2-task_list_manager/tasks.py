# Create a Python module named tasks.py that contains two functions:
# * add_task(task_list, task)
# * remove_task(task_list, task)
def add_task(task_list, task):
  if (task in task_list):
    return "The task was already in the task list."
  else:
    task_list.append(task)
  return "Task added."

def remove_task(task_list, task):
  try:
    task_list.remove(task)
    return "The task is removed from the task list."
  except ValueError as err:
    return "The task is not in the task list."

