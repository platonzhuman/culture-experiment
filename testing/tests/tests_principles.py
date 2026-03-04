import sys
sys.path.append("../src")
#TODO marke if with pip install -e
from math_demo import (
    add,
    add_with_bug
)



def test_addition():
    assert add(2, 2) == 4
    print("test basic addition")

def test_addition_with_bug():
    assert add_with_bug(2, 2) == 4
    assert add_with_bug(0, 0) == 0
    print("test bugged addition passed good")
    #assert add_with_bug(6, 7) == 13 with fail here




if __name__=="__main__":
    test_addition()
    test_addition_with_bug()