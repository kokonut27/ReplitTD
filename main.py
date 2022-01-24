import time
import os
import getkey
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

  if login_i == key_up or login_i == key_left or login_i == "w" or login_i == "a":
    a = current_option_login - 1
    if a == 0:
      current_option_login = 3
    else:
      current_option_login -= 1
  elif login_i == key_down or login_i == key_right or login_i == "s" or login_i == "d":
    a = current_option_login + 1
    if a == 4:
      current_option_login = 1
    else:
      current_option_login += 1
  elif login_i == space or login_i == "s" or login_i == "":
    login_menu = False
    clear()
  clear()

