# Переставьте соседние элементы списка (A[0] c A[1],A[2] c A[3] и т.д.).
# Если элементов нечетное число, то последний элемент остается на своем месте.
# Формат ввода
# Вводится список чисел. Все числа списка находятся на одной строке.
# Формат вывода
# Выведите ответ на задачу.

mas = list(map(int, input().split()))


def permutation_of_numbers():

    if len(mas) % 2 != 0:
        for i in range(0, len(mas)-1, 2):
            mas[i], mas[i+1] = mas[i+1], mas[i]
    else:
        for i in range(0, len(mas), 2):
                mas[i], mas[i+1] = mas[i+1], mas[i]

    print(*mas)

permutation_of_numbers()
