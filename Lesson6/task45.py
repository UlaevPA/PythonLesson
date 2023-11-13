# Задача №45. Общее обсуждение
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).

# def sum_div(_num_):
#     sum = 0
#     for i in range(1, _num_ // 2 + 1):
#         if _num_ % i == 0:
#             sum += i
#     return sum

# def main():
#     user_num = 100001
#     while user_num > 100000:
#         user_num = int(input("Введите предельное число: "))
#         result_list = []
#         for i in range(1, user_num):
#             sum1 = sum_div(i)
#             sum2 = sum_div(sum1)
#             if i == sum2 and i != sum1:
#                 if {sum1, i} in result_list:
#                     continue
#                 result_list.append({sum1, i})
#         return result_list

# print(main())

def sumDivisitors(num):
    div = (i for i in range(1, int(num / 2) + 1) if num % i == 0)
    # sum_ = sum(list(div))
    return sum(div)

def friendlyNums(num):
    newArray = (sorted([i,sumDivisitors(i)]) for i in range(4, num + 1)
                     if i == sumDivisitors(sumDivisitors(i)) and i !=sumDivisitors(i))
    friendlyArray = dict(newArray)
    return friendlyArray

def printFriendlyDict(dict_):
    for k,v in dict_.items():
        print(k,v)

k = int(input('Ведите число до которого будет осуществляться поиск: '))
printFriendlyDict(friendlyNums(k))