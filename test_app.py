import pytest
from app import divide

def test_divide_normal():
    assert divide(10, 2) == 5

def test_divide_negative():
    assert divide(-10, 2) == -5

def test_divide_float():
    assert divide(5, 2) == 2.5
