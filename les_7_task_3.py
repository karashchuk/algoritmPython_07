# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой — не больше медианы.

# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте
# метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).

import random
m = 10
array = [random.randint(0,50) for i in range(2*m+1)]
print(f'{array} - исходная последовательность')

def median(array):
    el = random.choice(array)
    def count_arr(el):
        l = []
        r = []
        m = []
        for i in array:
            if i < el:
                l.append(i)
            elif i > el:
                r.append(i)
            elif i == el:
                m.append(i)
        return (l, m, r)

    while True:
        l, m, r = count_arr(el)
        result = m[0]
        if abs(len(l) - len(r)) <= len(m):
            break
        else:
            if len(l) < len(r):
                el = random.choice(r)
            else:
                el = random.choice(l)
    return(m[0])
print(f'Медиана = {median(array)}')

# Проверим
print ('-'*30, 'Проверка', '-'*30)
s_arr = sorted(array)
print(f'{s_arr} - после сортировки')
print(f'Число посредине: {s_arr[len(s_arr)//2]}')

