def main():
    greet = input("Greeting: ")
    print(greeting(greet))

def greeting(word):
    word = word.strip().lower()
    if word[0:5] == "hello":
        return "$0"
    elif word[0] == "h" and word[0:5] != "hello":
        return "$20"
    return "$100"

main()
