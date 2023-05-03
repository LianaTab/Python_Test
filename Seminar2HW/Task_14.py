# Задача 14: Требуется вывести все целые степени двойки 
# (т.е. числа вида 2k), не превосходящие числа N.

IntNum = int(input("Введите число: "))
i = 0
number = 0
for i in range(IntNum): # Лучше решить через цикл while
    number = 2**i
    if number <= IntNum:
        print(f"{number}")
    else:
        quit()