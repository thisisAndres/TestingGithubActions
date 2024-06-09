import pytest
from lab2 import maximo

def test_maximo():
    assert maximo([1, 2, 3, 4, 5]) == 5
    assert maximo([5, 4, 3, 2, 1]) == 5
    assert maximo([1, 3, 2, 5, 4]) == 5
    assert maximo([-1, -2, -3, -4, -5]) == -1
    assert maximo([1]) == 1
    assert maximo([]) == None
    assert maximo([3, 3, 3]) == 3
    assert maximo([1, 2, 3, 3]) == 3
    assert maximo([3, 2, 1, 3]) == 3
    assert maximo([7, 5, 9, 2, 8]) == 9
