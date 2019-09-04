from typing import Optional


def bsearch(arr: List[int], target: int) -> int:
    """ bsearch for a target in a sorted arr
    """
    low, high = 0, len(arr)-1
    while low <= high:
        mid = low + (high + low) >> 1
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid

    return -1


def bsearch_recur(arr: List[int], targrt: int) -> int:
    return bsearch_recur_inter(arr, len(arr)-1, 0, targrt)


def bsearch_recur_inter(arr: List[int], high: int, low: int, target: int) -> int:
    if low > high:
        return -1
    mid = low + (high-low) >> 1
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return bsearch_recur(arr, high, mid+1, target)
    else:
        return bsearch_recur_inter(arr, mid-1, low, target)
