#!/usr/bin/python


def sort(lst, minimum, maximum):
    maximum += 1
    count = [0] * maximum
    for i in lst:
        count[i] += 1
    result = []
    for i in range(minimum, maximum):
        result += [i] * count[i]
    return result


a = [1, 4, 5, 1, 2, 5, 0, 0, 11, 14, 1, 0, 2, 13]
print sort(a, 0, 14)
