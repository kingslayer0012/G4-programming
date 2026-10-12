"""
Melendez_Jacob
MP1_EXAM
"""

print ("============================================")
print ("welcome to Fahrenheit to Celsius converter!!")
print ("============================================")
f = int(input("\nplease enter your temperature in Fahrenheit: "))
c = (f-32)*5/9
if c <= 0:
    print (f"\nhere is your Celsius {c} - Freezing Alert!!")
elif c > 32:
    print (f"\nhere is your Celsius {c} - Heat Warning!!")
else:
    print (f"\nhere is your Celsius {c} - Normal Temperature")
print ("\nThank you for using Fahrenheit to Celsius converter!!")
print ("\nhave a blessed day!!")