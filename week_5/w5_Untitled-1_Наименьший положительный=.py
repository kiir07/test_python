# Выведите значение наименьшего из всех положительных элементов в списке.
# Известно, что в списке есть хотя бы один положительный элемент,
# а значения всех элементов списка по модулю не превосходят 1000.

a = ()


def min_abs(a):
    a = list(map(int, input().split()))
    mx = []
    for i in range(0, len(a)):
        if int(a[i]) > 0:
            mx.append(a[i])

    print(min(mx))


min_abs(a)
