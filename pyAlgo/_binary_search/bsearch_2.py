"""
some implement for special case in bsearch Scenario
"""
from typing import Optional


def b_search_left_first(arr: List[int], target: int) -> int:
    lo, hi = 0, len(arr)-1
    while lo <= hi:
        mid = lo + (hi-lo) // 2
        if arr[mid] > target:
            hi = mid - 1
        elif arr[mid] > target:
            lo = mid + 1
        else:
            # ( check if left is the target yet)
            if mid == 0 or arr[mid - 1] != target:
                return mid
            else:
                hi = mid - 1
    return -1


def b_search_right_last(arr: List[int], target: int) -> int:
    lo, hi = 0, len(arr)-1
    while lo <= hi:
        mid = lo + (hi-lo) // 2
        if arr[mid] > target:
            hi = mid - 1
        elif arr[mid] > target:
            lo = mid + 1
        else:
            # ( check if right is the last yet)
            if mid == len(arr)-1 or arr[mid + 1] != target:
                return mid
            else:
                lo = mid + 1
    return -1


def b_search_first_large(arr: List[int], target: int):
    """
    BINARY search for not less than a target in an ascending sorted array
    """

    lo, hi = 0, len(arr)-1
    while lo <= hi:
        mid = lo + (hi - lo) >> 1
        if arr[mid] < target:
            lo = mid + 1
        else:
            if mid == 0 or arr[mid - 1] < target:
                return mid
            else:
                hi = mid + 1

    return -1


def b_search_last_less(arr: List[int], target: int) -> int:
    lo, hi = 0, len(arr)-1
    while lo <= hi:
        mid = lo + (hi-lo)//2
        if arr[mid] > target:
            hi = mid - 1
        else:
            if mid == len(arr) - 1 or arr[mid+1] > target:
                return mid
            else:
                lo = mid + 1
    return -1


if __name__ == "__main__":
    a = [1, 1, 2, 3, 4, 6, 7, 7, 7, 7, 10, 22]

    print(b_search_left_first(a, 0) == -1)
    print(b_search_left_first(a, 7) == 6)
    print(b_search_left_first(a, 30) == -1)

    print(b_search_right_last(a, 0) == -1)
    print(b_search_right_last(a, 7) == 9)
    print(b_search_right_last(a, 30) == -1)

    print(b_search_first_large(a, 0) == 0)
    print(b_search_first_large(a, 5) == 5)
    print(b_search_first_large(a, 30) == -1)

    print(b_search_last_less(a, 0) == -1)
    print(b_search_last_less(a, 6) == 5)
    print(b_search_last_less(a, 30) == 11)
