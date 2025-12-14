#professor implementation
"""Little professor EEE = incorrest answer; """

import random

def main():
    level = get_level()
    generate_integer(level)

def get_level():
    '''Prompts user for a level n; 1, 2 or 3'''
    while True:
        try:
            n = int(input("Level: "))
            if n not in range(1,4):
                raise ValueError
            break
        except ValueError:
            continue
    return n
def generate_integer(level):
    '''Generate integer with n digits'''
    user_score = 0
    user_errors = 0

    for i in range(10):
        if level == 1:
            x = random.randint(0,9)
            y = random.randint(0,9)
        elif level == 2:
            x = random.randint(10,99)
            y = random.randint(10,99)
        elif level == 3:
            x = random.randint(100,999)
            y = random.randint(100,999)

        while True:
            try:
                result = x + y
                user_result = int(input(f"{x} + {y} = "))
                if user_result == result:
                    user_score += 1
                    break
                elif user_result != result:
                    user_errors += 1
                    print("EEE")
                if user_errors == 3:
                    print(f"{x} + {y} = {result}")
                    break
            except ValueError:
                continue

    print(f"Score: {user_score}")
if __name__ == "__main__":
    main()
