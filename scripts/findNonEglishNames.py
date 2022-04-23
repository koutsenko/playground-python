import os


def find_wrong(path):
    wrong = []
    for root, dirs, files in os.walk(path):
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
    print(f"Found {len(wrong)} names:")
    for w in wrong:
        print(w)
    print("Done!")


if __name__ == "__main__":
    main()
