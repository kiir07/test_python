# Для данного числа n<100 закончите фразу “На лугу пасется...”
# одним из возможных продолжений: “n коров”, “n корова”, “n коровы”,
# правильно склоняя слово “корова”.
# Формат ввода
# Вводится натуральное число.
# Формат вывода
# Программа должна вывести введенное число n и одно из слов: korov,
# korova или korovy. Между числом и словом должен стоять ровно один пробел.
# Примечание

numCow = int(input())

if numCow == 1:
    print(numCow, 'korova')
elif 1 < numCow < 5:
    print(numCow, 'korovy')
elif 4 < numCow < 21 or numCow == 0:
    print(numCow, 'korov')
else:
    if numCow % 10 == 1:
        print(numCow, 'korova')
    elif 1 < numCow % 10 < 5:
        print(numCow, 'korovy')
    elif 4 < numCow % 10 < 21 or numCow % 10 == 0:
        print(numCow, 'korov')
