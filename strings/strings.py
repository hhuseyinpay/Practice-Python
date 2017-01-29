#!/usr/bin/python

s1 = 'I\'m single'

s2 = "I'm double double"

s3 = '''I'm very long-winded and Ireally need
to take up more than one line.  That way I can say all the very
`important' things which I must tell you.  Strings like me are useful
when you must print a long set of instructions, etc.'''

s4 = 'left' "right" 'left'

s5 = s1 + "\n" + s2

print s5 + '\n' + s3, "\n", s4

print 's5 has', len(s5), ' characters'
