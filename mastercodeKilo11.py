print("Welcome to random number generator")
print("A number between 1-6 is given, the number is equivalent to the year group")
print("The number that is given first is the year group that will leave their class at 12:48")
print("The next year group will leave at 12:51")
print("Then 12:54")
print("Followed by 12:57")
print("And finally at 1:00")
print("The first year group is....")
import random
for x in range(0, 6):
  random_number = random.randint(0, 6)
  print(random_number)
"""This is another code that gives a random number
import random

  number=random.random()
  number=6*number
  print(int(number))
"""
