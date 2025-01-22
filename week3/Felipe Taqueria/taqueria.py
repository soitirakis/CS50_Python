#taqueria restaurant

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    total_amount = 0
    while True:
        try:
            menu_item = input('Item: ')
            total_amount +=  menu[menu_item.title()]
        except KeyError:
            menu_item = input('Item: ')
        except EOFError:
            print()
            exit()
        except KeyboardInterrupt:
            exit()
        else:
            total = format(total_amount, ".2f")
            print(f"Total: ${total}")

main()
