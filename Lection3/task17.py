# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
from random import randint
list = []
count = 0
for i in range(7):
    list.append(randint(-10, 10))
print(list)
for i in list:
    if list[0] != list:
        count += 1
print("Встречается", count-1, "разных чисел")