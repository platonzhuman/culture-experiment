import sys
sys.path.append("../src")
#TODO marke if with pip install -e
from math_demo import (
    add,
    add_with_bug,
    calculate_tax_with_bug,
    calculate_tax
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

def test_addition_reasonable():
    assert add(2,2) == 4
    assert add(0, 0) == 0
    assert add(6, 7) == 13
    assert add(-6, -7) == -13
    assert add(6, -7) == -1
    assert add(-7, 0) == -7
    assert add(7, 0) == 7
    print("ADDITION_REASONABLE_PASS")

def test_addition_communicative():
    assert add(7, -6) == 1
    assert add(-6, 7) == 1
    print("test_addition_communicative")

def test_tax_calculation_pesticised():
    assert calculate_tax_with_bug(1000) == 150.0
    assert calculate_tax_with_bug(100) == 15.0
    assert calculate_tax_with_bug(10) == 1.5
    assert calculate_tax_with_bug(1) == 0.15
    assert calculate_tax_with_bug(245) == 36.75
    assert calculate_tax_with_bug(-200) == -30
    assert calculate_tax_with_bug(0) ==  0
    print("test_addition_calculate pesticised")

    #assert calculate_tax_with_bug(24.5) ==  3.67 #3.675
def test_tax_calculation():
    assert calculate_tax_with_bug(1000) == 150.0
    assert calculate_tax_with_bug(100) == 15.0
    assert calculate_tax_with_bug(10) == 1.5
    assert calculate_tax_with_bug(1) == 0.15
    assert calculate_tax_with_bug(245) == 36.75
    assert calculate_tax_with_bug(-200) == -30
    assert calculate_tax_with_bug(0) ==  0
    print("test_addition_calculate")

if __name__=="__main__":
    test_addition()
    test_addition_with_bug()
    test_addition_duplicated()
    # test_addition_overcomplicated()
    test_addition_reasonable()
    test_addition_communicative()
    test_tax_calculation_pesticised()
    test_tax_calculation()
