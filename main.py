#Напишіть функцію squares_list(lst), яка приймає
#список lst чисел та повертає новий список зі
#значеннями, які є квадратами елементів вхідного списку.
#Напишіть код, що демонструє роботу функції та показує
#список з квадратами елементів у деяких списках.
import random
lst = [random.randint(1 , 20) for i in range(5)]
print("Било:" , *lst)
def squares_list(lst):
    return [i ** 2 for i in lst]
print('Стало:', *squares_list(lst))
