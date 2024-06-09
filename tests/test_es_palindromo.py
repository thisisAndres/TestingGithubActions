import pytest
from lab2 import es_palidromo

def test_es_palidromo():
    assert es_palidromo("anilina")
    assert es_palidromo("A man a plan a canal Panama")
    assert not es_palidromo("palindrome")
    assert es_palidromo("No lemon no melon")
    assert not es_palidromo("hello")
    assert es_palidromo("racecar")
    assert es_palidromo("madam")
    assert es_palidromo("Was it a car or a cat I saw")
    assert not es_palidromo("python")
    assert es_palidromo("")