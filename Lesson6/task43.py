# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.

import random

def create_random_list(num):
    return [random.randint(0, 2) for _ in range(num)]

def find_couple(_user_list_: list):
    count_of_couple = 0
    for i in set(_user_list_):
        count_of_couple += _user_list_.count(i) // 2
    return count_of_couple

len_list = int(input("Введите длину массива: "))

user_array = create_random_list(len_list)

print(user_array)
print(find_couple(user_array))
