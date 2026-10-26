"""
Filename: <Average_Calculator>
Author: <Melendez,Jacob>
Created: <10/22/2026>
Instructor: Burgess
"""
a = 0
x = 0
n = 0
s = 0
print ("===============================")
print ("Welcome to Average Calculator!!")
print ("===============================")

print ("\nWelcome to Average Calculator this is an Average Calculator that does Average Calculator things")

while True:
    n = int(input("\nplease enter a number: "))
    s = s + n
    print (f"\nhere is the sum of your numbers {s}")
    if x >=0:
        x +=1
    print (f"\nhere is the current numbers you have inputted {x}")
    a = (s / x)
    print (f"\nhere is the your average value numbers inputted {a}")
    t = input ("\nwould you like to enter another number? (y/n): ")
    if t == "y":
        continue
    else:
        break

print ("\nThank you for using Average Calculator!!")
print ("\nhave a blessed day!!")