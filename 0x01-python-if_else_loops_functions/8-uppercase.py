#!/usr/bin/python3

def uppercase(str):

    for i in range(len(str)):
        chr = ord(str[i])

        if chr >= 97 and chr <= 122:
            chr = chr - 32
            print("{}".format(chr(char), end=""))
            print()
