


# a. Variable llamada "pesos" con input
pesos = input("Ingrese la cantidad en pesos colombianos (COP): ")

# b. Convertir a decimales
pesos = float(pesos)

# c. Variable TRM (COP a USD)
TRM = 4300

# d. Cálculo de la conversión
dolares = pesos / TRM

# e. Convertir a decimales para mejor comprensión
dolares = float(dolares)

# f. Mostrar el resultado con dos decimales
print(f'Tienes $ {dolares:.2f} dólares')