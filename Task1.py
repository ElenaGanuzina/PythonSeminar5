# В файле N натуральных чисел, записанных через пробел. Не хватает одного,
# чтобы выполнялось условие A[i]-1 = A[i-1]. Найти число.

import random

def create_arr():
    path= 'Python\Python5\n.txt'
    data= open(path, 'r')
    array = list(map(int, (data.readline().split(' '))))
    data.close()
    array.remove(random.choice(array))
    print(array)
    return array

def find_num(array):
    if array[0] != 0:
        return 0
    for i in range(1, len(array)):
        if (array[i]-1 != array[i-1]):
            return array[i]-1
    return -1

print(find_num(create_arr()))