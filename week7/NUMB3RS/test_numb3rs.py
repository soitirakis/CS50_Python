from numb3rs import validate

def test_validate():
    #Validation which cause a Fault
    assert validate(r"275.3.6.28") == False
    assert validate(r"10.10.999.10") == False
    assert validate(r"10.999.10.10") == False
    assert validate(r"512.512.512.512") == False
    assert validate(r"1.2.3.1000") == False
    assert validate(r"cat") == False

    #Successful validation
    assert validate(r"127.0.0.1") == True
    assert validate(r"1.2.3.4") == True
    assert validate(r"255.255.255.255") == True
