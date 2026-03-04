import sys
sys.path.append("../src")
#TODO marke if with pip install -e
from math_demo import add

def test_addition():
    assert add(2, 2) == 4
    print("test basic addition")

if __name__=="__main__":
    test_addition()