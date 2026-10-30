"""
Filename: <Number_Guessing_Game>
Author: <Melendez,Jacob>
Created: <10/30/2026>
Instructor: Burgess
"""
c = 0
print ("=================================")
print ("Welcome to Number Guessing Game!!")
print ("=================================")

import random
x = random.randint(1,100)
#print (x)

while True:
    g = int(input("\nGuess a number: "))
    if c >=0:
        c +=1
    if g > x:
        print ("to high")
    elif g < x:
        print ("to low")
    elif g == x:
        print ("\nyou win")
        break

print (f"\nthis is how many attempts it took you to guess the number {c}")
print ("\nThank you for playing Number Guessing Game!!")
print ("\nhave a blessed day!!")