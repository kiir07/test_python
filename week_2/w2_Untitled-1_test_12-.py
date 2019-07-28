# Даны три стороны треугольника a,b,c.
# Определите тип треугольника с заданными сторонами.
# Выведите одно из четырех слов: rectangular
# для прямоугольного треугольника,
# acute для остроугольного треугольника, obtuse для
# тупоугольного треугольника или impossible, если
# треугольника с такими сторонами не существует
# (считаем, что вырожденный треугольник тоже невозможен).
# Формат ввода
# Вводятся три целых числа.
# Формат вывода
# Выведите ответ на задачу.

a = int(input())
b = int(input())
с = int(input())


if с**2 == a**2+b**2:
    print('rectangular')
elif с**2 < a**2+b**2:
    print('acute')
elif с**2 > a**2+b**2:
    print('obtuse')
elif с < a + b:
    print('impossible')
