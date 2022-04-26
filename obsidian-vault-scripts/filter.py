import os

excluded_dirs = ['.git', '.obsidian']


def is_filtered_dir(directory):
    parts = directory.split(os.sep)
    result = False
    for part in parts:
        if part in excluded_dirs:
            result = True
            break
    return result


def filter_dirs(dirs):
    result = []
    for directory in dirs:
        if directory not in excluded_dirs:
            result.append(directory)
    return result
