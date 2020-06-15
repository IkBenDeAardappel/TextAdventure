import time



#vraag om naam, naam = de input
print("Hi, what's your name?")
name = input()
print("Hello", (name + '.'))
time.sleep(2)

#ask to start the game
print("Would you like to start the game?")
print("type: 'y' or 'n'")
answer = input()
if len(answer) > 1:
  print("Error! Only 1 characters allowed! You lost.")
  time.sleep(1)
  exit()  
elif answer == "n":
  print("Hello darkness my old friend...")
  time.sleep(1)
  exit()
elif answer == "y":
  time.sleep(1)
else:
  print("That is not an option. You lost.")
  time.sleep(1)
  exit()

time.sleep(1)

item = ["flashlight"]
inventory = []

def addToInventory(item):
  inventory.append(item)


#start game
print("You wake up in a dimly lit room. You appear to be in some sort of sleeping quarter.")
time.sleep(4)
print("You look around and spot a few beds all with their own night stand. You also notice 4 doors.")
time.sleep(4)
print("You find a flashlight on one of the night stands. Do you want to pick up the flashlight?")
print("type: 'y' or 'n'")
answer = input()
if answer == "y":
  addToInventory("flashlight")
  print("You picked up the flashlight.") 
elif len(answer) > 1:
  print("Error! Only 1 characters allowed!")
  time.sleep(1)
  exit()  
elif answer == "n":
  print("Are you sure?")
  print("type: 'y' or 'n'")
  answer = input()
  if len(answer) > 1:
    print("Error! Only 1 characters allowed!")
    time.sleep(1)
    exit()
  elif answer == "n":
    addToInventory("flashlight")
    print("You picked up the flashlight this time.")
    time.sleep(1)
  elif answer == "y":
    print("Too bad.")
    time.sleep(1)


def room_northhall():
  print("north")
def room_easthall():
  print("east")
def room_southhall():
  print("south")
def room_westhall():
  print("west")

def room_sleepingquarter():
  print("You are in standing in the sleeping quarters.")
  if "flashlight" in inventory:
    time.sleep(2)
  else:
   print("Do you wish to pick up the flashlight anyways?")
   print("type: 'y' or 'n'.")
   answer = input()
   if answer == "y":
    addToInventory("flashlight")
    print("You picked up the flashlight.")
    time.sleep(2)
   else:
    time.sleep(2)

  print("You see 4 doors leading: north, east, south and west. Where do you want to go?")
  print("type: 'n', 'e', 's', 'w' (or 'q' to quit)")
  answer = input()
  if answer == "q":
    print("Thanks for playing!")
    time.sleep(1)
    exit()
  elif answer == 'n':
    if "flashlight" in inventory:
      room_northhall()
    else:
      print("The hallway looks way to dark, you can't go in without a form of light.")
      time.sleep(2)
      room_sleepingquarter()
  elif answer == 'e':
    if "flashlight" in inventory:
      room_easthall()
    else:
      print("The hallway looks way to dark, you can't go in without a form of light.")
      time.sleep(2)
      room_sleepingquarter()
  elif answer == 's':
    if "flashlight" in inventory:
      room_southhall()
    else:
      print("The hallway looks way to dark, you can't go in without a form of light.")
      time.sleep(2)
      room_sleepingquarter()
  elif answer == 'w':
    if "flashlight" in inventory:
      room_westhall()
    else:
      print("The hallway looks way to dark, you can't go in without a form of light.")
      time.sleep(2)
      room_sleepingquarter()
  else:
    print("That is not an option.")
    room_sleepingquarter()

room_sleepingquarter()
