import os

i = 0;
while(1):
    i += i
    print i
    os.fork()
