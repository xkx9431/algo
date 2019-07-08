""" 
    quick sort
"""


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
