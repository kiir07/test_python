# Сортировка списков
# В программировании очень часто удобнее работать с отсортированными данными
# В языке Питон существует возможность отсортировать списки двумя способами.
# Рассмотрим их на примере решения простой задачи о сортировке последовательности
# чисел по неубыванию (это как по возрастанию, но, возможно, с одинаковыми числами).
# Вот первый способ упорядочить его:

myList = list(map(int, input().split()))
myList.sort()
print(' '.join(map(str, myList)))

# Второй способ состоит в применении функции sorted, которая возвращает отсортированный список, но не изменяет значение своего параметра:

myList = list(map(int, input().split()))
sortedList = sorted(myList)
print(' '.join(map(str, sortedList)))

# Функция sorted может принимать в качестве параметра не только список, но и что угодно итерируемое: кортежи, iterable или строки:

print(sorted((1, 3, 2)))
print(sorted(range(10, -1, -2)))
print(sorted("cba"))


# При этом sorted всегда возвращает список, т.е. вывод этой программы будет такой:
# [1, 2, 3]
# [0, 2, 4, 6, 8, 10]
# ['a', 'b', 'c']
# Сортировку можно применять к спискам, все элементы которых сравнимы между собой.
# Обычно это однородные списки (состоящие из элементов одного типа) или, в редких случаях, целые и вещественные числа вперемешку.

# Сравнение кортежей и списков
# Два кортежа или списка можно также сравнивать между собой. Например, выражение (1, 2, 3) < (2, 3, 4)
# будете истинным, а [1, 2, 3] < [1, 2] ложным. Сравнение кортежей и списков происходит поэлементно,
# как и сравнение строк. Как только на каких-то позициях кортежа или списка встретились различные элементы,
# то взаимный порядок кортежей такой же, как у этих элементов. Если же различий найдено не было,
# то меньше тот кортеж, который короче. Всё в точности как при сравнении строк.

# Естественно, сравниваемые кортежи или списки должны содержать на соответствующих позициях
# сравнимые элементы. Попытка сравнить кортеж (1, 2) с кортежем ("Some text", 42) приведет к
# ошибке (а сравнение (1, 2) с (42, "Some text") к ошибке не приведет). Обычно, всё же,
# сравниваются кортежи, состоящие из элементов одинакового типа.

# Это свойство кортежей можно использовать для решения сложных задач на сортировку.

# Пусть для каждого человека задан его рост и имя,
# необходимо определить упорядочить список людей по росту,
# а в случае одинакого роста - в алфавитном порядке. При решении
# этой задачи достаточно хранить описание каждого человека в виде
# кортежа, где первым элементом будет рост, а вторым - фамилия.
# Рассмотрим пример: для каждого человека задан рост и его имя.
# Необходимо упорядочить их по возрастанию роста, а в случае одинакового роста - в алфавитном порядке.

n = int(input())
peopleList = []
for i in range(n):
    tempManData = input().split()
    manData = (int(tempManData[0]), tempManData[1])
    peopleList.append(manData)
peopleList.sort()
for manData in peopleList:
    print(' '.join(map(str, manData)))


# В этом примере нам повезло и удалось составить кортеж,
# который содержит параметры сравниваемых людей ровно в нужном порядке.
# Часто встречаются более неприятные ситуации. Рассмотрим ту же задачу,
# но теперь людей нужно упорядочить по убыванию роста, но в случае одинакового
# роста они по-прежнему должны быть упорядочены по алфавиту. Простое использование
# reversed=True не приведет к желаемому результату: люди с одинаковым ростом будут стоять в неправильном порядке.

# Здесь можно применить хитрость и превратить рост каждого человека в отрицательное
# число, модуль которого будет равен исходному росту. После этого список можно просто
# упорядочить по возрастанию - самые высокие люди будут иметь наименьший отрицательный
# "рост", по которому происходит сравнение в первую очередь. Перед выводом необходимо
# превратить рост обратно в положительное число.

n = int(input())
peopleList = []
for i in range(n):
    tempManData = input().split()
    manData = (-int(tempManData[0]), tempManData[1])
    peopleList.append(manData)
peopleList.sort()
for badManData in peopleList:
    manData = (-badManData[0], badManData[1])
    print(' '.join(map(str, manData)))

# Этот код малопонятен и плох.

# Параметр key в функции sort
# Для реализации нестандартных сортировок лучше не уродовать исходные данные, 
# а использовать параметр key, передающийся в функцию сортировки.

# Значением этого параметра должна быть функция, которая применяется к каждому
# элементу списка и затем сравнение элементов происходит по значению этой функции (оно называется ключом).

# Рассмотрим такой пример: необходимо упорядочить введённые строки по длине,
# а в случае равной длины оставить их в том порядке, как они шли во входном файле.
# Например, для входных строк ''c'', ''abb'', ''b'' правильным ответом должно быть
# ''c'', ''b'', ''abb'' (''c'' идет раньше ''b'', т.к. они имеют равную длину, а ''c'' стояло во входных данных раньше ''b'').

# К счастью, сортировка, используемая в Питоне обладает свойством устойчивости (stable), т.е. для элементов с равным ключом сохраняется их взаимный порядок.

# Решение этой задачи будет выглядеть следующим образом:

n = int(input())
strings = []
for i in range(n):
    strings.append(input())
print('\n'.join(sorted(strings, key=len)))

# В качестве еще одного примера рассмотрим задачу о сортировке точек на плоскости,
# заданных парой целых координат x и y по неубыванию расстояния от начала координат.
# В данном случае в качестве функции для генерации ключа, по которому будут сравниваться
# элементы, мы напишем свою функцию, которая будет возвращать квадрат расстояния от точки
# до начала координат. Квадрат расстояния мы используем для того, чтобы оставаться в целых
# числах и избавится от необходимости считать квадратный корень (медленно и неточно):
def dist(point):
    return point[0] ** 2 + point[1] ** 2

n = int(input())
points = []
for i in range(n):
    point = tuple(map(int, input().split()))
    points.append(point)
points.sort(key=dist)
for point in points:
    print(' '.join(map(str, point)))
# Здесь каждый элемент списка - кортеж из двух чисел.
# Именно такой параметр принимает наша функция. Возможно, вы хотели бы использовать функцию
# hypot из библиотеки math, чтобы не писать свою функцию подсчета ключа, однако это невозможно - она ожидает на вход два числовых параметра, а не кортеж.



