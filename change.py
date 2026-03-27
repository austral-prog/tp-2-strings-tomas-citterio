def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    print("Ingrese el gasto: ")
    gasto = float(input())
    print("Ingrese el dinero recibido: ")

    vuelto = dinero_recibido - gasto

    pesos = int(vuelto)
    centavos = int(round((vuelto - pesos) * 100))

    print()
    print("Vuelto")
    print()
    print("Pesos: ")
    print(pesos)
    print("Centavos: ")
    print(centavos)
