def main():
    x, y = get_fraction()
    if x or y:
        result = convert(x, y)

    print(display(result))

def get_fraction():
    fraction = input("Fraction: ")
    while True:
        spl_word = '/'
        try:
            x = int(fraction.split(spl_word)[0])
            y = int(fraction.split(spl_word)[1])
            x / y
        except ValueError:
            fraction = input("Fraction: ")
        except ZeroDivisionError:
            fraction = input("Fraction: ")
        if x > y:
            fraction = input("Fraction: ")
        else:
            break
    return x, y

def convert(x,y):
    result = x / y
    if result <= 1 / 100:
        result = 'E'
    elif result >= 99 / 100:
        result = 'F'
    else:
        result *= 100
        result = round(result)
    return str(result)

def display(fraction):
    if fraction.isdigit():
        fraction += "%"
    return fraction

main()
