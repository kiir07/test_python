# Шоколадка имеет вид прямоугольника, разделенного на n×m долек.
# Шоколадку можно один раз разломить по прямой на две части.
# Определите, можно ли таким образом отломить от шоколадки часть,
# состоящую ровно из k долек.
# Формат ввода
# Программа получает на вход три числа: n, m, k.
# Формат вывода
# Программа должна вывести одно из двух слов: YES или NO.

a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())

if a1 <= b2 and a2 <= b1:
    print('NO')
else:
    print('YES')