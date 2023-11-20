# Program to create a continuous command based python calculator
import re

run = True  # Variable to be used in while loop for continuous running of calculator
previous_value = 0  # Variable for keeping track of previous value which initiates with 0 like a normal calculator
equation = ""  # Variable for taking equation input from the user in the command


print("Welcome to the smartest Python Calculator...")
print("Type 'exit' at any moment to stop!")


def run_calculator():
    global equation
    global run
    global previous_value

    if equation == "":
        equation = input("Enter your equation: ")
    else:
        equation = input("Continue your equation: " + str(previous_value))
    if equation.__contains__("exit"):
        print("Goodbye, human!")
        run = False
    else:
        equation = re.sub('[^0-9+-\\\\*/%]', '', equation)
        if previous_value != 0:
            equation = str(previous_value) + equation
        # print(equation)
        previous_value = eval(equation)
        print(previous_value)
        # print("The output is", previous_value)


while run:
    run_calculator()
