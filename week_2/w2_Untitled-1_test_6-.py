# В доме несколько подъездов. В каждом подъезде одинаковое
# количество квартир. Квартиры нумеруются подряд,
# начиная с единицы. Может ли в некотором подъезде
# первая квартира иметь номер x, а последняя – номер y?
# Формат ввода
# Вводятся два натуральных числа x и y (x ≤ y).
# Формат вывода

a = int(input())
b = int(input())
y = 'YES'
n = 'NO'
sr = b % (b - (a - 1))
sr2 = b // (a - 1)
if sr == 0 and a >= sr2:
    print(y)
else:
    print(n)