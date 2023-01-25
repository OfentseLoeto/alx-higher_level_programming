#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    try:
        my_list = [0, 1, 2, 4, 5]

        num = my_list[0]


        print("{:d\n}".format(my_list), end=" ")

    except (ValueError, TypeError):
        pass
        print("")

    return (num)
