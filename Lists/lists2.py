#!/usr/bin/python3.6

""" list splicing and comprehension """
import math


def print_list_info(lst_name: str, lst: []) -> None:
    print("list {0} is {1}".format(lst_name, lst))
    print("list length is {0}".format(len(lst)))
    print('---------------------------------')


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print_list_info("list1", list1)

list2 = list1[2:5]
print_list_info("list2", list2)

list3 = list1[6:-1]
print_list_info("list3", list3)

list4 = list2 + list3
print_list_info("list4", list4)

list4 = list4 + list3
print_list_info("list4 (again)", list4)

list4.extend(list3)
print_list_info("list4 (again 2)", list4)

list5 = list4 * 2
print_list_info("list5", list5)

# comprehension with condition
list6 = [x * x for x in list1 if x * x % 3 == 0]
print_list_info("list6", list6)

# comprehension with condition
list7 = ["sqrt of {0}={1}".format(x, math.sqrt(x)) for x in list1]
print_list_info("list7", list7)

# comprehension with lambda - generator
list8 = list(map(lambda x: x**2, range(1, 11)))
print_list_info("list8", list8)
