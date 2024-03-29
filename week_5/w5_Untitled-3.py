# Метод split позволяет разрезать строку (string) на отдельные слова ("токены").
# В качестве разделителя может выступать пробел, символ табуляции или перевода строки. Этот метод не изменяет строку и возвращает список строк-токенов.
# Например, если запустить такую программу
print('red green        blue'.split())
# то будет напечатано ['red', 'green', 'blue']. Количество разделителей между токенами не играет роли.

# Чтобы научиться читать числа из одной строки нужно научиться еще одной функции - map.
# Функция map принимает два параметра: первый это функции, а второй - iterable элементов,
# к которому нужно применить эту функцию. В результате получается iterable с результатом применения функции к каждому элементу списка параметра.
# Например, такой код:
print(list(map(len, ['red', 'green', 'blue'])))
# напечатает [3, 5, 4] - список с результатом применения функции len к списку ['red', 'green', 'blue'].

# Метод split в сочетании с функцией map удобно использовать для считывания списка чисел,
# записанных в одну строку и разделенных пробелами. Такое считывание будет выглядеть так:
numList = list(map(int, input().split()))
# Сначала осуществляется считывание строки, затем выполняется метод split,
# который создает список токенов, состоящих из цифр, а затем к каждому токену применяется функция int. В результате этого получается список цифр.

# Метод join позволяет объединить iterable строк, используя ту строку, к которой он применен, в качестве разделителя. Например, такой код:
print(', '.join(['Veni', 'Vidi', 'Vici']))
# выведет Veni, Vidi, Vici. Строка ', ' будет выступать в качестве разделителя который будет вставляться после каждой строки из списка-параметра (кроме последней).

# Метод join позволяет быстро и коротко выводить списки чисел.
# Проблема в том, что он умеет принимать в качестве параметра только iterable строк.
# Но с помощью функции map мы можем легко получить iterable из списка чисел,
# применив к каждому элементу функцию str. Вывод списка чисел numList разделенных пробелами будет выглядеть так:

numList = [1, 2, 3]
print(' '.join(map(str, numList)))


# К переменным типа список можно применять методы, перечислим некоторые из них:

# Методы, не изменяющие список и возвращающие значение:

# count(x) - подсчитывает число вхождений значения x в список. Работает за время O(N)

# index(x) - находит позицию первого вхождения значения x в список. Работает за время O(N)

# index(x, from) - находит позицию первого вхождения значения x в список, начиная с позиции from. Работает за время O(N)

# Методы, не возвращающие значение, но изменяющие список:

# append(x) - добавляет значение x в конец списка

# extend(otherList) - добавляет все содержимое списка otherList в конец списка. В отличие от операции + изменяет объект к которому применен, а не создает новый

# remove(x) - удаляет первое вхождение числа x в список. Работает за время O(N)

# insert(index, x) - вставляет число x в список так, что оно оказывается на позиции index.
# Число, стоявшее на позиции index и все числа правее него сдвигаются на один вправо. Работает за время O(N)

# reverse() - Разворачивает список (меняет значение по ссылке, а не создает новый список как myList[::-1]). Работает за время O(N)

# Методы, возвращающие значение и изменяющие список:

# pop() - возвращает последний элемент списка и удаляет его

# pop(index) - возвращает элемент списка на позиции index и удаляет его. Работает за время O(N)