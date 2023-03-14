import os

def search_files(directory):
    files = []
    search_files_recursive(directory, files)
    return files

def search_files_recursive(directory, files):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            files.append(filepath)
        elif os.path.isdir(filepath):
            search_files_recursive(filepath, files)
