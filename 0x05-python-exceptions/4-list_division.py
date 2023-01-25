#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    new_list = []

    for i in range(0, list_length)

    try:
        dev = my_list_1[i] / my_list_2[i]
    
    except TypeError:
        print("wrong type")
        dev = 0
        
    except ZeroDivisionError:
        print("Devision by zero")
        dev = 0

    except IndexError:
        print("Out of range")
        dev = 0

    finally:
        new_list append(div)
        return (new_list)

