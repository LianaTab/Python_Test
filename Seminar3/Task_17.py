# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

"""
spisok = [1, 1, 2, 0, -1, 3, 4, 4]
mnoj = set(spisok)
print(len(mnoj))
"""
array = [2, 2, 4, 5, 6]

array2 = []

for i in array:
    if i not in array2:
        array2.append(i)
print(len(array2))