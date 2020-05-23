# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
# на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random
size = 25
array = [random.randint(0,50) for i in range(size)]
print(f'Исходная последовательность: {array}')

def merge(left,right):
    res = []
    i,j = 0,0
    while (i < len(left)) and (j < len(right)):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    while (i < len(left)):
        res.append(left[i])
        i += 1
    while (j < len(right)):
        res.append(right[j])
        j += 1
    return res

def merge_sort(array):
    if len(array) < 2:
        return array
    m = len(array)//2
    left = merge_sort(array[:m])
    right = merge_sort(array[m:])
    return(merge(left,right))

ss = merge_sort(array)
print(f'После сортировки:            {ss}')