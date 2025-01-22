##list of groceries
def main():

    grocery_list = []
    while True:
        try:
            grocery_item = input()
        except EOFError:
            print()
            display(grocery_list)
            exit()
        else:
            grocery_item = grocery_item.upper()
            grocery_list.append(grocery_item)

def display(list_of_items):
    list_of_items.sort()
    counter = 0
    new_list = {}
    for i in range(len(list_of_items)):
        counter = list_of_items.count(list_of_items[i])
        try:
            new_list[list_of_items[i]] = counter
        except KeyError:
            print("error")
    #print(new_list)
    for k, v in new_list.items():
        print(v, k)

main()
