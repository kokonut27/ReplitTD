import time
import os
import random
import getkey
import getpass
import cursor
import socket
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

replit_talk_map = [
  "corner", 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
  9, "p", "p", "p", "p", "p", "p", "p", "p", 99, 99, 99, 99, 99, 99, 99, 99, 0, 0, 0, 0, 10,
  9, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "p", 99, 99, 99, 0, 0, 0, 0, 10,
  9, 3, 0, "p", 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 0, 0, 0, 0, 10,
  9, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "p", 99, 99, 99, 0, 0, 0, 0, 10,
  9, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "p", "p", "p", 99, 99, 99, 99, 99, 10,
  9, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, "p", 99, 99, 99, 99, 99, 99, 99, 99, 99, 10,
  9, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "p", 99, 99, 99, 99, 99, 10,
  9, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "p", 99, 99, 99, 99, 99, 99, 99, 99, 10,
  9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "p", "p", "p", "p", 99, 99, 99, 99, 10,
  9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "p", 0, 0, 0, 0, 0, 0, 99, 10,
  9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "p", 0, 0, 0, 0, 0, 0, 99, 10,
  9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "p", 0, 0, 0, 0, 0, 0, 99, 10,
  9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "p", 0, 0, 0, 0, 0, 0, 99, 10,
  9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "p", "p", "p", "p", 99, 99, 99, 99, 10, 
  # 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10
]

replit_home_map = [
  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
  1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
  1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
  1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
  1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
  1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
  1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
  1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
  1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
  1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
  1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
  1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
  1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
  1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
  1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 
  # 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
]

python_repl_map = [
  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
  1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
  1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
  1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
  1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
  1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
  1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
  1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
  1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
  1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
  1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
  1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
  1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
  1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
  1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 
  #  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
]

def print_map(themap):
  _end = ""
  i = 0
  side_num = 0
  letter = "a"
  for x in themap:
    i += 1
    side_num += 1
    if i == 22: 
      _end = "\n"
      i = 0
      if side_num == 22:
        letter = "b"
      elif side_num == 44:
        letter = "c"
      elif side_num == 66:
        letter = "d"
      elif side_num == 88:
        letter = "e"
      elif side_num == 110:
        letter = "f"
      elif side_num == 132:
        letter = "g"
      elif side_num == 154:
        letter = "h"
      elif side_num == 176:
        letter = "i"
      elif side_num == 198:
        letter = "j"
      elif side_num == 220:
        letter = "k"
      elif side_num == 242:
        letter = "l"
      elif side_num == 264:
        letter = "m"
      elif side_num == 286:
        letter = "n"
      elif side_num == 308:
        letter = "o"
      elif side_num == 330:
        letter = "p"
    else: 
      _end = ""
    if themap == replit_talk_map:
      if x == "corner":
        print(" ", end = _end)
      if x == 0:
        print(" ", end = _end)
      if x == 9:
        print(letter, end = "")
      if x == 1:
        if side_num >= 10:
          if side_num == 10:
            print()
        else:
          print(side_num, end = _end)
      elif x == 2:
        print(white_back + blue + "All" + w, end = _end)
      elif x == 3:
        print(white_back + blue + "Announcements" + w, end = _end)
      elif x == 4:
        print(white_back + blue + "Ask" + w, end = _end)
      elif x == 5:
        print(white_back + blue + "Jam" + w, end = _end)
      elif x == 6:
        print(white_back + blue + "Tutorials" + w, end = _end)
      elif x == 7:
        print(white_back + blue + "Share" + w, end = _end)
      elif x == 8:
        print(white_back + blue + "Template" + w, end = _end)
      elif x == "p":
        print(white_back + "  " + w, end = _end)
      elif x == 10:
        print()
    

def find_player() -> int:
  index = -1
  for i in map:
    index += 1
    if i == 2: 
      return index

# All global variables
login_menu = True
current_option_login = 1
current_option_play = 1
login_menu = True
signup_menu = True


cursor.hide()
clear()

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
    elif login_i in [space, "", "x"]:
      login_menu = False
      clear()
    clear()

  cursor.show()
  
  if current_option_login == 2: # Skips option 1 because Guest has no saving option. This may change later on in the future.
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
          
  elif current_option_login == 1:
    print(f"{green}Logging into game as guest...{w}")
    time.sleep(2)
    clear()

  signup_menu = False
  login_menu = False
  play_menu = True
  cursor.hide()

  while play_menu:
    print("ReplitTD")
    if current_option_play == 1:
      print(f"{yellow}> Quick play{w}")
      print("Play online")
      print("Competitive")
    elif current_option_play == 2:
      print("Quick play")
      print(f"{yellow}> Play online{w}")
      print("Competitive")
    elif current_option_play == 3:
      print("Quick play")
      print("Play online")
      print(f"{yellow}> Competitive{w}")
    menu_i = getkey.getkey()
    
    if menu_i in [key_up, key_left, "w", "a"]:
      a = current_option_play - 1
      if a == 0:
         current_option_play = 3
      else:
        current_option_play -= 1
    elif menu_i in [key_down, key_right, "s", "d"]:
      a = current_option_play + 1
      if a == 4:
        current_option_play = 1
      else:
        current_option_play += 1
    elif menu_i in [space, "", "x"]:
      play_menu = False
      clear()
    clear()
  
    cursor.show()

  if current_option_play == 1:
    map_lists = ["Replit Talk", "Python Repl", "Replit Home"]
    map = random.choice(map_lists)
    num = 0

    while num <= 10:
      num+=1
      cursor.hide()
      for i in range(2):
        print("Game setup")
        print("Selecting map...")
        print_map(replit_talk_map)
        time.sleep(0.1)
        clear()
        print("Game setup")
        print("Selecting map...")
        print_map(python_repl_map)
        time.sleep(0.1)
        clear()
        print("Game setup")
        print("Selecting map...")
        print_map(replit_home_map)
        time.sleep(0.1)
        clear()

    if map == map_lists[0]:
      print_map(replit_talk_map)
      print("\nCurrent towers:\n[1]. (N) Noob\n[2]. (P) PythonCoder\n[3]. (J) JavaCoder")
      idk = random.choice([True, False])
      if idk:
        print("Note: syntax for choosing towers is choosing them by number, and separating them with spaces.")
      cursor.show()
      choose_towers = input("> ")

      choose_towers = choose_towers.split(" ")

      print(choose_towers)
      
    elif map == map_lists[1]:
      print_map(python_repl_map)
      print("\nCurrent towers:\n[1]. (N) Noob\n[2]. (P) PythonCoder\n[3]. (J) JavaCoder")
      idk = random.randint(1, 2)
      if idk == 1:
        print("Note: syntax for choosing towers is choosing them by number, and separating them with spaces.")
      cursor.show()
      choose_towers = input("> ")
      
    elif map == map_lists[2]:
      print_map(replit_home_map)
      print("\nCurrent towers:\n[1]. (N) Noob\n[2]. (P) PythonCoder\n[3]. (J) JavaCoder")
      idk = random.randint(1, 2)
      if idk == 1:
        print("Note: syntax for choosing towers is choosing them by number, and separating them with spaces.")
      cursor.show()
      choose_towers = input("> ")

  elif current_option_play == 2:
    pass

  elif current_option_play == 3:
    pass