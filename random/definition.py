#!/usr/bin/python

def prhello():
    "Print hello"
    print "Hello, World!"

prhello()

def prlines(str, num):
    "Print num lines consisting of str, repeating str once more on each line."
    for n in range(0,num):
        print str * (n + 1)

prlines('z', 5)
print
prlines('fred ', 4)
