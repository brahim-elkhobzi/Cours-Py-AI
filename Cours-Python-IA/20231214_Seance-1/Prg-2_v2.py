nombre = int(input("Saisir un nombre : "))

if (nombre % 4 == 0) :
    print(nombre, "est un multiple de 4")
elif (nombre % 2 == 0) :
    print(nombre, "est pair")
else :
    print(nombre, "est impair")