import os


# os.listdir(path)
# os.path.join(path1, path2, path3)

BASE_URL = os.getcwd()

# print(os.listdir(BASE_URL))

for target in os.listdir('.'):
    # target_path = BASE_URL + '/' + target
    target_path = os.path.join(BASE_URL, target)
    if os.path.isfile(target_path):
        print(f'FILE: {target_path}')
    if os.path.isdir(target_path):
        print(f'DIR: {target_path}')
        for t in os.listdir(target_path):
            t_path = os.path.join(BASE_URL, target, t)
            if os.path.isfile(t_path):
                print(f'     File: {t_path}')
            else:
                print(f'     Dir: {t_path}')
