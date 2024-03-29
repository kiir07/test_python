# Многие приемы и функции для работы со строками также подходят и для кортежей, например, можно складывать два кортежа:
a = (1, 2, 3)
b = (4, 5, 6)
print(a + b)
# В результате применения этой операции будет выведено (1, 2, 3, 4, 5, 6).
# В случае сложения создается новый кортеж, который содержит в себе элементы сначала из первого,
# а затем второго кортежа (точно так же как и в случае со строками).
# Также кортеж можно умножить на число, результат этой операции аналогичен умножению строки на число.

# Приведем пример, когда опускание скобок приводит к ошибке. (1, 2) + (3, 4)
# будет давать (1, 2, 3, 4), а 1, 2 + 3, 4 будет давать (1, 5, 4), т. к.
# сумма будет понята Питоном как выражение для второго элемента кортежа.

# Кортеж можно получить из строки, вызвав функцию tuple от строки.
# В результате каждая буква станет элементом кортежа. К кортежу можно
# применять функцию str, которая вернет текстовое представление кортежа
# (элементы, перечисленные через запятую с пробелом и разделенные пробелами).

# В одном кортеже могут храниться элементы различных типов, например, строки,
# числа и другие кортежи вперемешку. Например, в кортеже myTuple = (('a', 1, 3.14), 'abc', ((1), (2, ))),
# myTuple[0] будет кортежем ('a', 1, 3.14), myTuple[1] строкой 'abc', а myTuple[2]
# кортежем состоящим из числа 1 и кортежа из одного элемента (2, ). Числа, записанные в скобках,
# интерпретируются как числа, в случае возникновения необходимости создать кортеж из одного
# элемента необходимо после значения элемента написать запятую. Если вывести myTuple[2][1],
# то напечатается (2,), а если вывести myTuple[2][1][0], то будет напечатано число 2.

# Кортеж, содержащий в себе один элемент, называется синглтоном. Как и к строкам,
# к кортежам можно применять операцию среза с тем же смыслом параметров. Если в срезе
# один параметр, то будет возвращена ссылка на элемент с соответствующим номером. Например,
# print((1, 2, 3)[2]) напечатает 3. Если же в срезе более одного параметра, то будет сконструирован
# кортеж, даже если он будет синглтоном. Например, в случае вызова print((1, 2, 3)[1:])
# будет напечатано (2, 3), а в случае вызова print((1, 2, 3)[2:]) будет напечатан синглтон (3,).

manDesc = ("Ivan", "Ivanov", 28)
name, surname, age = manDesc

# В переменной name кажется ''Ivan'', в surname - ''Ivanov'', а в переменной age число 28. На английском распаковка кортежа называется tuple unpacking.
# Процесс создания кортежа называется упаковкой кортежа.
a, b, c = 1, 2, 3
a, b, c = c, b, a
print(a, b, c)

# будет выведено 3 2 1. Обратите внимание, что функции print передается в качестве параметра не кортеж, а три целых числа.
# Главное что нужно понять, что записать вида (a, b, c) = (c, b, a)
# не эквивалентна цепочке присваиваний вида a = c; b = b; c = a.
# Такая цепочка присваиваний привела бы к тому, что в переменных a, b, c оказались бы значения 3, 2, 3.

# Функция range

print(tuple(range(10)))
# то будет напечатано (0, 1, 2, 3, 4, 5, 6, 7, 8, 9). Функция range с одним параметром n генерирует iterable, содержащий последовательные числа от 0 до n-1.

# Существует вариант range с двумя параметрами, range(from, to) сгенерирует iterable со всеми числами от from до to-1 включительно.

# Также существует range с тремя параметрами range(from, to, step), который сгенерирует iterable с числами от from,
# не превышающие to с шагом изменения step. Если шаг отрицателен, то from должен быть больше to. Например,
# range(10, 0, -2) сгенерирует последовательность чисел 10, 8, 6, 4, 2. 0 не будет входить в эту последовательность.

# Цикл for
# Цикл for позволяет поочередно перебрать элементы из чего-нибудь итерируемого (iterable или tuple). Например, мы можем перебрать названия цветов яблок таким способом:

for color in ('red', 'green', 'yellow'):
    print(color, 'apple')

# В результате выполнения этой программы будет напечатано:
# red apple
# green apple
# yellow apple
# На место переменной color
# будут поочередно подставляться значения из кортежа. В общем случае цикл for выглядит так for
# имяПеременной in нечтоИтерируемое:

# Часто for используется вместе с функцией range. Например, с помощью for можно напечатать нечетные числа от 1 до 100:
for i in range(1, 100, 2):
    print(i)

# Внутри for может быть расположен и другой for. Вот так выглядит код для вывода таблицы умножения всех чисел от 1 до 10 (не очень красивой):

for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=' ')
    print()


