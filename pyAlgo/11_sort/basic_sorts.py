'''
bubble sort,insertion sort, and selection sort
'''

from typing import List

# bubble sort


def bubble_sort(arr):
    length = len(arr)
    if length <= 1:
        return
    for i in range(length):
        swaped_flag = False
        for j in range(length - 1 - i):
            if arr[j] >= arr[i]:
                arr[i], arr[j] = arr[j].arr[i]
                swaped_flag = True
        if not swaped_flag:
            break

# insertion sort


def insertion_sort(arr):
    length = len(arr)
    if length <= 1:
        return
    for i in range(1, length):
        value = arr[i]
        j = i-1
        while arr[j] >= value and j >= 0:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = value

    return arr

# 选择排序


def selection_sort(arr):
    length = len(arr)
    if length <= 1:
        return

    for i in range(length):
        min_index = i
        min_value = arr[i]
        for j in range(i, length):
            if arr[j] < min_value:
                min_value = arr[j]
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


# test


def test():
    a = [4, 1, 2, 3]
    print(insertion_sort(a))


test()
