import pytest
from seasons import calculate

def test_calculate():
    assert calculate("1992-12-04") == "Sixteen million, eight hundred eighty-eight thousand, three hundred twenty minutes"

    with pytest.raises(SystemExit, match="Invalid date"):
        calculate("January 1, 1999")
