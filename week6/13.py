# os.scandir
import os


def show_files_and_dirs(dir_path: str):
    with os.scandir(dir_path) as scan:
        for entry in scan:
            if entry.is_dir():
                print(entry.name)


show_files_and_dirs(os.getcwd())
