"""
count sort
"""

from typing import List
import itertools


def counting_sort(arr: List[int]):
    if len(arr) <= 1:
        return
    counts = [0] * (max(arr)+1)
    for num in arr:
        counts[num] += 1
    counts = list(itertools.accumulate(counts))
    print(counts)

    arr_tmp = [None] * len(arr)
    for num in arr:
        index = counts[num] - 1
        arr_tmp[index] = num
        counts[num] -= 1
    arr[:] = arr_tmp


if __name__ == "__main__":
    arr = [4, 5, 0, 9, 3, 3, 1, 9, 8, 7]
    print(arr)
    counting_sort(arr)
    print(arr)
