# Определите количество четных элементов
# в последовательности, завершающейся числом 0.
# Формат ввода
# Вводится последовательность целых чисел,
# оканчивающаяся числом 0 (само число 0 в
# последовательность не входит, а служит как признак ее окончания).
# Формат вывода
# Выведите ответ на задчу.

n = 1
i = 0

while n != 0:
    n = int(input())
    if n == 0:
        continue
    elif n % 2 == 0:
        i += 1
    else:
        continue
print(i)
