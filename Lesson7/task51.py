# Семинар 7. Функции высшего порядка
# Задача №51. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод: Вывод:
# values = [0, 2, 10, 6] same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)


values = [0, 2, 10, 6]

def same_by(characteristic, objects):
    if len(set(map(characteristic, objects))) in (0, 1):
        return True
    return False

print(same_by(lambda x: x % 2, values))
print(same_by(lambda x: x % 2, []))
print(same_by(lambda x: x > 2, values))