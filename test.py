s = 0


q1 = input ("\nFirst question, What is the default data type for numbers in Python?: ")
if q1 == "int":
    print ("\nCorrect! You have been awarded 2 points!")
    if s >=0:
        s +=2
else:
    print ("\nIncorrect! You have been penalized 1 point!")
    if s >0:
        s -=1
print (f"your score is {s}/10")
