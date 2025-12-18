from datetime import date
import inflect
import sys
import re

def main():
    birth_day = input("Date of Birth: ")

    #validate the format using regx 
    matches = re.match(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", birth_day, flags = re.IGNORECASE)
    if matches:
        print(calculate(birth_day))
    else:
        sys.exit("Invalid date")

def calculate(datestr):
    year, month, day = datestr.split("-")
    year, month, day = int(year), int(month), int(day)

    today = date.today()

    my_birthday = date(year, month, day)
    my_age = today - my_birthday
    number_of_minutes = my_age.days * 24 * 60

    #converting numerals to words using inflect
    p = inflect.engine()
    words = p.number_to_words(number_of_minutes).capitalize() +  " minutes"
    words = words.replace("and ", "") #remove the "and " from the sentences
    return words


if __name__ == "__main__":
    main()
