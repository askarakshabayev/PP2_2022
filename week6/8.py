# os.walk
import os

BASE_URL = os.getcwd()

# print(os.walk(BASE_URL))

for root, dirs, files in os.walk(BASE_URL):
    print(root)
    print("ALL DIRECTORIES:")
    for dir in dirs:
        print(dir)
    print('ALL FILES:')
    for file in files:
        print(file)


