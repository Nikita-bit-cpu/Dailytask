# tools.py

import os

def empty_folder(folder_path):
    # Delete all files and subdirectories in the given folder path
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            os.remove(file_path)
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            os.rmdir(dir_path)

def list_dir(folder_path):
    # List all files in the given folder path
    files = os.listdir(folder_path)
    return files