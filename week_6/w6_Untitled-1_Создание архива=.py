# Системный администратор вспомнил, что давно не делал
# архива пользовательских файлов. Однако, объем диска
# куда он может поместить архив, может быть меньше
# ем суммарный объем архивируемых файлов.
# Известно, какой объем занимают файлы каждого пользователя.
# Напишите программу, которая по заданной информации о
# пользователях и свободному объему на архивном диске
# определит максимальное число пользователей,
# чьи данные можно поместить в архив.
# Формат ввода
# Программа получает на вход в одной строке число S –
# размер свободного места на диске (натуральное, не превышает 10000),
# и число N – количество пользователей (натуральное, не превышает 100),
# после этого идет N чисел - объем данных каждого пользователя
# (натуральное, не превышает 1000), записанных каждое в отдельной строке.
# Формат вывода
# Выведите наибольшее количество пользователей,
# чьи данные могут быть помешены в архив.

a = list(map(int, input().split()))
b = []
while a[1] > len(b):
    b.append(int(input()))


def archive_n(a, b):
    b.sort()
    sum = 0
    k = 0

    for i in range(0, len(b)):
        sum += b[i]
        if sum < a[0] and i < len(b):
            k += 1
    print(k)


archive_n(a, b)
