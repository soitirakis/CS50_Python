def main():
    greet = input("Greeting: ")
    print(value(greet))


def value(word):
    word = word.strip().lower()
    if word[0:5] == "hello":
        return 100
    elif word[0] == "h" and word[0:5] != "hello":
        return 20
    return 0


if __name__ == "__main__":
    main()
