def create_set(title):
    a=input(title).split(",")
    b=set(a)
    print(b)
    return b
first_set=create_set("Введите через запятую список слов: ")
c=len(first_set)
second_set=create_set("Первый список состоит из " +str(c) + " слов, введите еще один список с таким же количеством слов ")
z = dict(zip(first_set, second_set))
print(z)