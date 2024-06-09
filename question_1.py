This function effectively reads the contents of a file specified by its filename. It uses a try-except block to handle file opening errors.
#approach 2
#improved code
def get_contents(fname):
    try:
        with open(fname) as f:
            return f.read()
    except FileNotFoundError:
        return None


#UNIT test
def get_contents(fname):
    try:
        f = open(fname).read()
        return f
    except FileNotFoundError:
        return None

import pytest
@pytest.mark.parametrize("fname, output",[("./aksharaa.txt",None),("./akshara.txt",['h', 'a', 'i', ' ', 'w', 'o', 'r', 'l', 'd', '\n', 'w', 'e', 'l', 'c', 'o', 'm', 'e', '\n'])])
def test_multiplication_11(fname, output):
    r = get_contents(fname)
    if r!=None:
        r=list(r)
    assert r==output or r== None
