# Задача 8: Требуется определить, можно ли от шоколадки размером 
# n × m долек отломить k долек, если разрешается сделать один разлом 
# по прямой между дольками (то есть разломить шоколадку на два 
# прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('Введите количество долек n: '))
m = int(input('Введите количество долек m: '))
k = int(input('Введите количество долек, которые нужно отломить: '))

if (k <= n * m) and k % n == 0 or k % m == 0:
    print("Yes")
else:
    print("No")


