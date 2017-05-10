from time import sleep

def easy():
  score = 0
  answer=input("Your letters are: N,P,E")

  if answer=="PEN":
    print("CORRECT!")
    score = score +1

  elif answer=="NEP":
    print("WRONG!")

  else:
    print("WRONG!")

  print("")

  answer=input("Your letters are: H,G,U")

  if answer=="HUG":
    print("CORRECT!")
    score = score +1

  elif answer=="GUH":
    print("WRONG!")

  else:
    print("WRONG!")

  print("")

  answer=input("Your letters are: U,R,O,F")

  if answer=="FOUR": 
    print("CORRECT!") 
    score = score +1

  elif answer=="OURF":
    print("WRONG!")

  else:
    print("WRONG!")
  
  print("")	
  
  answer=input("Your letters are: E,D,R")
  
  if answer=="RED":
  	print("CORRECT!")
	score = score +1
  
  elif answer=="ERD":
  	print("WRONG!")
  
  else:
  	print('WRONG!')
	
  print("")

  answer=input("Your letters are: O,R,U")

  if answer=="OUR":
  	print("CORRECT!")
	score = score +1
  
  elif answer=="ROU":
  	print("WRONG!")
  
  else:
  	print('WRONG!')
	
  print("")

  answer=input("Your letters are: G,B,A")

  if answer=="BAG":
  	print("CORRECT!")
	score = score +1
    
  elif answer=="GAB":
  	print("WRONG!")
  
  else:
  	print('WRONG!')
answer=input("Your letters are: I,B,N")
if answer=="BIN":
	print("correct!")
	score = score +1
elif answer=="NIB":
	print("wrong")
else:
	print("wrong")

  print("You have " + str(score) + " point/s")
  
def medium():
  score = 0

  
  
def hard():
  score = 0  
  
  
  
print("WELCOME TO....")
sleep(2)
print(" _    _  _________________ ")
print("| |  | ||  _  | ___ |  _  |")
print("| |  | || | | | |_/ / | | |")
print("| |/\| || | | |    /| | | |")
print("\  /\  /\ \_/ / |\ \| |/ / ")
print(" \/  \/  \___/\_| \_|___/  ")
print(" ")
print(" _____ _____ ______  ___  ___  _________ _      ____  ")
print("/  ___/  __ \| ___ \/ _ \ |  \/  || ___ \ |    |  __| ")
print("\ `--.| /  \/| |_/ / /_\ \| .  . || |_/ / |    | |__  ")
print(" `--. \ |    |    /|  _  || |\/| || ___ \ |    |  __| ")
print("/\__/ / \__/\| |\ \| | | || |  | || |_/ / |____| |___ ")
print("\____/ \____/\_| \_\_| |_/\_|  |_/\____/\_____/\____/ ")
print("")
print("")
print("")
sleep(2)
print("      ___           ___           ___       ___           ___     ")
print("     /\  \         /\__\         /\__\     /\  \         /\  \    ")
print("    /::\  \       /:/  /        /:/  /    /::\  \       /::\  \   ")
print("   /:/\:\  \     /:/  /        /:/  /    /:/\:\  \     /:/\ \  \  ")
print("  /::\ \:\  \   /:/  /  ___   /:/  /    /::\ \:\  \   _\:\ \ \  \ ")
print(" /:/\:\ \:\__\ /:/__/  /\__\ /:/__/    /:/\:\ \:\__\ /\ \:\ \ \__)")
print(" \/_|::\/:/  / \:\  \ /:/  / \:\  \    \:\ \:\ \/__/ \:\ \:\ \/__/")
print("    |:|::/  /   \:\  /:/  /   \:\  \    \:\ \:\__\    \:\ \:\__\  ")
print("    |:|\/__/     \:\/:/  /     \:\  \    \:\ \/__/     \:\/:/  /  ")
print("    |:|  |        \::/  /       \:\__\    \:\__\        \::/  /   ")
print("     \|__|         \/__/         \/__/     \/__/         \/__/    ")
print("")
sleep(1)
print("Make a word out of the letters given")
sleep(2)
print("")
print("You MUST use all of the letters given")
sleep(2)
print("")
print("If you make the correct word you will be awarded one point and will move on")
sleep(2)
print("")
print("If you get it wrong you will still move onto the next question")
sleep(2)
print("")
print("You MUST answer using CAPITAL LETTERS")
sleep(2)
print("")
print("Choose your difficulty")
sleep(2)
print("")

diff=input("Easy, Medium, Hard ")

if diff=="EASY":
  print("You chose EASY")
  easy()

elif diff=="MEDIUM":
  print("You chose MEDIUM")
  medium()
  
elif diff=="HARD":
  print("You chose HARD")
  hard()
  
