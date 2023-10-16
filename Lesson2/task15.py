# Задача №15. Решение в группах
# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

# import random
# n = int(input("Введите количество арбузов: "))

# massa = [random.randint(1, 25) for i in range (n)]
# print(massa)    
# min_weight = min(massa)
# max_weight = max(massa)
# print(f"Для тещи: ", min_weight, "кг")
# print(f"Для себя: ", max_weight, "кг")

import random
# print(random.random())
# print(random.randint(1, 2))
# print('-' * 45)
n = 5
mass_list = []
for _ in range(n):
    mass_list.append(random.randint(1, 10))
print(mass_list)
# print(' *', min(mass_list), max(mass_list))
# print(sum(mass_list))
min_ = mass_list[0]
max_ = mass_list[0]
for i in mass_list:
    if i > max_:
        max_ = i
    if i < min_:
        min_ = i
print(min_, max_)
    