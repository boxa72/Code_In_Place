"""
Prompts the user to enter numbers and prints
the running total until the user enters 0.
"""

def main():
    
    prompt()

def prompt():
    total = 0
    while number != 0:
        number = int(input("Enter a value"))
        total += number
        print("Running total is " + str(total))
if __name__ == '__main__':
    main()