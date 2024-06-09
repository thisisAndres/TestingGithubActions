import pytest
from lab2 import mcd

def test_mcd():
    assert mcd(48, 18) == 6
    assert mcd(20, 8) == 4
    assert mcd(100, 25) == 25
    assert mcd(7, 3) == 1
    assert mcd(14, 7) == 7
    assert mcd(0, 5) == 5
    assert mcd(5, 0) == 5
    assert mcd(1, 1) == 1
    assert mcd(21, 14) == 7
    assert mcd(1071, 462) == 21