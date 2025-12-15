import pytest
from lines import main
import sys
import os

def main():
    pass

#define a helper to run main script
def run_script(args):
    sys.argv = args
    try:
        output = []
        _stdout = sys.stdout
        sys.stdout = open("output.txt", "w")

        main()

        sys.stdout.close()
        sys.stdout = _stdout
        with open("output.txt", "r") as file:
            output = file.read().strip()
        os.remove("output.txt")

        return output
    except SystemExit as e:
        return str(e)

def test_no_argumets():
    '''Test case for no arguments'''
    result = run_script(['your_script_name.py'])
    assert result == "Too few command-line arguments"

def test_too_many_arguments():
    '''Test case too many arguments'''
    result = run_script(['your_script_name.py', 'file1.py', 'file2.py'])
    assert result == "Too many command-line arguments"

if __name__=="__main__":
    main()
