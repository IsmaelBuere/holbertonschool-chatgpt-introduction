#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n = n - 1
    return result

if len(sys.argv) != 2:
    print("Uso: {} <numero>".format(sys.argv[0]))
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("El argumento debe ser un numero entero.")
    sys.exit(1)

if n < 0:
    print("El número debe ser no negativo.")
    sys.exit(1)

f = factorial(int(sys.argv[1]))
print(f)