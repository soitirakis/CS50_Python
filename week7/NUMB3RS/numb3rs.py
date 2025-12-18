import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    #match = re.match(r"^([0-9]{1,3}\.){3}[0-9]{1,3}$", ip, re.IGNORECASE)
    match = re.match(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)
    #results = []
    if match:
        for i in range(1,5):
            if int(match.group(i)) > 255 or int(match.group(i)) < 0:
                return False
        return True
    else:
        return False



    '''if not match:
        return False

    numbers = ip.split(".")

    for num in numbers:
        if not (0 <= int(num) <= 255):
            return False
        if len(num) > 1 and num[0] == "0":
            return False

    return True'''


if __name__=="__main__":
    main()
