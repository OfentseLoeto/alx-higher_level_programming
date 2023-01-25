#!/usr/bin/python3

safe_print_list_integers = __import__('2-safe_print_list_integers').safe_print_list_integers



num = [1, 2, 3, 4, 5]



nb_print = safe_print_list_integers(num, 2)

print("nb_print: {:d}".format(nb_print))



num = [1, 2, 3, "School", 4, 5, [1, 2, 3]]

nb_print = safe_print_list_integers(num, len(num))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(num, len(num) + 2)

print("nb_print: {:d}".format(nb_print))
