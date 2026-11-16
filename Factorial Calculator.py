"""
Filename: <Factorial_Calculator>
Author: <Melendez,Jacob>
Created: <11/12/2026>
Instructor: Burgess
"""
def factorial():
    x = int(input ("input a number: "))
    t = 1
    print(f"{x}! = ",end="")
    for i in range(x, 0, -1):
        if i > 1:
            print(f"{i} * ", end="")
        else:
            print(f"{i} ", end="")
        t *= i
    print(f"= {t}")


def main():
    print("This program computes factorials and displays their intermediate calculations.")
    running = "y"
    while running == "y":
        factorial()
        running = input("Do another calculation? (y/n)\n").lower()
    print("Thank you for using this factorial calculator!")

if __name__ == "__main__":
    main()