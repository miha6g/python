def create_set(title):
    a = input(title).split(",")
    print(a)
    return a


first_set = create_set("Введите через запятую список слов: ")
c = len(first_set)
second_set = create_set(
    "Первый список состоит из " + str(c) + " слов, введите еще один список с таким же количеством слов")
dictionary = {}

for i in range(0, len(first_set)):
    dictionary[first_set[i]] = second_set[i]
print(dictionary)
