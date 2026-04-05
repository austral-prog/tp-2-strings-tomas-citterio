def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    gasto = float(input("Ingresar gasto:\n"))
    dinero_recibido = int(input("Dinero recibido\n"))

    vuelto = round(dinero_recibido - gasto, 2)

    pesos = int(vuelto)
    centavos = round((vuelto - pesos) * 100)

    print("\nVuelto\n")
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)
