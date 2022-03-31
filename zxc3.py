a = input("Введите первый овощ: ")
b = input("Введите второй овощ: ")
c = input("Введите третий овощ: ")
print(a.lower(),b.lower(),c.lower())
print(a.upper(),b.upper(),c.upper())
print(a.capitalize(),b.capitalize(),c.capitalize())
countA=int(input(str(a.capitalize())+" кол-во(шт.): "))
countB=int(input(str(b.capitalize())+" кол-во(шт.): "))
countC=int(input(str(c.capitalize())+" кол-во(шт.): "))
print('Информация об овоще: {овощ}:{количество}шт'.format(овощ=a.capitalize(), количество=countA))
print('Информация об овоще: {овощ}:{количество}шт'.format(овощ=b.capitalize(), количество=countB))
print('Информация об овоще: {овощ}:{количество}шт'.format(овощ=c.capitalize(), количество=countC))


