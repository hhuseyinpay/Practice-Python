#!/usr/bin/python3

a = ['hasan', 'huseyin', 'pay']
for i, x in enumerate(a):
    print('%d: %s' % (i + 1, x))
#------------
for i, x in enumerate(a, 1):
    print('%d: %s' % (i, x))
