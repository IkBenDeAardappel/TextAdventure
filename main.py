import time

#vraag om naam, naam = de input
print("Hi, what's your name?")
name = input()
print("Hello", (name + '.'))
time.sleep(2)

#ask to start the game
def startGame():
  print("Would you like to start the game?")
  print("type: 'y' or 'n'")
  answer = input()
  if len(answer) > 1:
    print("Error! Only 1 character allowed! Try again.")
    time.sleep(1)
    startGame()  
  elif answer == "n":
    print("Hello darkness my old friend...")
    time.sleep(1)
    exit()
  elif answer == "y":
    time.sleep(1)
  else:
    print("That is not an option. Try again.")
    time.sleep(1)
    startGame()

startGame()
time.sleep(1)

item = ["flashlight"]
inventory = []

def addToInventory(item):
  inventory.append(item)
def starterFlashlight():
  print("Do you want to pick up the flashlight?") 
  print("type: 'y' or 'n'")
  answer = input()
  if answer == "y":
    addToInventory("flashlight")
    print("You picked up the flashlight.")
    time.sleep(1) 
  elif len(answer) > 1:
    print("Error! Only 1 characters allowed! Try again.")
    time.sleep(1)
    starterFlashlight()  
  elif answer == "n":
   print("Alright.")
   time.sleep(2)
  else:
    print("That is not an option. Try again.")
    time.sleep(1)
    starterFlashlight()
def headBump():
  print("Where do you want to go?")
  print("Type: 'w'(sleeping quarters), 'e' (or 'q' to quit).")
  answer = input()
  if answer == "w":
    room_sleepingquarter()
  elif answer == "e":
    print("Oh my god, you did it again?! Guess the wall was talking about you...")
    time.sleep(2)
    headBump()
  elif answer == 'q':
    print("Thanks for playing!")
    time.sleep(1)
    exit()
  else:
    print("That is not an option. Try again.")
    

#start game
print("You wake up in a dimly lit room. You need to get out of here. You appear to be in some sort of sleeping quarter.")
time.sleep(4)
print("You look around and spot a few beds all with their own night stand.")
time.sleep(4)
print("You find a flashlight on one of the night stands.")
starterFlashlight()

def room_kitchen():
  print("You are standing in the Kitchen.")
def room_kitchenstorage():
  print("You are standing in the Kitchen Storage.")
def room_northhall():
  print("As you open the door, you can see a bunch of centipedes running away towards the darkness...")
  time.sleep(3)
  print("You are standing in the North Hall.")
  time.sleep(2)
  print("Where do you want to go?")
  print("Type: 'n', 'e' or 's'(sleeping quarters)(or 'q' to quit).")
  answer = input()
  if answer == "n":
    room_kitchen()
  elif answer == "e":
    room_kitchenstorage()
  elif answer == "s":
    room_sleepingquarter
  elif answer == "q":
    print("Thanks for playing!")
    exit()
  else:
    print("That is not an option. Try again.")
    room_northhall()
def room_easthall():
  print("You are standing in the East Hall.")
  time.sleep(2)
  print("This hall seems to be a dead end.")
  time.sleep(2)
  print("You spot the words '바보' written on the wall. You take a closer look and notice it has been written with blood.")
  time.sleep(3)
  print("Where do you want to go?")
  print("Type: 'w'(sleeping quarters), 'e' (or 'q' to quit).")
  answer = input()
  if answer == "w":
    room_sleepingquarter()
  elif answer == "e":
    print("You bumped your head against the wall. Told you it was a dead end...")
    time.sleep(3)
    headBump()
  else:
    print("That is not an option. Try again.")
    room_easthall()
def room_southhall():
  print("south")
def room_westhall():
  print("west")
def room_introsleepingquarter():
  print("You are standing in the sleeping quarters.")
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
    print("That is not an option. Try again.")
    room_sleepingquarter()
def room_sleepingquarter():
  print("You are standing in the sleeping quarters.")
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
    print("That is not an option. Try again.")
    room_sleepingquarter()

room_introsleepingquarter()
