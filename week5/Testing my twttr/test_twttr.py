#twttr code tests
from twttr import shorten

def test_twttr():
    try:
        assert shorten("twitter") == "twttr"
        assert shorten("TWITTER") == "TWTTR"
        assert shorten("What's your name?") == "Wht's yr nm?"
        assert shorten("CS50") == "CS50"
    except AssertionError as e:
        print(f"Assert: {e}")
