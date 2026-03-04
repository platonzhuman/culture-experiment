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

def test_addition_duplicated():
    #it is real good test 
    assert add(2, 3) == 2 + 3

def test_addition_overcomplicated():
    # formally valid test but too slow
    for i in range(0, 2**32):
        for j in range(0, 2**32):
            assert add(i, j) == sum([i, j]) #might dublicate principles
            assert add(-i, j) == sum([-i, j])
            assert add(i, -j) == sum([i, -j])
            assert add(-i, -j) == sum([-i, -j])




if __name__=="__main__":
    test_addition()
    test_addition_with_bug()
    test_addition_duplicated()
    # test_addition_overcomplicated()