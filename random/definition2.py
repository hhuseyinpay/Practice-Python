#!/usr/bin/python

def dink(base, middles = [ 'red', 'blue' ], end = '.'):
    'Silly sentence generator.'
    for m in middles:
        print base + m + end

dink('The paint is ')
print
dink('The walls are ', ['painted', 'cracked', 'ugly'], ' like mine.')
print
dink('My car is ', end = ' and braken.')
print
dink ('', end = ' with chickens.',
        middles = ['Eating', 'Dancing', 'Watching TV'])
