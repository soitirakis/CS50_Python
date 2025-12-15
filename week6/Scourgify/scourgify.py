import sys
import csv

def main():
    n = len(sys.argv)
    if n == 3:
        file_to_read = sys.argv[1]
        file_to_write = sys.argv[2]
    elif n < 3:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")

    try:
        with open(file_to_read, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            people = []
            for row in reader:
                last, first = row['name'].split(",")
                first, last = first.strip(), last.strip()
                house = row['house']
                people.append({'first': first, "last": last, "house": house})
            #print(people)
        with open(file_to_write, "w", newline="") as csvfile:
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            writer.writeheader()
            for value in people:
                writer.writerow(value)

    except OSError:
        sys.exit(f"Could not read {file_to_read}")
    except ValueError as e:
        print(e)
    except AttributeError as e:
        print(e)

if __name__=="__main__":
    main()
