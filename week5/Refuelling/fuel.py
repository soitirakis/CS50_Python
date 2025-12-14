def main():
    fuel = get_fraction()
    result = convert(fuel)

    print(gauge(result))

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
    return fraction

def convert(fraction):
    spl_word = "/"
    x = int(fraction.split(spl_word)[0])
    y = int(fraction.split(spl_word)[1])
    result = x / y * 100
    return result

def gauge(result):
    if result <= 1:
        result = 'E'
    elif result >= 99:
        result = 'F'
    else:
        result = str(round(result))
    if result.isdigit():
        result += "%"
    return result

main()
