# 6. JSON Settings Handler
#  Create a JSON file settings.json that contains some configuration (e.g., {"theme": "dark", "volume": 80}).
#  Write a script that reads this JSON file using the json module, prints the current settings, and asks the user to change one setting.
#  After the user changes a setting, write the updated JSON back to the file.
#  Handle any file read/write exceptions gracefully.
import os, sys, json

def print_current_settings(settings):
  print("\nCurrent settings:")
  n = 1
  for key in settings:
    print(n,key,":",settings[key])
    n += 1

# welcome message
print("~~ Welcome to the JSON Settings Handler ~~")

filename = "settings.json"
# Comment out the next line when not running from my VSC setup 
filename = "innleveringer/BE_WR2/BE-WR2/6-JSON_settings_handler/"+filename # VSC requires path from working directory, not script directory

try:
  # read file
  io = open(filename, 'r')
  settings = json.load(io)
  io.close()

  print_current_settings(settings)

  print("To change a setting, please enter its number.") 
  print("To exit, type 0.")
  # using numbers instead of keys complicates the code but helps me learn more about dictionaries in Python
  
  setting_to_change = -1
  while not (setting_to_change == 0):
    try:
      setting_to_change = int(input())
      if (setting_to_change > len(settings)): # setting does not exist
        raise ValueError
      elif (setting_to_change == 0): # user wants to quit
        print("Thank you for using the JSON Settings Handler.")
        # update file
        io = open(filename, 'w')
        json.dump(settings, io)
        io.close()
      else: # user has typed a valid integer
        setting_key = list(settings)[setting_to_change-1] # find key
        print(f"You want to change the {setting_key}.")
        new_value = input("Please type the new value:\n")
        settings[setting_key] = new_value # update setting
        print("Setting is updated.")
        print_current_settings(settings)
    except (TypeError, ValueError):
      setting_to_change = input("You did not type a valid integer. Please try again.\n")
except FileNotFoundError:
  print("The setting file could not be found.")

