import sys
from PIL import Image, ImageOps

def main():
    n = len(sys.argv)
    suffixes = (".jpg", ".jpeg", ".png")

    if n == 3:
        file_to_open = sys.argv[1]
        file_to_save = sys.argv[2]

        if file_to_open.endswith(suffixes) and file_to_save.endswith(suffixes):
            pass
        else:
            sys.exit("Invalid input")

        if file_to_open.split(".")[1] == file_to_save.split(".")[1]:
            try:
                image = Image.open(file_to_open)
            except FileNotFoundError:
                sys.exit("Input does not exist")

            shirt = Image.open("shirt.png")
            size = shirt.size

            puppet = ImageOps.fit(image, size)
            puppet.paste(shirt, shirt)
            puppet.save(file_to_save)
        else:
            sys.exit("Input and ouput have different extensions")
            
    elif n < 3:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")

if __name__ == "__main__":
    main()
