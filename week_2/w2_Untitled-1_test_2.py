# Даны два целых числа. Программа должна вывести число "1",
# если первое число больше второго, число "2",
# если второе больше первого или число "0", если они равны.
# Формат ввода
# Вводятся два целых числа.
# Формат вывода
# Выведите ответ на задачу.

a = int(input())
b = int(input())
n1 = 1
n2 = 2
n3 = 0
if a > b:
    print(n1)
elif a < b:
    print(n2)
else:
    print(n3)