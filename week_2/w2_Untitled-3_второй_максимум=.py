# опрарпр..

e1 = e2 = 0
a = -1

while a != 0:
    if a >= e1:
        e2 = e1
        e1 = a
    elif a >= e2 and a <= e1:
        e2 = a
    a = int(input())
print(e2)
