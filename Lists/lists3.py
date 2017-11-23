#!/usr/bin/python3.6

""" passing list to methods """

# lst is always passed with ref
def add_to_list_1(number, lst):
    print("Adding number {0}".format(number))
    lst.append(number)

# default list is appended each time
def add_to_list_2(number, lst = []):
    print("Adding number {0}".format(number))
    lst.append(number)
    return lst

# new list is created each time
def add_to_list_3(number, lst = None):
    if lst is None:
        lst = []
    print("Adding number {0}".format(number))
    lst.append(number)
    return lst

def print_list_info(lst_name: str, lst: []) -> None:
    print("list {0} is {1}".format(lst_name, lst))
    print("list length is {0}".format(len(lst)))
    print('---------------------------------')


list1 = [1, 2, 3]
print_list_info("list1 1", list1)

add_to_list_1(4, list1)
print_list_info("list1 2", list1)

add_to_list_1(5, list1)
print_list_info("list1 3", list1)

#

list2 = add_to_list_2(4)
print_list_info("list2", list2)

list2_1 = add_to_list_2(5)
print_list_info("list2 1", list2_1)

#

list3 = add_to_list_3(4)
print_list_info("list3", list3)

list3_1 = add_to_list_3(5)
print_list_info("list3 1", list3_1)

#

list4 = [5, 6, 7, 8]
print_list_info("list4", list4)

list4_1 = add_to_list_2(9, list4)
print_list_info("list4_1", list4_1)

#

list5 = [11, 12, 13, 14]
print_list_info("list5", list5)

list5_1 = add_to_list_2(9, list5)
print_list_info("list5_1", list5_1)

