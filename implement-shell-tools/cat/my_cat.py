import argparse
import glob
import sys

def main():
    parser = argparse.ArgumentParser(prog="cat", add_help=False)
    parser.add_argument("-n", action="store_true")
    parser.add_argument("-b", action="store_true")
    parser.add_argument("files", nargs="*")
    
    args = parser.parse_args()
    line_count = 1

    if not args.files:
        args.files = ["-"]

    file_list = []
    for pattern in args.files:
        expanded = glob.glob(pattern)
        if expanded:
            file_list.extend(expanded)
        else:
            file_list.append(pattern)

    for path in file_list:
        try:
            if path == "-":
                f = sys.stdin
            else:
                f = open(path, "r")

            for line in f:
                is_blank = not line.strip()
                
                if args.b:
                    if not is_blank:
                        print(f"{line_count:>6}\t{line}", end="")
                        line_count += 1
                    else:
                        print(line, end="")
                
                elif args.n:
                    print(f"{line_count:>6}\t{line}", end="")
                    line_count += 1
                
                else:
                    print(line, end="")

            if path != "-":
                f.close()

        except FileNotFoundError:
            print(f"cat: {path}: No such file or directory", file=sys.stderr)

if __name__ == "__main__":
    main()