def convert(str):
    str = str.replace(":)", "🙂")
    str = str.replace(":(", "🙁")
    return str

def main():
    faces = convert(input("Text: "))
    print(faces)

main()
