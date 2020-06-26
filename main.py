import time

def code():
  print("type code:")
  code = input()
  if code == "8804":
    print("Correct!")
    time.sleep(2)
    room_forest()
  elif len(code) < 4:
    print("The code has to be 4 digits. Try again.")
    time.sleep(2)
    room_ladder()
  elif len(code) > 4:
    print("The code has to be 4 digits. Try again.")
    time.sleep(2)
    room_ladder()  
  else:
    print("That is not an option. Try again.") 
    time.sleep(2)
    room_ladder()

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
        print("Are you sure?")
        print("type: 'y' or 'n'")
        answer = input()
        if answer == "y":
          print("Alright.")
          time.sleep(2)
        elif len(answer) > 1:
          print("Error! Only 1 characters allowed! Try again.")
          time.sleep(2)
          starterFlashlight()
        elif answer == "n":
          print("you picked up a flashlight")
          addToInventory("flashlight")
          time.sleep(2)
        elif answer == "q":
          print("Thanks for playing!")
          time.sleep(2)
          exit()
        else:
          print("That is not an option. Try again.")
          time.sleep(2)
          starterFlashlight()
          time.sleep(2)

def headBump():
    print("Where do you want to go?")
    print("Type: 'w'(sleeping quarters), 'e' (or 'q' to quit).")
    answer = input()
    if answer == "w":
        room_sleepingquarter()
    elif answer == "e":
        print(
            "Oh my god, you did it again?! Guess the wall was talking about you..."
        )
        time.sleep(4)
        headBump()
    elif answer == 'q':
        print("Thanks for playing!")
        time.sleep(1)
        exit()
    else:
        print("That is not an option. Try again.")

def room_control():
  print("You are standing in what seems to be some sort of control room.")
  time.sleep(4)
  print("There are a lot of monitors displaying all the rooms you have been in.")
  time.sleep(4)
  print("One particular monitor is just displaying 4 digits: '8804'.")
  time.sleep(4)
  print("You also see a lot of buttons. This room is way cleaner than all of the other rooms you have been in so far.")
  time.sleep(4)
  print("What do you want to do?")
  print("Type 'n'.")
  answer = input()
  if answer == 'n':
    room_westhall()
  elif answer == 'q':
    print("Thanks for playing!")
    exit()
  elif answer == 'i':
    print(inventory)
    time.sleep(3)
    room_control()
  else:
    print("That is not an option. Try again.")
    time.sleep(2)
    room_control()

def starterKnife():
  print("You spot a knife on one of the kitchen counters.")
  time.sleep(3)
  print("Do you want to pick up the knife?")
  print("type 'y' or 'n'")
  answer = input()
  if answer == "y":
    addToInventory("knife")
    print("You picked up the knife.")
    time.sleep(2)
  elif len(answer) > 1:
    print("Error! Only 1 characters allowed! Try again.")
    time.sleep(2)
    starterKnife()
  elif answer == "n":
    print("Alright.")
    time.sleep(2)
  else:
    print("That is not an option. Try again.")
    time.sleep(2)
    starterKnife()
    time.sleep(2)

def room_kitchen():
  print("You are standing in the Kitchen. It smells like rotten meat.")
  time.sleep(4)
  if "knife" not in inventory:
    starterKnife()
  print("Where do you want to go?")
  print("Type: 's'")
  answer = input()
  if answer == "s":
    room_northhall()
  elif answer == "q":
    print("Thanks for playing!")
    time.sleep(1)
    exit()
  elif answer == "i":
    print(inventory)
    time.sleep(3)
    room_kitchen()
  else:
    print("That is not an option. Try again.")
    room_kitchen()

def room_kitchenstorage():
  print("You are standing in the Kitchen Storage.")
  time.sleep(3)
  if "key" not in inventory:
    print("You look on all the shelves and spot a dusty key with the label 'control room'.")
    time.sleep(4)
    print("Do you want to pick up the key?")
    print("Type 'y' or 'n'.")
    answer = input()
    if answer == "y":
      addToInventory("key")
      print("You picked up the key.")
      time.sleep(2)
    elif answer == "n":
      print("You did not pick up the key.")
      time.sleep(2)
    elif answer == "q":
      print("Thanks for playing!")
      exit()
    else:
      print("That is not an option. Try again.")
      time.sleep(2)
      room_kitchenstorage()
  else:
    print("There is nothing you can pick up in this room.")
  print("What do you want to do?")
  print("Type 'w'.")
  answer = input()
  if answer == "w":
    room_northhall()
  elif answer == "q":
    print("Thanks for playing!")
    exit()
  elif answer == "i":
    print(inventory)
    time.sleep(2)
    room_kitchenstorage()
  else:
    print("That is not an option. Try again.")
    time.sleep(1)
    room_kitchenstorage()

