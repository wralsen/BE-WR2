# 6. JSON Settings Handler
#  Create a JSON file settings.json that contains some configuration (e.g., {"theme": "dark", "volume": 80}).
#  Write a script that reads this JSON file using the json module, prints the current settings, and asks the user to change one setting.
#  After the user changes a setting, write the updated JSON back to the file.
#  Handle any file read/write exceptions gracefully.
import os, sys, json

# read file
filename = "settings.json"
# Comment out the next line when not running from VSC (VSC requires path from working directory, not script directory)
filename = "innleveringer/BE_WR2/BE-WR2/6-JSON_settings_handler/"+filename

try:
  io = open(filename, 'r')
  settings = json.load(io)
  io.close()

  # printing current settings
  print("Current settings:")
  for key in settings:
    print(key,":",settings[key])

except (FileNotFoundError):
  print(f"Could not find file {filename}.")

