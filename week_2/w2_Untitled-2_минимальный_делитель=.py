# Дано целое число, не меньшее 2.
# Выведите его наименьший натуральный делитель, отличный от 1.
# Формат ввода
# Вводится целое положительное число.
# Формат вывода
# Выведите ответ на задачу.

n = int(input())
i = 1
k = 2
while i != 0:
    if n % k == 0:
        print(k)
        i = n % k
    else:
        k += 1
