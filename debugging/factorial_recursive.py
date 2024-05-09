#!/usr/bin/python3
import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if len(sys.argv) != 2:
    print("Uso: {} <número>".format(sys.argv[0]))
    sys.exit(1)

try:
    number = int(sys.argv[1])
except ValueError:
    print("El argumento debe ser un número entero.")
    sys.exit(1)

result = factorial(number)
print(result)
