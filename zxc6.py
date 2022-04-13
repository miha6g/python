import math
import random


class Calculator:
    @staticmethod
    def basemath(operation):
        x = float(input("x = "))
        y = float(input("y = "))
        if operation == "+":
            print(x + y)
        if operation == "-":
            print(x - y)
        if operation == "*":
            print(x * y)
        if operation == "/":
            if y == 0:
                print("Делить на 0 нельзя")
                return
            print(x / y)

    @staticmethod
    def mathpro(operation):
        x = float(input("x = "))
        if operation == "exponentiation":
            print(math.exp(x))
        if operation == "module":
            print(math.fabs(x))
        if operation == "factorial":
            print(math.factorial(x))
        if operation == "arccos":
            print(math.acos(x))

    @staticmethod
    def rand():
        print(random.randint(0, 100))


while True:

    a = input(
        "Какую операцию вы хотите выполнить: +, - , / , * , exponentiation, module, random , factorial , arccos , exit : ")
    if a in ('+', '-', '*', '/'):
        Calculator.basemath(a)
    if a in ("exponentiation", "module", "factorial", "arccos"):
        Calculator.mathpro(a)
    if a == "random":
        Calculator.rand()
    if a == "exit":
        break

