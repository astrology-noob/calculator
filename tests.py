import pytest
from calculator import Сalculator

cal = Сalculator()

def test_addition():
    assert cal.add(4, 5) == 9

def test_subtraction():
    assert cal.subtract(4, 5) == -1

def test_multiplication():
    assert cal.multiply(4, 5) == 20

def test_division():
    assert cal.divide(4, 5) == 0.8

def test_raising_to_power():
    assert cal.raise_to_power(4, 5) == 1024




