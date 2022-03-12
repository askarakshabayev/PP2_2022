import fnmatch
import os

BASE_URL = os.getcwd()

with os.scandir(BASE_URL) as items:
    for item in items:
        if item.is_file():
            if fnmatch.fnmatch(item.name, '*.py'):
                print(f'___________{item.name}_____________')
                file = open(item.name, 'r')
                content = file.read()
                print(content)
                file.close()
