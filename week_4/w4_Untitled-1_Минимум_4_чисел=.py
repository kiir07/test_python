# Напишите функцию min4(a, b, c, d)
# вычисляющую минимум четырех чисел, которая
# не содержит инструкции if, а использует
# стандартную функцию min от двух чисел.
# Считайте четыре целых числа и выведите их минимум.
# Формат ввода
# Вводятся четыре целых числа.
# Формат вывода
# Выведите ответ на задачу.
a = int(input('Введите число:'))
b = int(input('Введите число:'))
c = int(input('Введите число:'))
d = int(input('Введите число:'))


def min8(a, b, c, d):
    s = min(a, b, c, d)
    return s

print(min8(a, b, c, d))
