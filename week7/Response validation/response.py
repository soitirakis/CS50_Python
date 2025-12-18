from validator_collection import validators, checkers, errors

def main():
    print(validate(input("Email: ")))

def validate(email):
    value = "Valid"
    try:
        email_address = validators.email(email, allow_empty = False)
    except errors.EmptyValueError:
        value = "Invalid"
    except errors.InvalidEmailError:
        value = "Invalid"
    return value

if __name__ == "__main__":
    main()
