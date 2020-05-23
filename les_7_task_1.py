# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком. Улучшенные
# версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.


import random
size = 20
array = [random.randint(-100,100) for i in range(size)]

# классический вариант
def bubble_sort(array):
    n = 1
    while n < len(array):
        for i in range(len(array) - n):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1

# улучшение 1. если при очередном проходе по последовательности не было ни одной замены, значит уже выстроена
# последовательность
def bubble_sort2(array):
    n = 1
    while n < len(array):
        k = True

        for i in range(len(array) - n):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                k = False
        if k:
            break
        n += 1
# улучшение 2. при каждом проходе ищем сразу макимум и "гоним" его в конец неотсортированной части
def bubble_sort_max(array):
    n = 1
    while n < len(array):
        nmax = max(array[:len(array) - n])
        for i in range(array.index(nmax), len(array) - n):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1

ar = array.copy()
print(f'{array} - Исходная последовательность', '\n', '-'*100)
ar = array.copy()
bubble_sort(ar)
print(f'{ar} - Сортировка классическая')
ar = array.copy()
bubble_sort2(ar)
print(f'{ar} - Сортировка с учетом сортированной части')
ar = array.copy()
bubble_sort_max(ar)
print(f'{ar} - Сортировка с учетом поиска максимума')