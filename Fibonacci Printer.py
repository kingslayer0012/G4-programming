"""
Filename: <Fibonacci_Printer>
Author: <Melendez,Jacob>
Created: <11/18/2026>
Instructor: Burgess
"""
x=0
y=1
t=x+y
x=y
y=t
x,y=y,x+y

def n_fibonacci():
    n = int(input ("input a non-negative whole number: "))
    for i in range (n):
        print (i)





#You should not need to change any code below this point
def main():
    print("This program displays the standard Fibonacci sequence that is n elements long.")
    running = "y"
    while running == "y":
        n_fibonacci()
        running = input("\nPrint another sequence? (y/n)").lower()
    print("Thank you for using this standard Fibonacci sequence printer!")

if __name__ == "__main__":
    main()