import sys

lines = []

def main():
    n = len(sys.argv)
    try:
        if n == 2:
            file_path = sys.argv[1]
            if file_path.endswith(".py"):
                pass
            else:
                sys.exit("Not a Python file")
        elif len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        else:
            sys.exit("Too many command-line arguments")
        with open(file_path, "r") as file:
            row = file.readlines()
    except OSError:
        sys.exit("File does not exist")

    for line in row:
        line = line.strip()
        if line == '' or line[0:1] == "#":
            continue
        else:
            lines.append(line)
    #print(lines)
    print(len(lines))
if __name__ == "__main__":
    main()
