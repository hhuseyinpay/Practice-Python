#!/usr/bin/python

#
# This program evaluates polynomials.  It first asks for the coefficients
# of a polynomial, which must be entered on one line, highest-order first.
# It then requests values of x and will compute the value of the poly for
# each x.  It will repeatly ask for x values, unless you the user enters
# a blank line.  It that case, it will ask for another polynomial.  If the
# user types quit for either input, the program immediately exits.
#

# Need some string services, and some standard system services.
import string, sys

#
# Function to evaluate a polynomial at x.  The polynomial is given
# as a list of coefficients, from the greatest to the least.

def polyval(x, coef):
    '''Evaluate at x the polynomial with coefficients given in coef.
        The value p(x) is returned.'''

    sum = 0
    while 1:
        sum = sum + coef[0]
        coef = coef[1:]
        if not coef: break
        sum = sum * x
    return sum


#
# Function to read a line containing a list of integers and return
# them as a list of integers.  If the string conversion fails, it
# returns the empty list.  If the input line is the word 'quit', then
# it exits the program (which is actually accomplished with an exception).
# Other exceptions are passed on.

def readints(prompt):
     '''Read a line of integers and return the list of integers.'''
     line = raw_input(prompt)
     if line == 'quit': sys.exit(0)

     retval = [ ];
     for str in string.split(line):
         try:
             retval.append(int(str))
         except ValueError:
             print 'Conversion of', str, 'failed.'
             return [ ]
         return retval

def polystr(p):
    exp = len(p)

    retval = ''
    while p:
        exp = exp - 1

        coef = p[0]
        p = p[1:]

        if coef == 0: continue

        if retval:
            if coef >= 0:
                retval = retval + ' + '
            else:
                coef = -coef
                retval = retval + ' - '

        if coef != 1 or exp == 0:
            retval = retval + str(coef)
            if exp != 0: retval = retval + '*'

        if exp != 0:
            retval = retval + 'x'
            if exp != 1: retval = retval + '^' + str(exp)

    if not retval: retval = '0'

    return retval

try:
    while 1:
        while 1:
            poly = readints('Enter a polynomial coefficients: ')
            if poly: break
            print 'Try again.'

        while 1:
            resp = raw_input('Enter x value or blank line: ')
            if resp == 'quit': sys.exit(0)
            if not resp: break

            try:
                x = int(resp)
            except ValueError:
                print "That doesn't look like an integer. Please try again."
            else:
                print 'p(x) =', polystr(poly)
                print 'p(' + str(x) + ') =', polyval(x, poly)

except (EOFError, KeyboardInterrupt):
    print
