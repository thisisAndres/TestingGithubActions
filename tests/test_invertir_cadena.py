import pytest
from lab2 import invertir_cadena

def test_invertir_cadena():
    assert invertir_cadena("hola") == "aloh"
    assert invertir_cadena("mundo") == "odnum"
    assert invertir_cadena("") == ""
    assert invertir_cadena("a") == "a"
    assert invertir_cadena("radar") == "radar"
    assert invertir_cadena("level") == "level"
    assert invertir_cadena("Python") == "nohtyP"
    assert invertir_cadena("12345") == "54321"
    assert invertir_cadena("abc def") == "fed cba"
    assert invertir_cadena("palindrome") == "emordnilap"