# Шахматный король ходит по горизонтали, вертикали и диагонали,
# но только на 1 клетку. Даны две различные клетки шахматной доски,
# определите, может ли король попасть с первой клетки на вторую одним ходом.
# Формат ввода
# Программа получает на вход четыре числа от 1 до 8 каждое,
# задающие номер столбца и номер строки сначала для первой клетки,
# потом для второй клетки.
# Формат вывода
# Программа должна вывести YES, если из первой клетки
# ходом короля можно попасть во вторую или NO в противном случае.

a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
no = 'NO'
yes = 'YES'

if (a2 - a1 <= 1 or a2 - a1 <= 0) and (b2 - b1 <= 1 or b2 - b1 <= 0):
    print(yes)
else:
    print(no)
