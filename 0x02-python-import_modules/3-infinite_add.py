#!/usr/bin/python3

if __name__ == "__main__":
    
    import sys

    total = 0
    num = sys.argv

    if len(num) > 1:

        for i in range(1, len(num)):
            total += int(num[i])

            print('{}'.format(total))
