find the frequencies of all the characters in that string and return a dictionary with key as the character and its value as its frequency in the given string


r={i:s.count(i)-1 for i in set(s)}
print(r)




from collections import Counter
res = Counter(s)
r = dict(map(lambda x: (x, res[x] - 1), res))
print(r)


#UNIT TEST CASE

import pytest

def f(s):
    r = {}
    for i in s:
         if i in r:

             r[i] += 1
         else:
             r[i] = 0

    return r
print(f("akshara"))

@pytest.mark.parametrize("s, output",[("akshara",{'a': 3, 'k': 0, 's': 0, 'h': 0, 'r': 0})])
def test_multiplication_11(s, output):
    r=f("akshara")
    assert r==output
