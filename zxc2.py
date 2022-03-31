
import math
import random
while True:
    a=input("Какую операцию вы хотите выполнить: +, - , / , * , exponentiation, module, random , factorial , arccos , exit : ")
    if a in ('+', '-', '*', '/'):
        x = float(input("x = "))
        y = float(input("y = "))
        if a =="+":
            print(x+y)
        if a =="-":
            print(x-y)
        if a =="*":
            print(x*y)
        if a =="/":
            if y == 0:
                print("Делить на 0 нельзя")
                continue
            print(x/y)
    if a in ("exponentiation", "module", "factorial", "arccos"):
        x = float(input("x = "))
        if a == "exponentiation":
            print(math.exp(x))
        if a == "module":
            print(math.fabs(x))
        if a == "factorial":
            print(math.factorial(x))
        if a == "arccos":
            print(math.acos(x))
    if a == "random":
        print(random.randint(0, 100))
    if a == "exit":
        break

