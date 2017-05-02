from time import sleep
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
print(" _____ _____ ______  ___  ___  _________ _      _____ ")
print("/  ___/  __ \| ___ \/ _ \ |  \/  || ___ \ |    |  ___|")
print("\ `--.| /  \/| |_/ / /_\ \| .  . || |_/ / |    | |__  ")
print(" `--. \ |    |    /|  _  || |\/| || ___ \ |    |  __| ")
print("/\__/ / \__/\| |\ \| | | || |  | || |_/ / |____| |___ ")
print("\____/ \____/\_| \_\_| |_/\_|  |_/\____/\_____/\____/ ")
sleep(2)
print("Make a word out of the letters given")
print("You MUST use all of the letters given")
print("If you make the correct word you will be awarded one point and will move on")
print("If you get it wrong you will still move onto the next question")
print("You MUST answer with the work in CAPITAL LETTERS")
print("First question")
answer=input("Your letters are: N,P,E")
if answer=="PEN":
  print("CORRECT!")
  score = score +1
elif answer=="NEP":
  print("WRONG!")
else:
  print("WRONG!")
print(score)
