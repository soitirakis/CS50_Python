##vanity plates
##max 6 char, min 2 char; must start with 2 letters; numbers only at the end; no periods, spaces, punctation; first number not 0

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print('Valid')
    else:
        print('Invalid')

def is_valid(string):
    length_string = len(string)
    valid = True

    #Check char between 2 and 6
    if length_string < 2 or length_string > 6:
        valid = False

    #Check first 2 characters to be letters
    if not string[0:2].isalpha():
        valid = False

    #Check no punctation, space, periods
    symbol = ['.', ',', ' ']
    for char in string:
        if char in symbol:
            valid = False

    #Check for numbers
    #if string is alphanumeric; for first digit, all the next ones need to be digit
    if string.isalnum():
        for i in range(len(string)):
            if string[i].isdigit():
                if not string[i:].isdigit():
                    valid = False
                    break

    #check for 0 not first number
    for char in string:
        if char.isdigit():
            index = string.index(char)
            partial_string = string[:index]
            if partial_string.isalpha() and char == '0':
                valid = False
                break

    return valid

if __name__ == '__main__':
    main()
