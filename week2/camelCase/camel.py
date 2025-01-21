##snake_case

def main():
    name = input("Name: ")
    snake_case = ""
    for x in name:
        if x.islower():
            snake_case += x
        elif x.isupper():
            snake_case += "_"
            snake_case += x.lower()
    print(snake_case)

main()
