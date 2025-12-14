from plates import is_valid

def test_is_valid_length():
    assert is_valid("CS50") == True
    assert is_valid("C")  == False
    assert is_valid("CS50XP2") == False
    assert is_valid("H") == False

def test_is_valid_first_letters():
    assert is_valid("CS20") == True
    assert is_valid("02CS") == False
    assert is_valid("C020") == False

def test_is_valid_special():
    assert is_valid("PI3.14") == False
    assert is_valid("PI3 14") == False

def test_is_valid_not_zero():
    assert is_valid("CS05") == False

def test_is_valid_number_placement():
    assert is_valid("AA222") == True
    assert is_valid("AA22A") == False

def test_is_valid_only_numbers():
    assert is_valid("50") == False

def test_is_valid_only_letters():
    assert is_valid("GOODBYE") == False

