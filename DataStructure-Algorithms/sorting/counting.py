#!/usr/bin/python
'''
best: (n+k)
worst: O(n+k)
space O(k)'''


def countingSort(lst, maxVal):
    maxVal += 1
    count = [0] * maxVal
    for i in lst:
        count[i] += 1
    j = 0
    for i in range(maxVal):
        for k in range(count[i]):
            lst[j] = i
            j += 1
    return (lst)


a = [1, 4, 5, 1, 2, 5, 0, 00, 11, 14, 1, 0, 2, 13]
print countingSort(a, 14)
