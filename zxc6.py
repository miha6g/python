from mymodule import Calculator

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
