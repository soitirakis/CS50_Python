##twitter
##omite all vowels

def main():
    user_string = input('Input: ')
    print(f'Output: {twitter(user_string)}')

def twitter(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    new_string = ''
    for char in string:
        if char in vowels:
            continue
        else:
            new_string += char

    return new_string


if __name__ == '__main__':
    main()
