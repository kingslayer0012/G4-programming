x = input("do you prefer working from home or the office?: ")

if x == "home":
    input("tell me why you would prefer home: ")
else:
    input("tell me why you would prefer office: ")

print ("ok next question")
r = input ("why did you choose to apply to our company?: ")
print ("ok next question")

y = input ("do you feel comfortable talking to your coworkers?: ")

if y == "yes":
    print ("ok")
else:
    input ("tell me why?: ")

print ("ok next question")
t = input ("what distracts you the most?: ")
print ("ok final question")

z = input ("do you feel comfortable asking people for help?: ")

if z == "yes":
    print ("ok")
else:
    input ("tell me why?: ")

print ("thanks for taking my interview")

print("You entered: ",x)
print("You entered: ",r)
print("You entered: ",y)
print("You entered: ",t)
print("You entered: ",z)