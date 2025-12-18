import re
import sys

def main():
    print(count(input("Text: ")))

def count(text):
    match = re.findall(r"(?<![A-Za-z0-9])um(?![A-Za-z0-9])", text, re.IGNORECASE)
    counter = len(match)
    return counter

if __name__ == "__main__":
    main()
