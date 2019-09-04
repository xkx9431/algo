""" 
    quick sort
"""
import random


def quick_sort(arr):

    def quick_sort_c(a, p, r):
        if p >= r:
            return
        q = partition(a, p, r)
        quick_sort_c(a, p, q-1)
        quick_sort_c(a, q+1, r)

    def partition(a, p, r):
        pivot = a[r]
        i = p
        for j in range(p, r):
            if a[j] < pivot:
                a[i], a[j] = a[j], a[i]
                i += 1
        a[i], a[r] = a[r], a[i]
        return i

    quick_sort_c(arr, 0, len(arr)-1)

# advenced quick sort


def advanced_quick_sort(arr):
    if not arr or len(arr) < 1:
        return arr

    def swap(arr, low, upper):
        arr[low], arr[upper] = arr[upper], arr[low]
        return arr

    def Quick_sort_2_wards(arr, low, upper):
        if low >= upper:
            return arr
        # 随机选取基准值, 并将基准值替换到数组第一个元素
        swap(arr, low, random.randint(low, upper))
        tmp = arr[low]
        # 缓存边界值, 从上下边界同时排序
        i, j = low, upper
        while True:
            i += 1
            while i <= upper and arr[i] <= tmp:
                i += 1
            while arr[j] > tmp:
                j -= 1
            if i >= j:
                break
            swap(arr, i, j)
        swap(arr, low, j)
        Quick_sort_2_wards(arr, low, j-1)
        Quick_sort_2_wards(arr, j+1, upper)
        return arr
    return Quick_sort_2_wards(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    a1 = [3, 5, 6, 7, 8]
    a2 = [2, 2, 2, 2]
    a3 = [4, 3, 2, 1]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    quick_sort(a1)
    print(a1)
    quick_sort(a2)
    print(a2)
    quick_sort(a3)
    print(a3)
    quick_sort(a4)
    print(a4)

    a1 = [3, 5, 6, 7, 8]
    a2 = [2, 2, 2, 2]
    a3 = [4, 3, 2, 1]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    advanced_quick_sort(a1)
    print(a1)
    advanced_quick_sort(a2)
    print(a2)
    advanced_quick_sort(a3)
    print(a3)
    advanced_quick_sort(a4)
    print(a4)
