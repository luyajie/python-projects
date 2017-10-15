
def __get_tuple1():
    return (123, 'VOD LN', 'Vodafone', 23.36000061)

def __get_tuple2():
    return (123, 'VOD LN', 'Vodafone', 23.36000061)

def __get_tuple3():
    return (123, 'VOD LN', 'Vodafone', 23.3600006009)

tup1 = __get_tuple1()
tup2 = __get_tuple2()
tup3 = __get_tuple3()

print('\n\nResults:')
print('Tuple1 = Tuple2: ' + str(tup1 == tup2))
print('Tuple1 = Tuple3: ' + str(tup1 == tup3))
print('Tuple3 = Tuple2: ' + str(tup3 == tup2))

print('Tuple1 {0} - {1}'.format(tup1[0], tup1[-1]))

print ('-------------------------------------')
