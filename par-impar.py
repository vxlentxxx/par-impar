# Ejercicio N°4 Poder diferenciar si un numero es par o impar

# input

print("--------------------------------------")
X= int(input("Digite el vaalor de x: "))


# prosesing

r = X % 2
if r == 0:
    rta = "PAR"
    print("El Numer es Par")

else:
    rta = "IMPAR"
    print("El Numero es Impar")
print("---------------------------------------")
# output

print("----------------------------------------")
print("El numero" + str(X)+ "es" + rta)
print("---------------------------------------")
