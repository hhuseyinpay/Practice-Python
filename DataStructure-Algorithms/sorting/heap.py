#!/usr/bin/python
'''
best: (n log(n))
worst: O(n log(n))
space: O(1)     ***inplace'''


def heapify(lst, end, i):
    left = 2 * i + 1
    right = 2 * (i + 1)
    max = i

    if left < end and lst[i] < lst[left]:
        max = left
    if right < end and lst[max] < lst[right]:
        max = right
    if max != i:
        lst[i], lst[max] = lst[max], lst[i]
        heapify(lst, end, max)


def heapSort(lst):
    end = len(lst)
    start = end
    for i in range(start, -1, -1):
        heapify(lst, end, i)
    for i in range(end - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        heapify(lst, i, 0)


a = [1, 4, 6, 2, 2, 1, 4, 5, 1, 1, 123, 2, 4]
heapSort(a)
print a
