#Задано словник зі словами та їх значеннями. Напишіть
#функцію long_words(dictionary), яка приймає цей
#словник та повертає список всіх слів, що містять не менше
#ніж 5 символів (не забудьте оператор return). Напишіть
#код, що демонструє роботу функції та показує список слів
#у деяких словниках.
def long_words(dictionary):
   return [finish for finish in dictionary if len(finish) >= 5]
slovo = {'Aplle' : 'Frut' , 'Yellow' : 'Color' , 'Marking' : 'Vegetable '}
print(long_words(slovo))