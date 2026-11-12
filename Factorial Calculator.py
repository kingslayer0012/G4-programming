"""
Filename: <Factorial_Calculator>
Author: <Melendez,Jacob>
Created: <11/12/2026>
Instructor: Burgess
"""

def factorial():
    x = int(input ("input a number: "))
    t = 1
    for i in range(x,0,-1):
         t *= i
    print (f"{t}")




# You should not need to change any code below this point
def main():
    print("This program computes factorials and displays their intermediate calculations.")
    running = "y"
    while running == "y":
        factorial()
        running = input("Do another calculation? (y/n)\n").lower()
    print("Thank you for using this factorial calculator!")

if __name__ == "__main__":
    main()
