#Напишіть функцію count_vowels(s), яка приймає
#аргумент у вигляді рядка s та повертає кількість
#голосних літер у цьому рядку. Напишіть код, що
#демонструє роботу функції та показує кількість
#голосних літер у деяких рядках.
s = input("Введіть текст: ")
def count_vowels(s):
    abs = 'qeyuioaQEYUIOA'
    count = 0
    for finish in s :
        if finish in abs:
            count += 1
    print()
    print('Текст:' , s)
    print('Кількість голосних в тексті' , count)
count_vowels(s)