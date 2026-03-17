def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    gasto = float(input("Ingrese el gasto:\n "))
    dinero_recibido = int(input("Ingrese el dinero recibido:\n "))

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
