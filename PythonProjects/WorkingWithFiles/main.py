import os
import shutil
file_path = 'my path'

def list_everything(path):
    for folder, sub_folders, files in os.walk(file_path):
        print(f"you are currently looking at {folder}")
        print('\n')
        print("the subfolders are: ")
        for sub_fold in sub_folders:
            print(f"\t subfolder: {sub_fold}")

        print('\n')
        print("the files are: ")
        for f in files:
            print(f"\t File: {f}")
        print('\n')


list_everything(file_path)