def room_ladder():
  print("You enter a  small room. The only thing in this room is a ladder going up.")
  time.sleep(3)
  print("You climb the ladder. This seems to be the way out!")
  time.sleep(3)
  print("You approach a hatch. You try to push it, but it won't open.")
  time.sleep(3)
  print("You need to enter a 4 digit code.")
  time.sleep(3)
  print("What do you want to do?")
  print("Type 'code'(to type the code for the hatch) or 'n'.")
  answer = input()
  if answer == 'n':
    room_southhall()
  elif answer == "code":
    code()
  elif answer == "q":
    print("Thanks for playing!")
    time.sleep(1)
    exit()
  elif answer == "i":
    print(inventory)
    time.sleep(3)
    room_ladder()
  else:
    print("That is not an option. Try again.")
    time.sleep(3)
    room_ladder()

def room_forest():
  print("You open the hatch. It is night time.")
  time.sleep(3)
  print("You climb the ladder and stand up. Where am I?")
  time.sleep(3)
  print("You look around. All you see is trees.")
  time.sleep(3)
  print("You get startled by a distant howl of what you assume must be a wolf.")
  time.sleep(4)
  print("Congratz, you won! You escaped the bunker!...")
  time.sleep(4)
  print("But did you really?....")
  time.sleep(2)
  exit()

def room_northhall():
    print("As you open the door, you can see a bunch of centipedes run away towards the darkness...")
    time.sleep(4)
    print("You are standing in the North Hall.")
    time.sleep(3)
    print("Where do you want to go?")
    print("Type: 'n', 'e' or 's'(sleeping quarters).")
    answer = input()
    if answer == "n":
        room_kitchen()
    elif answer == "e":
        room_kitchenstorage()
    elif answer == "s":
        room_sleepingquarter()
    elif answer == "q":
        print("Thanks for playing!")
        exit()
    elif answer == "i":
      print(inventory)
      time.sleep(3)
      room_northhall()
    else:
        print("That is not an option. Try again.")
        room_northhall()

def room_easthall():
  print("You are standing in the East Hall.")
  time.sleep(2)
  print("This hall seems to be a dead end.")
  time.sleep(3)
  print("You spot the words:", name + " '바보' written on the wall. You take a closer look and notice it has been written with blood.")
  time.sleep(5)
  print("Where do you want to go?")
  print("Type: 'w'(sleeping quarters), 'e'")
  answer = input()
  if answer == "w":
    room_sleepingquarter()
  elif answer == "e":
    print("You bumped your head against the wall. Told you it was a dead end...")
    time.sleep(3)
    headBump()
  elif answer == "q":
    print("Thanks for playing!")
    exit()
  elif answer == "i":
    print(inventory)
    time.sleep(2)
    room_easthall()
  else:
    print("That is not an option. Try again.")
    room_easthall()

def askKnife():
  if "knife" in inventory:
    room_southhall()
  else:
    print("You hear a loud growl behind the door. It would not be wise to go in without any form of self defense.")
    time.sleep(5)
    print("Are you sure you want to go in?")
    print("Type 'y' or 'n'.")
    answer = input()
    if answer == "y":
      print("You enter the North Hall. A monster immediately approaches you and eats you whole.")
      time.sleep(4)
      print("GAME OVER")
      exit()
    elif answer == "n":
      room_sleepingquarter()

def killMonster():
  print("You are standing in the South Hall.")
  time.sleep(3)
  print("You see a monster at the end of the hallway. You're lucky you picked up that knife. You run towards it and stab the monster. It makes a weird growling noise before it falls on the ground with a loud thud.")
  time.sleep(8)
  addToInventory("MonsterMeat")
  print("You now have Monster Meat in your inventory.")
  time.sleep(3)
  room_southhall()

def room_southhall():
  if "MonsterMeat" in inventory:
    print("You are standing in the South Hall. You see the lifeless body of the monster on the ground. It smells.")
    time.sleep(5)
    print("Where do you want to go?")
    print("Type: 'n'(sleeping quarters), 's'.")
    answer = input()
    if answer == "n":
      room_sleepingquarter()
    elif answer == "s":
      room_ladder()
      time.sleep(2)
    elif answer == "q":
      print("Thanks for playing!")
      exit()
    elif answer == "i":
      print(inventory)
      time.sleep(2)
      room_southhall()
    else:
      print("That is not an option. Try again.")
      room_southhall()
  else:
    killMonster()

