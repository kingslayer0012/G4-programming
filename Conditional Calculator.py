"""
Filename: conditional calculator.py
Author: <Melendez, Jacob>
Created: <09/25/2026>
Instructor: burgess
"""
from time import sleep
print ("welcome to conditional calculator")

print ("\nthis is a conditional calculator that will help you with 2 numbers on the 4 simple symbols")

n1 = int(input ("\nenter first number: "))
x = input ("\nenter your operation(+,-,*,/): ")
n2 = int(input ("\nenter second number: "))

if x == '+':
    print (f"\n {n1}+{n2}={n1+n2}")
elif x == '-':
    print (f"\n {n1}-{n2}={n1-n2}")
elif x == '*':
    print (f"\n {n1}*{n2}={n1*n2}")
elif x == '/':
    print (f"\n {n1}/{n2}={n1/n2}")

print ("\nthank you for using conditional caculator")
print ("have a blessed day")

sleep(5)