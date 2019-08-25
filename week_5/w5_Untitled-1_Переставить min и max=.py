# В списке все элементы попарно различны.
# Поменяйте местами минимальный и максимальный элемент этого списка.
# Формат ввода
# Вводится спиок целых чисел. Все числа списка находятся на одной строке.
# Формат вывода
# Выведите ответ на задачу.

mas = list(map(int, input().split()))


def transposition_min_and_max():

    a = min(mas)
    b = max(mas)
    a1 = mas.index(a)
    b1 = mas.index(b)
    mas[a1], mas[b1] = mas[b1], mas[a1]
    # mas1.insert(a1, b)
    # mas2.insert(b1, a)
    print(*mas)


transposition_min_and_max()
