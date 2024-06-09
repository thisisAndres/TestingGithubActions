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

def maximo(lista):
    if not lista:
        return None
    
    max_val = lista[0]
    for num in lista:
        if num > max_val:
            max_val = num
        
    return max_val

def contar_vocales(cadena):
    contador = 0
    
    for char in cadena.lower():
        if char in 'aeiou':
            contador += 1
    
    return contador