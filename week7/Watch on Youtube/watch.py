import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    match = re.search(r"^.+src=.+/embed/([a-zA-Z0-9]+[^\"])", s, re.IGNORECASE)
    prefix = "https://youtu.be/"
    if match:
        match = match.group(1)
        prefix += match
        return prefix

if __name__=="__main__":
    main()
