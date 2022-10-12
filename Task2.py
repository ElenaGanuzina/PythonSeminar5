# Дан список чисел. Создать список, в который попадают числа, 
# описывающие возрастающую последовательность. 
# порядок элементов менять нельзя.

import random

def create_list(num):
    return random.choices(range(num * 2), k=num)

def new_list(array):
    new_list = []
    for i in range(len(array)):
        any = array[i]
        arr = [any]
        for j in range(i+1, len(array)):
            if array[j] > any:
                arr.append(array[j])
                any = array[j]
        if len(array) > 1:
            new_list.append(arr)
    return new_list



m = create_list(10)
print(m, new_list(m), sep="\n")
