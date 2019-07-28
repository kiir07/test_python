# Есть две коробки, первая размером A₁×B₁×C₁,
# вторая размером A₂×B₂×C₂. Определите, можно
# ли разместить одну из этих коробок внутри другой,
# при условии, что поворачивать коробки можно только
# на 90 градусов вокруг ребер.
# Формат ввода
# Программа получает на вход числа A₁,B₁,C₁,A₂,B₂,C₂.
# Формат вывода
# Программа должна вывести одну из следующих строчек:
# Boxes are equal, если коробки одинаковые,
# The first box is smaller than the second one,
# если первая коробка может быть положена во вторую,
# The first box is larger than the second one,
# если вторая коробка может быть положена в первую,
# Boxes are incomparable, во всех остальных случаях.

a1, b1, c1 = int(input()), int(input()), int(input())
a2, b2, c2 = int(input()), int(input()), int(input())

if a1 < 1 or b1 < 1 or c1 < 1 or a2 < 1 or b2 < 1 or c2 < 1:
    print('Boxes are incomparable')
if a1 >= b1 and a1 >= c1:
    if b1 >= c1:
        e1 = a1
        e2 = b1
        e3 = c1
    else:
        e1 = a1
        e2 = c1
        e3 = b1
if b1 >= a1 and b1 >= c1:
    if a1 >= c1:
        e1 = b1
        e2 = a1
        e3 = c1
    else:
        e1 = b1
        e2 = c1
        e3 = a1
if c1 >= a1 and c1 >= b1:
    if a1 >= b1:
        e1 = c1
        e2 = a1
        e3 = b1
    else:
        e1 = c1
        e2 = b1
        e3 = a1
if a2 >= b2 and a2 >= c2:
    if b2 >= c2:
        k1 = a2
        k2 = b2
        k3 = c2
    else:
        k1 = a2
        k2 = c2
        k3 = b2
if b2 >= a2 and b2 >= c2:
    if a2 >= c2:
        k1 = b2
        k2 = a2
        k3 = c2
    else:
        k1 = b2
        k2 = c2
        k3 = a2
if c2 >= a2 and c2 >= b2:
    if a2 >= b2:
        k1 = c2
        k2 = a2
        k3 = b2
    else:
        k1 = c2
        k2 = b2
        k3 = a2
if e1 >= k1 and e2 >= k2 and e3 > k3:
    print('The first box is larger than the second one')
elif e1 > k1 and e2 >= k2 and e3 >= k3:
    print('The first box is larger than the second one')
elif e1 >= k1 and e2 > k2 and e3 >= k3:
    print('The first box is larger than the second one')
elif e1 <= k1 and e2 <= k2 and e3 < k3:
    print('The first box is smaller than the second one')
elif e1 < k1 and e2 <= k2 and e3 <= k3:
    print('The first box is smaller than the second one')
elif e1 <= k1 and e2 < k2 and e3 <= k3:
    print('The first box is smaller than the second one')
elif e1 == k1 and e2 == k2 and e3 == k3:
    print('Boxes are equal')
else:
    print('Boxes are incomparable')
