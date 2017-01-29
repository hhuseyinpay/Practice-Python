#!/usr/bin/python

a = [1, 2, 3, 4, 5, 11, 10, 9, 8]
it = (x for x in a)
print(it)
print(next(it))

roots = ((x, x**0.5) for x in it)
print (roots)
print(next(roots))
