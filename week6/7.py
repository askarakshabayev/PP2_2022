import os


def print_space(level):
    for i in range(level):
        print('', end=' ')


def show_all_files(path, level):
    for target in os.listdir(path):
        target_path = os.path.join(path, target)
        if os.path.isfile(target_path):
            print_space(level)
            print(f'FILE: {target_path}')
        else:
            print_space(level)
            print(f'DIR: {target_path}')
            show_all_files(target_path, level + 1)


# BASE_URL = os.getcwd()
path = '/Users/askar/Documents/KBTU/PP2_2022'

show_all_files(path, 0)
# '.'
# '..'
