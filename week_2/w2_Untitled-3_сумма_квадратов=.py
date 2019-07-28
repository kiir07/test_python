# По данному натуральному n вычислите сумму 1²+2²+3²+...+n².
# Формат ввода
# Вводится натуральное число.
# Формат вывода
# Выведите ответ на задачу.

n = int(input())
sumSquare = 0
i = 1
while n >= i:
    sumSquare = sumSquare + i * i
    i += 1
print(sumSquare)
