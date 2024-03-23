# Solicitar al usuario que ingrese 10 números.
numeros = []
for i in range(10):
    num = float(input("Ingrese un número: "))
    numeros.append(num)

# Calcular el promedio de la lista
promedio = sum(numeros) / len(numeros)

# Mostrar el resultado del promedio al usuario.
print("El promedio de los números ingresados es:", promedio)

