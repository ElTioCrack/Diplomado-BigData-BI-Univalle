import sys

print("Hola. Yo soy un programa en Python")

try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = a + b
    print(f"La suma de {a} y {b} es {c}")
except IndexError:
    print("Error: Faltan argumentos")
    print("Uso: python script.py <numero1> <numero2>")
except ValueError:
    print("Error: Los argumentos deben ser numeros enteros")
    print("Uso: python script.py <numero1> <numero2>")
