#!/usr/bin/python
'''
best: (nk)
worst O(nk)
space: O(n+k) '''

from math import log


def getDigit(num, base, digitNum):
    return (num // base ** digitNum) % base


def makeBlanks(size):
    return [[] for i in range(size)]


def split(lst, base, digitNum):
    buckets = makeBlanks(base)
    for num in lst:
        buckets[getDigit(num, base, digitNum)].append(num)
    return buckets


def merge(lst):
    newLst = []
    for sublist in lst:
        newLst.extend(sublist)
    return newLst


def maxAbs(lst):
    return max(abs(num) for num in lst)


def splitBySign(lst):
    buckets = [[], []]
    for num in lst:
        if num < 0:
            buckets[0].append(num)
        else:
            buckets[1].append(num)
    return buckets


def radixSort(lst, base):
    passes = int(round(log(maxAbs(lst), base)) + 1)
    newLst = list(lst)
    for digitNum in range(passes):
        newLst = merge(split(newLst, base, digitNum))
    return merge(splitBySign(newLst))


a = [10, 50, 12, 42, 11, 12, 55, 12, 12, 11, 12]
print radixSort(a, 10)
