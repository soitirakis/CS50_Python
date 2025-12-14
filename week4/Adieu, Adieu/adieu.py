#adieu program

def main():
    names = []

    while True:
        try:
            name = input("Name: ")
        except EOFError:
            print()
            print(display(names))
            exit()
        names.append(name)

def display(names):
    n = len(names)
    phrase = "Adieu, adieu, to"
    if n == 1:
        return f"{phrase} {names[0]}"
    elif n == 2:
        return f"{phrase} {names[0]} and {names[1]}"
    else:
        last_name = names.pop(-1)
        result = ", ".join(names)
        result += ","
        #print(result)
        return f"{phrase} {result} and {last_name}"

main()
