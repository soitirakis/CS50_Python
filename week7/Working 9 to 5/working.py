import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):

    #regex to check the proper format, and to ignore case
    #one or two values, AM/PM \, devided by ":" or not
    if match := re.search(r"([0-9]{0,2}:?[0-9]{0,2}\s?(AM|PM))\sto\s?([0-9]{0,2}:?[0-9]{0,2}\s?(AM|PM))", s, re.IGNORECASE):
        opening_hour = match.group(1).split(" ")
        closing_hour = match.group(3).split(" ")
        working_hours = [opening_hour, closing_hour]
    else:
        raise ValueError

    converted_time = []

    #creates a list with the time to convert

    for time in working_hours:
        if ":" in time[0]:
            hours, minutes = time[0].split(":")
            if int(minutes) >= 60:
                raise ValueError
        else:
            hours = time[0]
            minutes = "00"
        if int(hours) == 12:
            hours = "00"
        elif int(hours) < 10:
            hours = "0" + hours
        if time[1].lower() == "am":
            opening_time = hours + ":" + minutes
        else:
            hours = int(hours) + 12
            opening_time = str(hours) + ":" + minutes
        converted_time.append(opening_time)
    return converted_time[0] + " to " + converted_time[1]



if __name__=="__main__":
        main()
