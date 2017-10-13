import os

print ('-------------------------------------')
print ('Comparing CANS outputs\n\n')
new_file_path = 'E:\\temp\\Temp\\cans\\compare\\new'
old_file_path = 'E:\\temp\\Temp\\cans\\compare\\old'


def __get_files_in_folder(path_to_check):
    file_list = [os.path.join(path_to_check, f) for f in os.listdir(path_to_check)]
    return file_list

#old_files = [os.path.join(old_file_path, f) for f in os.listdir(old_file_path)]
#old_files.reverse()

old_files = __get_files_in_folder(old_file_path)
for file in old_files:
    print(file)

new_files = __get_files_in_folder(new_file_path)
for file in new_files:
    print(file)