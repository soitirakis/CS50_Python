# bitcoin problem week4
"""buy bitcoins"""

import requests
import sys
import json

valute = {"USD": "$", "EUR": "€", "GBP": "£"}


def main():

    while True:
        """'try-except to check no of args; type of arg float"""
        try:
            if len(sys.argv) == 3:
                currency_code = sys.argv[2].upper()
                if currency_code not in valute:
                    raise ValueError(f"Unsupported currency: {currency_code}") # using secong arg to set valute type: USD, EUR, GBP

                n = float(sys.argv[1])
                value = round(convert_value(n, currency_code), 4)
                print(f"{value:,}")
                break
            else:
                raise IndexError
        except IndexError:
            sys.exit("Missing command-line argument")
        except ValueError:
            sys.exit("Command-line argument is not a number")


def convert_value(n):
    """Get the exchange rate for the specified currency and return the value"""
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        exchange_rate = float(data["bpi"]["USD"]["rate_float"])
        return n * exchange_rate
    except requests.RequestException:
        sys.exit("Error: unable to fetch data from API")
    except KeyError:
        sys.exit("Error: Currency {currency_code} not found in API")

if __name__ == "__main__":
    main()
