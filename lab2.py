import pytest

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def invertir_cadena(cadena):
    return cadena[::-1]

def mcd(a, b):
    while b:
        a, b = b, a % b
    return a

def es_palidromo(cadena: str):
    cadena = cadena.replace(" ", "").lower()
    return cadena == cadena[::-1]

def contar_vocales(cadena):
    contador = 0
    
    for char in cadena.lower():
        if char in 'aeiou':
            contador += 1
    
    return contador

def suma_pares(lista):
    return sum(num for num in lista if num % 2 == 0)