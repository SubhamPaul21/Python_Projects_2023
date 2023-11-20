# This file is about creating a Python calculator script
# Function for addition
def add(number1, number2):
    return number1 + number2


# Function for subtraction
def sub(number1, number2):
    return number1 - number2


# Function for multiplication
def multiply(number1, number2):
    return number1 * number2


# Function for division
def divide(number1, number2):
    return number1 / number2


# Function to get the numbers for calculation
def get_numbers():
    first_input = int(input("Insert the First Number: "))
    second_input = int(input("Insert the Second Number: "))
    return first_input, second_input


# Function to ask if user wants to do more calculation
def wanna_continue():
    print("1: Continue")
    print("2: Exit")
    continue_or_not = int(input("Select your choice: "))
    if continue_or_not == 1:
        calculate()
    elif continue_or_not == 2:
        exit()
    else:
        print("----XXXX----")
        print("Invalid Input")
        print("Let's try again")
        print("----XXXX----", end="\n\n")
        wanna_continue()


# Function for Calculation prompts
def calculate():
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    choice = int(input("Select your choice: "))

    if choice == 1:
        num1, num2 = get_numbers()
        print(num1, "+", num2, "=", add(num1, num2))
        wanna_continue()
    elif choice == 2:
        num1, num2 = get_numbers()
        print(num1, "-", num2, "=", sub(num1, num2))
        wanna_continue()
    elif choice == 3:
        num1, num2 = get_numbers()
        print(num1, "*", num2, "=", multiply(num1, num2))
        wanna_continue()
    elif choice == 4:
        num1, num2 = get_numbers()
        print(num1, "/", num2, "=", divide(num1, num2))
        wanna_continue()
    else:
        print("----XXXX----")
        print("Invalid input")
        print("Let's try again")
        print("----XXXX----", end="\n\n")
        calculate()


calculate()
