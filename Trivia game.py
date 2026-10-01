"""
Filename: Trivia_Game.py
Author: <Melendez, Jacob>
Created: <09/29/2026>
Instructor: burgess
"""

print ("======================")
print ("    Trivia Game!!!")
print ("======================")

print ("Hello, Welcome to my trivia game!")
print ("\nMy trivia game has 10 questions that you have to answer!")
print ("\nYou will get points from answering questions correctly if not you will lose points!")
print ("\nLets start!!")

input ("\nPress enter to start!")

q1 = input ("\nFirst question, What is the default data type for numbers in Python?: ")
if q1 == "int":
    print ("\nCorrect! You have been awarded 2 points!")
else:
    print ("\nIncorrect! You have been penalized 1 point!")

q2 = input ("\nSecond question, What symbol is used to perform the modulo operation in Python?: ")
if q2 == "%":
    print ("\nCorrect! You have been awarded 2 points!")
else:
    print ("\nIncorrect! You have been penalized 1 point!")

q3 = input ("\nThird question, Strings are actually arrays of what data type?: ")
if q3 == "char":
    print ("\nCorrect! You have been awarded 2 points!")
else:
    print ("\nIncorrect! You have been penalized 1 point!")

q4 = input ("\nFourth question, What function is used to get responses from the user in the console?: ")
if q4 == "input":
    print ("\nCorrect! You have been awarded 2 points!")
else:
    print ("\nIncorrect! You have been penalized 1 point!")

q5 = input ("\nFifth question, What keyword is used to define a function in Python?: ")
if q5 == "def":
    print ("\nCorrect! You have been awarded 2 points!")
else:
    print ("\nIncorrect! You have been penalized 1 point!")

q6 = input ("Sixth question, What is the term for combining multiple lists into one?: ")
if q6 == "concatenation":
    print ("\nCorrect! You have been awarded 2 points!")
else:
    print ("\nIncorrect! You have been penalized 1 point!")

q7 = input ("Seventh question, WWhat keyword is used to combine an else and if statement for multiple conditional branches: ")
if q7 == "elif":
    print ("\nCorrect! You have been awarded 2 points!")
else:
    print ("\nIncorrect! You have been penalized 1 point!")

q8 = input ("Eight question, What method is used to add an item to the end of a list?: ")
if q8 == "append":
    print ("\nCorrect! You have been awarded 2 points!")
else:
    print ("\nIncorrect! You have been penalized 1 point!")

q9 = input ("Ninth question, What symbol is used for exponents in Python?: ")
if q9 == "**":
    print ("\nCorrect! You have been awarded 2 points!")
else:
    print ("\nIncorrect! You have been penalized 1 point!")

q10 = input ("Final question, What function would you use to find how many items are in a list?: ")
if q10 == "len()":
    print ("\nCorrect! You have been awarded 2 points!")
else:
    print ("\nIncorrect! You have been penalized 1 point!")

print ("\nThank you for playing my Trivia Game!")
print ("\nYou answered 9/10 questions correctly")
print ("\nYou received a score of 17/20!")