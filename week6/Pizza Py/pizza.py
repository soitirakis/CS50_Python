import csv
import sys
from tabulate import tabulate

def main():
    n = len(sys.argv)
    if n == 2:
        file_path = sys.argv[1]
        if file_path.endswith(".csv"):
            pass
        else:
            sys.exit("Not a CSV file")
    elif n < 2:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")

    try:
        with open(file_path, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            lines = []
            for row in reader:
                lines.append(row)
            print(tabulate(lines, headers="keys", tablefmt="grid"))
    except OSError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
