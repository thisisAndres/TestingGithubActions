import pytest
from lab2 import contar_vocales

def test_contar_vocales():
    assert contar_vocales("hola") == 2
    assert contar_vocales("mundo") == 2
    assert contar_vocales("") == 0
    assert contar_vocales("a") == 1
    assert contar_vocales("aeiou") == 5
    assert contar_vocales("bcdfghjklmnpqrstvwxyz") == 0
    assert contar_vocales("AEIOU") == 5
    assert contar_vocales("Python") == 1
    assert contar_vocales("Vocales") == 3
    assert contar_vocales("vOcAlEs") == 3