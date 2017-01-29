#!/usr/bin/python3
import os


def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
        print ("bytes")
    else:
        value = bytes_or_str
        print ("string")
    return value


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
        print ("string")
    else:
        value = bytes_or_str
        print ("bytes")
    return value


to_str(bytes('a', encoding='ASCII'))
to_str('a')
to_bytes(bytes('a', encoding='ASCII'))
to_bytes('a')

with open('/tmp/random.bin', 'wb') as f:
    f.write(os.urandom(10))

with open('/tmp/random.bin', 'rb') as f:
    print (f.read())
