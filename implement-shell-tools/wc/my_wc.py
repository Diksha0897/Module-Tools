import sys
import glob

def count_file(path):
    with open(path, "rb") as f:
        data = f.read()

    text = data.decode(errors="ignore")

    lines = text.count("\n")
    words = len(text.split())
    bytes_count = len(data)

    return lines, words, bytes_count


def print_counts(lines, words, bytes_count, path, flags):
    parts = []

    if flags["l"]:
        parts.append(str(lines))
    elif flags["w"]:
        parts.append(str(words))
    elif flags["c"]:
        parts.append(str(bytes_count))
    else:
        parts.extend([str(lines), str(words), str(bytes_count)])

    parts.append(path)
    print("\t".join(parts))


def main():
    args = sys.argv[1:]

    flags = {"l": False, "w": False, "c": False}
    files = []

    for arg in args:
        if arg == "-l":
            flags["l"] = True
        elif arg == "-w":
            flags["w"] = True
        elif arg == "-c":
            flags["c"] = True
        else:
            expanded = glob.glob(arg)
            files.extend(expanded if expanded else [arg])

    if not files:
        files = []

    total_l = total_w = total_c = 0

    for file in files:
        try:
            lines, words, bytes_count = count_file(file)

            total_l += lines
            total_w += words
            total_c += bytes_count

            print_counts(lines, words, bytes_count, file, flags)

        except FileNotFoundError:
            print(f"wc: {file}: No such file or directory", file=sys.stderr)

    if len(files) > 1:
        print_counts(total_l, total_w, total_c, "total", flags)


if __name__ == "__main__":
    main()