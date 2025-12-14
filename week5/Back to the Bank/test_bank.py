from bank import value


def main():
    test_bank()


def test_bank():
    assert value("hello") == 0
    assert value("Hello, Newman") == 0


def test_bank_20():
    assert value("How you doing?") == 20
    assert value("Hi, hello") == 20


def test_bank_100():
    assert value("What's happening?") == 100
    assert value("What's up?") == 100


if __name__ == "__main__":
    main()
