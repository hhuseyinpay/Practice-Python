#!/usr/bin/python

snoggle = 17
def wongle(n):
    snoggle = n

print 'A:', snoggle,
wongle(245)
print snoggle

def wangle(n):
    global snoggle
    snoggle = n

print 'B:', snoggle,
wangle(235)
print snoggle

def snapple(n):
    n = 55

print 'C:', snoggle,
snapple(snoggle)
print snoggle

def snarffle(z):
    z.append(22)

toggle = [ 'a', 'b', 'c' ];
print 'D:', toggle,
snarffle(toggle)
print toggle

def snarggle(z):
    z= [ 4, 5 ]

print 'F:', toggle,
snarggle(toggle)
print toggle
