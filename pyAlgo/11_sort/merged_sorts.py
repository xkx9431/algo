"""
merge sort

"""


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    return merge(left, right, arr.copy())


def merge(left, right, merged):
    left_cur, right_cur = 0, 0
    while left_cur < len(left) and right_cur < len(right):
        if left[left_cur] <= right[right_cur]:
            merged[left_cur+right_cur] = left[left_cur]
            left_cur += 1
        else:
            merged[left_cur + right_cur] = right[right_cur]
            right_cur += 1
    for left_cur in range(left_cur, len(left)):
        merged[left_cur+right_cur] = left[left_cur]
    for right_cur in range(right_cur, len(right)):
        merged[left_cur + right_cur] = right[right_cur]

    return merged


if __name__ == "__main__":
    a1 = [3, 5, 6, 7, 8]
    a2 = [2, 2, 2, 2]
    a3 = [4, 3, 2, 1]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    print(merge_sort(a1))
    print(merge_sort(a2))
    print(merge_sort(a3))
    print(merge_sort(a4))
