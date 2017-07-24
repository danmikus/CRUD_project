import sys
import os

sys.path.append(os.path.join('..', 'app'))

from products_app import *

def test_price_1():
    test1 = check_price("3.0")
    assert test1 == False

def test_price_3():
    test1 = check_price("3.00")
    assert test1 == False

def test_price_5():
    test1 = check_price("3.2")
    assert test1 == True

def test_price_6():
    test1 = check_price("3.222")
    assert test1 == True
