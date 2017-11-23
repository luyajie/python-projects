#!/usr/bin/python3.6

# to learn all lists functions

listOfTenNumbers_range = list(range(10))
print(listOfTenNumbers_range)

listOfTenNumbers_comprehension_1 = [x for x in listOfTenNumbers_range]
print(listOfTenNumbers_comprehension_1)

listOfTenNumbers_comprehension_2 = [x for x in range(1, 5)]
print(listOfTenNumbers_comprehension_2)

listOfSquares = [x*x for x in range(1, 10)]
print(listOfSquares)

listOfCubes_2 = []
for x in range(1, 10):
    listOfCubes_2.append(x * x * x)
print(listOfCubes_2)

listOfCubes_2.append("string")
print(listOfCubes_2)

print(listOfCubes_2[0])
print(listOfCubes_2[1])
print(listOfCubes_2[len(listOfCubes_2)-1])
print(listOfCubes_2[len(listOfCubes_2)-2])
print(listOfCubes_2[-1])
print(listOfCubes_2[-3])


subList_1 = listOfCubes_2[2:-2]
print(subList_1)