def room_westhall():
    print("You are standing in the West Hall.")
    time.sleep(3)
    print("This hall splits of in to two rooms.")
    time.sleep(3)
    print("Where do you want to go?")
    print("Type: 'e'(sleeping quarters), 's' , 'n'.")
    answer = input()
    if answer == "e":
      room_sleepingquarter()
    elif answer == "s":
      if "key" in inventory:
        room_control()
      else:
        print("You try to open the door but it won't budge. It seems to be locked.")
        time.sleep(4)
        room_westhall()
    elif answer == "n":
      room_storage()
    elif answer == "q":
      print("Thanks for playing!")
      exit()
    elif answer == "i":
      print(inventory)
      time.sleep(2)
      room_westhall()
    else:
      print("That is not an option. Try again.")
      room_westhall()

def room_introsleepingquarter():
    print("You are standing in the sleeping quarters.")
    time.sleep(3)
    print("You see 4 doors leading: north, east, south and west. Where do you want to go?")
    print("Type: 'n', 'e', 's', 'w'.")
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
            time.sleep(4)
            room_sleepingquarter()
    elif answer == 'e':
        if "flashlight" in inventory:
            room_easthall()
        else:
            print("The hallway looks way to dark, you can't go in without a form of light.")
            time.sleep(4)
            room_sleepingquarter()
    elif answer == 's':
        if "flashlight" in inventory:
            askKnife()
        else:
            print("The hallway looks way to dark, you can't go in without a form of light.")
            time.sleep(4)
            room_sleepingquarter()
    elif answer == 'w':
        if "flashlight" in inventory:
            room_westhall()
        else:
            print("The hallway looks way to dark, you can't go in without a form of light.")
            time.sleep(4)
            room_sleepingquarter()
    elif answer == "q":
      print("Thanks for playing!")
      time.sleep(1)
      exit()
    elif answer == "i":
      print(inventory)
      time.sleep(3)
      room_sleepingquarter()
    else:
        print("That is not an option. Try again.")
        room_sleepingquarter()

def room_sleepingquarter():
  print("You are standing in the sleeping quarters.")
  if "flashlight" in inventory:
    time.sleep(2)
  else:
    time.sleep(2)
    print("Do you wish to pick up the flashlight anyways?")
    print("type: 'y' or 'n'.")
    answer = input()
    if answer == "y":
      addToInventory("flashlight")
      print("You picked up the flashlight.")
      time.sleep(2)
    elif answer == "n":
      print("Alright.")
      time.sleep(2)
    else:
      print("That is not an option. Try again.")
      time.sleep(2)
      room_sleepingquarter()

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
      time.sleep(4)
      room_sleepingquarter()
  elif answer == 'e':
    if "flashlight" in inventory:
      room_easthall()
    else:
      print("The hallway looks way to dark, you can't go in without a form of light.")
      time.sleep(4)
      room_sleepingquarter()
  elif answer == 's':
    if "flashlight" in inventory:
      askKnife()
    else:
      print("The hallway looks way to dark, you can't go in without a form of light.")
      time.sleep(4)
      room_sleepingquarter()
  elif answer == 'w':
    if "flashlight" in inventory:
      room_westhall()
    else:
      print("The hallway looks way to dark, you can't go in without a form of light.")
      time.sleep(4)
      room_sleepingquarter()      
  elif answer == "q":
      print("Thanks for playing!")
      time.sleep(1)
      exit()
  elif answer == "i":
      print(inventory)
      time.sleep(3)
      room_sleepingquarter()
  else:
      print("That is not an option. Try again.")
      room_sleepingquarter()

def room_storage():
  print("You enter a storage room. You cough as you inhale a wave of rotten meat.")
  time.sleep(5)
  print("You look around the room only to see a very bloody body on a chair in the corner.")
  time.sleep(5)
  print("You immediately leave the room and close the door.")
  time.sleep(4)
  room_westhall()

item = ["flashlight", "knife", "key", "MonsterMeat"]
inventory = []


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
        print("Before you start, here are a few commands:")
        print("'q' to quit.")
        print("'i' to show inventory.")
        print("'n', 'e', 's' and 'w' to go places.")
        time.sleep(5)
        print("Have Fun!")
        time.sleep(2)
    else:
        print("That is not an option. Try again.")
        time.sleep(1)
        startGame()

startGame()
time.sleep(1)

#start game
print("You wake up in a dimly lit room. You need to get out of here. You appear to be in some sort of sleeping quarter.")
time.sleep(4)
print("You look around and spot a few beds all with their own night stand.")
time.sleep(4)
print("You find a flashlight on one of the night stands.")
starterFlashlight()

room_introsleepingquarter()
