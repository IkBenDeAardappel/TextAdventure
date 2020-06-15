import time


#vraag om naam, naam = de input
print("Hi, what's your name?")
name = input()
print("Hello", (name + '.'))
possible_answers = ('y', 'n')
while input() in possible_answers:
  print('hello')
else:
  print("not an option")



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
  start_game = "You wake up in a dimly lit room. You appear to be in some sort of sleeping quarter."
  time.sleep(1)
  print(start_game)
else:
  print("That is not an option. You lost.")
  time.sleep(1)
  exit()

time.sleep(3)

#start game
class game_1:
  print("You look around and spot a few beds all with their own night stand. You also notice 4 doors.")
time.sleep(1)
print("You find a flashlight on one of the night stands. Do you want to pick up the flashlight?")
print("type: 'y' or 'n'")
answer = input()
if len(answer) > 1:
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
  print("You picked up the flashlight this time")
  time.sleep(1)
elif answer == "y":
 print("to bad")
 exit()
elif answer == "y":
  response = "You picked up a flashlight."
  time.sleep(1)
  print(response)
