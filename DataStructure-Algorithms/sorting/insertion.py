#!/usr/bin/python
''' 
best: (n) 
worst: O(n^2)   
space: O(1)      ***inplace'''


def insertion(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
    return array


a = [1, 5, 7, 1, 3, 11, 2, 4]
print insertion(a)
