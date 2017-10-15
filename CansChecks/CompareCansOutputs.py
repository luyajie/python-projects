#!/usr/bin/python3.5

import os
import re


print ('-------------------------------------')
print ('Comparing CANS outputs\n\n')

#new_file_path = 'E:\\temp\\Temp\\cans\\compare\\new'
#old_file_path = 'E:\\temp\\Temp\\cans\\compare\\old'

new_file_path = os.path.expanduser('~/Documents/data/compare/new')
old_file_path = os.path.expanduser('~/Documents/data/compare/old')
results_file_path = os.path.expanduser('~/Documents/data/compare/results.txt')
old_results_file_path = os.path.expanduser('~/Documents/data/compare/old_results.txt')
new_results_file_path = os.path.expanduser('~/Documents/data/compare/new_results.txt')


def __get_files_in_folder(path_to_check):
    file_list = [os.path.join(path_to_check, f) for f in os.listdir(path_to_check)]
    file_list.sort()
    return file_list

def __print_list(user_list):
    for item in user_list:
        print(item)

def __get_tuple(line):
    searchObj = re.search(r'.* Sending Dividends to both G2 db and dividend management webservice. Ticker: (.*), ActionId: (\d+), Flag: (.*), CompanyName: (.*), EffectiveDate: (.*), GrossAmount: (.*), NetAmount: (.*), PaidCurrency:(.*), ExchangeCode: (.*).*', line, re.M | re.I)
    if searchObj:
        #print('searchObj.group() : ', searchObj.group())
        ticker = searchObj.group(1)
        actionId = searchObj.group(2)
        flag = searchObj.group(3)
        companyName = searchObj.group(4)
        effectiveDate = searchObj.group(5)
        grossAmount = searchObj.group(6)
        netAmount = searchObj.group(7)
        paidCurrency = searchObj.group(8)
        exchangeCode = searchObj.group(9)
    else:
        ticker = ''
        actionId = ''
        flag = ''
        companyName = ''
        effectiveDate = ''
        grossAmount = ''
        netAmount = ''
        paidCurrency = ''
        exchangeCode = ''

    return (actionId, ticker, flag, companyName, effectiveDate, grossAmount, netAmount, paidCurrency, exchangeCode)

def __get_list(line):
    (actionId, ticker, flag, companyName, effectiveDate, grossAmount, netAmount, paidCurrency, exchangeCode) = __get_tuple(line)
    return [actionId, ticker, flag, companyName, effectiveDate, grossAmount, netAmount, paidCurrency, exchangeCode]


def __is_matched(tuple1, tuple2):
    if (tuple1 == tuple2) or (tuple1[0] == tuple2[0]):
        return True
    return False


def __get_formatted(tuple1, tuple2):
    if (tuple1 is not None) and (tuple2 is not None):
        return "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15},{16},{17}".format(tuple1[0], tuple1[1], tuple1[2], tuple1[3], tuple1[4], tuple1[5], tuple1[6], tuple1[7], tuple1[8],tuple2[0], tuple2[1], tuple2[2], tuple2[3], tuple2[4], tuple2[5], tuple2[6], tuple2[7], tuple2[8])

    if tuple1 is None:
        return ",,,,,,,,,{0},{1},{2},{3},{4},{5},{6},{7},{8}".format(tuple2[0], tuple2[1], tuple2[2], tuple2[3], tuple2[4], tuple2[5], tuple2[6], tuple2[7], tuple2[8])

    return "{0},{1},{2},{3},{4},{5},{6},{7},{8},,,,,,,,,".format(tuple1[0], tuple1[1], tuple1[2], tuple1[3], tuple1[4], tuple1[5], tuple1[6], tuple1[7], tuple1[8])


new_files = __get_files_in_folder(new_file_path)
#__print_list(new_files)

# read new file to get list of processed actionIds
divis_new_list = []
for file_path in new_files:
    file_reader = open(file_path, 'r')
    for line in file_reader:
        if line.__contains__('Sending Dividends to both G2 db and dividend management webservice'):
            tmp_tuple = __get_tuple(line)
            divis_new_list.append(tmp_tuple)




old_files = __get_files_in_folder(old_file_path)
#__print_list(old_files)

# read old files to get list of processed actionIds
divis_old_list = []
for file_path in old_files:
    file_reader = open(file_path, 'r')
    for line in file_reader:
        if line.__contains__('Sending Dividends to both G2 db and dividend management webservice'):
            tmp_tuple = __get_tuple(line)
            divis_old_list.append(tmp_tuple)



# now compare the two lists to find the differences
matched_list = []
unmatched_old_list = []
unmatched_new_list = []

old_list_len = len(divis_old_list)
new_list_len = len(divis_new_list)

old_running_index = 0
new_running_index = 0

# compare both lists
while old_running_index < old_list_len:
    while new_running_index < new_list_len:
        if divis_old_list[old_running_index] is not None and divis_new_list[new_running_index] is not None:
            if __is_matched(divis_old_list[old_running_index], divis_new_list[new_running_index]):
                matched_list.append(__get_formatted(divis_old_list[old_running_index], divis_new_list[new_running_index]))
                divis_old_list[old_running_index] = None
                divis_new_list[new_running_index] = None
                new_running_index = 0
            else:
                new_running_index = new_running_index + 1
        else:
            new_running_index = new_running_index + 1
    new_running_index = 0
    old_running_index = old_running_index + 1

# now list out old list
old_running_index = 0
while old_running_index < old_list_len:
    if divis_old_list[old_running_index] is not None:
        unmatched_old_list.append(__get_formatted(divis_old_list[old_running_index], None))
    old_running_index = old_running_index + 1


# now list out new list
new_running_index = 0
while new_running_index < new_list_len:
    if divis_new_list[new_running_index] is not None:
        unmatched_new_list.append(__get_formatted(None, divis_new_list[new_running_index]))
    new_running_index = new_running_index + 1


print('\n\nSummary')
print('Old service #: ' + str(len(divis_old_list)))
print('New service #: ' + str(len(divis_new_list)))
print('Matched #: ' + str(len(matched_list)))
print('Unmatched Old #: ' + str(len(unmatched_old_list)))
print('Unmatched New #: ' + str(len(unmatched_new_list)))


print('\n\nMatched')
__print_list(matched_list)

print('\n\nUnmatched Old')
__print_list(unmatched_old_list)

print('\n\nUnmatched New')
__print_list(unmatched_new_list)


print ('-------------------------------------')
