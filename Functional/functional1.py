#!/usr/bin/python3.6

""" functional programming """
# https://maryrosecook.com/blog/post/a-practical-introduction-to-functional-programming
# https://codesachin.wordpress.com/2016/04/03/a-practical-introduction-to-functional-programming-for-python-coders/
# https://www.ibm.com/developerworks/library/l-prog/

from functools import reduce

def print_list_info(lst_name: str, lst: []) -> None:
    print("{0} : {1}".format(lst_name, lst))
    print("length = {0}".format(len(lst)))
    print('---------------------------------')

def square(x):
    return (x, x**2)

def is_square_even(pair):
    return pair[1]%2 == 0

# zip
zip_list = list(zip(range(1,10), range(11, 20)))
print_list_info("zip_list", zip_list)


#  map
# print name length
name_lengths = list(map(len, ["Mary", "Isla", "Sam"]))
print_list_info("name_lengths", name_lengths)

main_list = range(1, 11)

# square all items in a given list
square_old_way = [(x, x**2) for x in main_list]
print_list_info("square_old_way", square_old_way)

square_using_map_lambda = list(map(lambda x: (x, x ** 2), main_list))
print_list_info("square_using_map", square_using_map_lambda)

square_using_map_1 = list(map(square, main_list))
print_list_info("square_using_map_1", square_using_map_1)
### map ###


# reduce
sum = str(reduce(lambda x, a: x + a, main_list, 0))
print("sum: " + sum)

product = str(reduce((lambda x, y: x * y), main_list, 1))
print("product: " + product)
### reduce ###


# filter
even_squares_lambda = list(filter((lambda x: x[1] % 2 == 0), square_using_map_1))
print_list_info("even_squares_lambda", even_squares_lambda)

even_squares_func = list(filter(is_square_even, square_using_map_1))
print_list_info("even_squares_func", even_squares_func)
### filter ###
