def perform_sort(p_array):
    if len(p_array) == 1:
        return p_array
    first_half = get_half(p_array, 0)
    second_half = get_half(p_array, 1)
    s_first_half = perform_sort(first_half)
    s_second_half = perform_sort(second_half)
    return sort_append(s_first_half, s_second_half)


def sort_append(arr1, arr2):
    res = []
    return res


def get_half(p_array, half):
    length = len(p_array)
    h_length = len(p_array) // 2
    lower_bound = 0 if half == 0 else h_length
    upper_bound = h_length if half == 0 else length
    return array if length == 1 else p_array[lower_bound:upper_bound]


import sys

sys.setrecursionlimit(4000)
array = [2, 6, 4, 8, 99, 3, 6, 1, 12, 15]
s_array = perform_sort(array)
print(array)
print(s_array)
