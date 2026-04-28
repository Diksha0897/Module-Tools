import os
import sys

def list_dir(path=".", show_all=False):
    try:
        items = os.listdir(path)
    except FileNotFoundError:
        print(f"ls: cannot access '{path}': No such file or directory")
        return

    if not show_all:
        items = [item for item in items if not item.startswith(".")]

    items.sort()

    for item in items:
        print(item)


def main():
    args = sys.argv[1:]

    show_all = False
    paths = []

    for arg in args:
        if arg == "-a":
            show_all = True
        elif arg == "-1":
            pass
        else:
            paths.append(arg)

    if not paths:
        paths = ["."]

    for i, path in enumerate(paths):
        if len(paths) > 1:
            print(f"{path}:")

        list_dir(path, show_all)

        if i != len(paths) - 1:
            print()

if __name__ == "__main__":
    main()