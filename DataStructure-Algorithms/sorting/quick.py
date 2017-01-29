#!/usr/bin/python
'''
best: (n log(n))
worst: O(n^2)
space: O(log(n))  ***inplace '''


def quickSort(lst, start=0, end=None):
    if end is None:
        end = len(lst) - 1
    if start >= end:
        return
    pivot = partition(lst, start, end)
    quickSort(lst, start, pivot - 1)
    quickSort(lst, pivot + 1, end)


def partition(lst, start, end):
    pivot = start
    for i in xrange(start + 1, end + 1):
        if lst[i] <= lst[start]:
            pivot += 1
            lst[i], lst[pivot] = lst[pivot], lst[i]
    lst[pivot], lst[start] = lst[start], lst[pivot]
    return pivot


a = [1, 4, 5, 9, 1, 9, 2, 0, 15, 1, 1, 2, 9]
quickSort(a)
print a
