import os

def search_files_recursive(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            print(filepath)
        elif os.path.isdir(filepath):
            search_files_recursive(filepath)

