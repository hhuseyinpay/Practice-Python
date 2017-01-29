#!/usr/bin/python
'''
best: (n log(n))
worst: O(n log(n))
space: O(n)'''


def mergeSort(lst):
    if len(lst) < 2:
        return lst[:]
    else:
        middle = int(len(lst) / 2)
        left = mergeSort(lst[:middle])
        right = mergeSort(lst[middle:])
        return merge(left, right)


def merge(left, right):
    if not left or not right:
        return

    result = []
    i, j = 0, 0
    while (len(result) < len(left) + len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break

    return result


a = [1, 4, 123, 2, 4, 5, 1, 1, 1, 122, 0]
print mergeSort(a)
