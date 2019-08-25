# В первой строке задается одно натуральное число N,
# не превосходящее 1000 – размер массива. Во второй
# строке содержатся N чисел – элементы массива (целые
# числа, не превосходящие по модулю 1000). В третьей
# строке вводится одно целое число x, не превосходящее по модулю 1000.
# Формат вывода
# Вывести значение элемента массива, ближайшее к x.
# Если таких чисел несколько, выведите любое из них.
import math
n = int(input())
n_mas = list(map(int, input().split()))
x = int(input())


def close_num():
    n_mas.sort()
    a = 0
    b = 0
    if x < n_mas[0]:
        print(n_mas[0])
    elif x > n_mas[len(n_mas)-1]:
        print(n_mas[len(n_mas)-1])
    elif x in n_mas:
        print(x)
    else:
        for i, j in enumerate(n_mas):
            if x > j:
                continue
            else:
                a = n_mas[i-1]
                b = n_mas[i]
                if math.fabs(b - x) > math.fabs(a - x):
                    print(a)
                else:
                    print(b)
            break


close_num()
