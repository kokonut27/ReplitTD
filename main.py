import time
import os
import getkey
import getpass
import cursor
from replit import db


key_up = "\x1b[A"
key_down = "\x1b[B"
key_right = "\x1b[C"
key_left = "\x1b[D"
space = u"\u0020"

red = "\033[0;91m"
w = "\033[0;37m"
black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
magenta = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
bblack = "\033[0;90m"
bred = "\033[0;91m"
bgreen = "\033[0;92m"
byellow = "\033[0;93m"
bblue = "\033[0;94m"
bmagenta = "\033[0;95m"
bcyan = "\033[0;96m"
bwhite = "\033[0;97m"
bold = '\033[1m'
end = '\033[0m'
pink = '\033[95m'
cyan_back = "\033[0;46m"
purple_back = "\033[0;45m"
white_back = "\033[0;47m"
blue_back = "\033[0;44m"
orange_back = "\033[0;43m"
green_back = "\033[0;42m"
pink_back = "\033[0;41m"
grey_back = "\033[0;40m"


def clear(): os.system("clear")

login_menu = True
current_option_login = 1

while True:
  while login_menu:
    print("Will you play as a guest, login, or signup?")
    if current_option_login == 1:
      print(f"{yellow}> Guest{w}")
      print("Login")
      print("Signup")
    elif current_option_login == 2:
      print("Guest")
      print(f"{yellow}> Login{w}")
      print("Signup")
    else:
      print("Guest")
      print("Login")
      print(f"{yellow}> Signup{w}")
    login_i = getkey.getkey()
  
    if login_i in [key_up, key_left, "w", "a"]:
      a = current_option_login - 1
      if a == 0:
        current_option_login = 3
      else:
        current_option_login -= 1
    elif login_i in [key_down, key_right, "s", "d"]:
      a = current_option_login + 1
      if a == 4:
        current_option_login = 1
      else:
        current_option_login += 1
    elif login_i in [space, ""]:
      login_menu = False
      clear()
    clear()
  
  if current_option_login == 2: # Skips option 1 because Guest has no saving option. This may change later on in the future.
    login_menu = True
    while login_menu:
      print("Login")
      username_l = input("Username: ")
      password_l = getpass.getpass(prompt="Password: ")
    
      try:
        test_user = db[username_l]

        if test_user == password_l:
          print(f"{green}Successfully logged in! Logging into game...{w}")
          time.sleep(2)
          clear()
          login_menu = False
    
      except:
        print(f"{red}No such username exists or the password is incorrect! Try again!{w}")
        time.sleep(2)
        clear()
        
  elif current_option_login == 3:
    signup_menu = True
    while signup_menu:
      print("Signup")
      username_s = input("Username: ")
      password_s = getpass.getpass(prompt="Password: ")
      confirm_pass = getpass.getpass(prompt="Confirm password: ")

      if confirm_pass != password_s:
        print(f"{red}Your confirmation password is incorrect! Try again!{w}")
        time.sleep(2)
        clear()
      else:
        try:
          db[username_s] = password_s
  
          print(f"{green}You have successfully created an account! Logging into game...{w}")
          time.sleep(2)
          clear()
          signup_menu = False
        except:
          print(f"{red}There was something wrong with creating an account! Try again!{w}")
          time.sleep(2)
          clear()

  input("hi")