def merge_sort(arr):
    '''Sort an array using merge sort'''
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    '''Merge two arrays'''
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


def is_anagram(first_string, second_string):
    '''Return a tuple with boolean'''
    split_first_string = list(first_string.lower())
    split_second_string = list(second_string.lower())
    a = "".join(merge_sort(split_first_string))
    b = "".join(merge_sort(split_second_string))
    return (a, b, a == b)
