# 6. JSON Settings Handler
import os, sys, json

def print_current_settings(settings):
  print("\nCurrent settings:")
  n = 1
  for key in settings:
    print(n,key,":",settings[key])
    n += 1
  print("\n")

# welcome message
print("~~ Welcome to the JSON Settings Handler ~~")

try: # read file
  filename = "innleveringer/BE-WR2/6-JSON_settings_handler/settings.json" # Note: VSC requres path from working directory, not script directory
  io = open(filename, 'r')
  settings = json.load(io)
  io.close()

  print_current_settings(settings)
  print("Enter the number of the setting you want to change.") 
  
  try:
    setting_to_change = int(input()) # throws exeption if input is not integer
    if (setting_to_change < 1) or (setting_to_change > len(settings)): # setting does not exist
      raise ValueError
    else: # user has typed a valid integer
      setting_key = list(settings)[setting_to_change-1] # find key
      print(f"You want to change the {setting_key}.")
      new_value = input("Please type the new value:\n")
      settings[setting_key] = new_value # update setting
      print("Setting is updated.") # user feedback is important
      print_current_settings(settings)
  except TypeError:
    print("You did not type an integer.")
  except ValueError:
    print("You did not type a number corresponding to a setting.")

  # update file
  io = open(filename, 'w')
  json.dump(settings, io)
  io.close()
  print("Thank you for using the JSON Settings Handler.")

except FileNotFoundError:
  print("The JSON settings file could not be found.")
