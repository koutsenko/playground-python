import os
from filter import is_filtered_dir, filter_dirs


def find_wrong(path):
    wrong = []
    for root, dirs, files in os.walk(path):
        if is_filtered_dir(root):
            continue
        dirs = filter_dirs(dirs)
        for file in files:
            if not file.isascii():
                wrong.append(os.path.join(root, file))
        for directory in dirs:
            if not directory.isascii():
                wrong.append(os.path.join(root, directory))
            wrong.extend(find_wrong(directory))
    return wrong


def main():
    wrong = find_wrong("D:\\notes\\")
    for w in wrong:
        print(w)
    print(f"Found {len(wrong)} names")


if __name__ == "__main__":
    main()
