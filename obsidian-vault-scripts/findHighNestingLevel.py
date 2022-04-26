import os
from filter import is_filtered_dir, filter_dirs

max_nesting_level = 4


def find_wrong(path):
    wrong = []
    for root, dirs, files in os.walk(path):
        if is_filtered_dir(root):
            continue
        dirs = filter_dirs(dirs)
        rel_path = os.path.relpath(root, path)
        if len(rel_path.split(os.sep)) > max_nesting_level:
            wrong.append(rel_path)
        for directory in dirs:
            wrong.extend(find_wrong(directory))
    return wrong


def main():
    wrong = find_wrong("D:\\notes\\")
    for w in wrong:
        print(w)
    print(f"Found {len(wrong)} paths")


if __name__ == "__main__":
    main()
