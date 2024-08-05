class Calculator:
    def __init__(self):
        self.__num1 = 0
        self.__num2 = 0

    def set_num1(self, num1):
        self.__num1 = num1

    def set_num2(self, num2):
        self.__num2 = num2

    def get_num1(self):
        return self.__num1

    def get_num2(self):
        return self.__num2

    def add(self):
        return self.__num1 + self.__num2

    def subtract(self):
        return self.__num1 - self.__num2

calc = Calculator()


calc.set_num1(10)
calc.set_num2(5)


result = calc.add()
print(f"Addition: {calc.get_num1()} + {calc.get_num2()} = {result}")

result = calc.subtract()
print(f"Subtraction: {calc.get_num1()} - {calc.get_num2()} = {result}")


calc.set_num1(20)
calc.set_num2(10)

result = calc.add()
print(f"Addition: {calc.get_num1()} + {calc.get_num2()} = {result}")

result = calc.subtract()
print(f"Subtraction: {calc.get_num1()} - {calc.get_num2()} = {result}")
