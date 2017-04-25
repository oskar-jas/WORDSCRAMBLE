print("Welcome to random number generator")
print("A number between 1-6 is given, the number is equivalent to the year group")
print("The number that is given first and second are the year group that will leave their class at 12:54")
print("The next two year groups will leave at 12:57")
print("And the last year groups at 1:00")
print("The first two year group are....: ")
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
#Was trying to make a code that doesnt give 2 numbers twice but i havent made a successful one yet
