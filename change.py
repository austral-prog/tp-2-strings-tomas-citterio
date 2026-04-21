def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """


print("Ingresar gasto:")
gasto = float(input())
print("Dinero recibido")
dinero = int(input())

vuelto = dinero - gasto

pesos = int(vuelto)
centavos = round((vuelto - pesos) * 100)

print()
print("Vuelto")
print()
print("Pesos:")
print(pesos)
print("Centavos:")
print(centavos)
