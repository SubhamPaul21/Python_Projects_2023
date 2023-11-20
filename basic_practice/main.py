def default_parameters(name="Subham", age=26):
    print("My name is", name, "and my age is", age)


def named_parameter(name="Sanket", age=55):
    print("My original name is", name, "and my original age is", age)


def undefined_parameters(*people):
    for personName in people:
        print("The name is", personName)


def sum1(num1, num2):
    return num1 + num2


class Enemy:
    def __init__(self, atk_low, atk_high):
        self.atk_low = atk_low
        self.atk_high = atk_high

    def get_atk_low(self):
        print("Lower Attack: ", self.atk_low)

    def get_atk_high(self):
        print("Higher Attack", self.atk_high)


enemy1 = Enemy(45, 60)
enemy2 = Enemy(60, 80)
enemy1.get_atk_low()
enemy2.get_atk_high()

# math1 = sum1(4, 10)
# print(math1)
# default_parameters(age=105)
# named_parameter(age=70, name="Sanket")
# undefined_parameters("Subham", "Sanket", "Suman", "Paja")
