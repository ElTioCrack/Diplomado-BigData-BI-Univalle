import sys
#sys.argv contiene una lista de los argumentos pasados
numargs = len(sys.argv)
if numargs != 3:
    print("Usage: ", sys.argv[0] , "<num1> <num2>")  #ou sys.stderr.write("message")
    exit(1)  #Cualquier código de salida diferente de zero significa que o programa de erro
else:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = a+b
    print(f"La suma de {a} y {b} es {c}")
