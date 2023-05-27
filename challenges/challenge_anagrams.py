def bubble_sort(arr):
    '''Return a list sorted'''
    array_length = len(arr)
    for i in range(array_length):
        for j in range(0, array_length-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def is_anagram(first_string, second_string):
    '''Return a tuple with boolean'''
    split_first_string = list(first_string.lower())
    split_second_string = list(second_string.lower())
    a = "".join(bubble_sort(split_first_string))
    b = "".join(bubble_sort(split_second_string))
    return (a, b, a == b)