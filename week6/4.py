import os

# os.path.exists(path)
# os.remove(path)
# os.path.isdir(path)
# os.path.isfile(path)
# os.rmdir(path)  - delete empty folder

path = '/Users/askar/Documents/KBTU/PP2_2022/week6/input.txt'
path_dir = '/Users/askar/Documents/KBTU/PP2_2022/week6'
path_to_delete = '/Users/askar/Documents/KBTU/PP2_2022/week6/dir1'

os.rmdir(path_to_delete)

# if os.path.exists(path):
#     print("Yes")
# else:
#     print("No")

# if os.path.exists(path):
#     os.remove(path)

# if os.path.isdir(path_dir):
#     print('DIR')
# else:
#     print("File")

# if not os.path.isfile(path_dir):
#     print('DIR')
# else:
#     print("File")
