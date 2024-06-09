import pytest
from lab2 import suma_pares

def test_suma_pares():
    assert suma_pares([1, 2, 3, 4, 5]) == 6
    assert suma_pares([0, 2, 4, 6, 8]) == 20
    assert suma_pares([1, 3, 5, 7, 9]) == 0
    assert suma_pares([]) == 0
    assert suma_pares([-2, -4, -6]) == -12
    assert suma_pares([2]) == 2
    assert suma_pares([1, 2, 3, 4, 5, 6]) == 12
    assert suma_pares([10, 15, 20, 25, 30]) == 60
    assert suma_pares([1, 1, 1, 1, 1]) == 0
    assert suma_pares([2, 2, 2, 2, 2]) == 10
