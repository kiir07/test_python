# Чтобы определить длину строки s можно воспользоваться функцией len(s) - она возвращает целое число, равное длине строки.

# Срез - это способ извлечь из строки отдельные символы или подстроки. 
# При применении среза конструируется новая строка, строка, к которой был применён срез, остается без изменений.

# Простейший вид среза - это обращение к конкретному символу строки по номеру. 
# Чтобы получить i-ый символ строки нужно написать s[i]. 
# В результате этого будет сконструирована строка, содержащая только один символ --- тот,
#  который стоял на месте i. Нумерация символов идет с нуля, при попытке обратиться к символу с номером больше либо равном длине строки возникает ошибка.

# В языке Питон присутствует и нумерация символов строки отрицательными числами. 
# Последний символ строки имеет номер -1, предпоследний -2 и так далее. При попытке обратиться к символу с номером, меньшим чем -len(s) возникает ошибка.

# Нумерация символов в строке ''String'' представлена в таблице:

# S	    t	r	i	n	g
# 0	    1	2	3	4	5
# -6	-5	-4	-3	-2	-1

# Если первый параметр находится правее второго, то будет сгенерирована пустая строка.

# Также существует срез с тремя параметрами, где третий параметр задает шаг, 
# с которым нужно брать символы. Например, можно взять все символы с начала до конца с шагом 2,
#  это будет выглядеть как s[::2], в результате чего получится строка "Srn".
#   Естественно, первый и второй параметры можно не опускать. 
#   Если третий параметр не указан, т.е. в квадратных скобках записано только одно двоеточие, то шаг считается равным 1.

# Шаг в срезе может быть и отрицательным, в таком случае первый параметр должен находится правее второго. 
# Например, s[5:1:-2] даст строку "gi - 5-ый и 3-ий символы, а символ с номером 1 уже не входит. 
# Развернутую строку можно получить срезом s[::-1] -все символы от "начала" до "конца" в обратном порядке. 
# # Если третий параметр отрицательный, то началом среза считается последний символ, а концом - позиция перед нулевым символом.

# Существуют модификации этих методов с двумя параметрами. 
# s.find(substring, from) будет осуществлять поиск в подстроке s[from:]. 
# Например, 'String'.find('ing', 1) вернет 3 (нумерация символов остается как в исходной строке). 
# По аналогии со срезами параметры могут быть и отрицательными.

# Также есть модификации с тремя параметрами: они ищут подстроку в срезе s[a:b].

# Часто возникает задача найти и вывести все вхождения подстроки в строку, включая накладывающиеся. 
# Например, для строки 'ABABA' и подстроки 'ABA' ответ должен быть 0, 2. Ее решение выглядит так:

string = input()
substring = input()
pos = string.find(substring)
while pos != -1:
    print(pos)
    pos = string.find(substring, pos + 1)

# Метод rfind работает аналогично find, но ищет самое правое вхождение.

# Метод replace(old, new) позволяет заменить все вхождения подстроки old на подстроку new. 
# При этом конструируется новая строка, где были произведены замены. Нужно обратить внимание,
#  что метод replace заменяет вхождения подстрок без учета предыдущих совершенных замен.
#   Если применить следующую операцию 'AAAAAA'.replace('AA', 'A'), то в результате получится строка 'AAA', а не 'A', как можно было бы ожидать.

# Фактически, можно считать, что метод replace находит очередное вхождение подстроки old,
#  осуществляет замену и продолжает поиск с позиции после всех замененных символов (без наложения и поиска в свежезамененной части).

# Существует модификация replace(old, new, count), которая осуществляет не более count замен самых левых вхождений подстроки old.

# Также для строк существует метод count, который позволяет подсчитать количество вхождений подстроки. 
# По аналогии с методом find определены методы count с двумя и тремя параметрами.