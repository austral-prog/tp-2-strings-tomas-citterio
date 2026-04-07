def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    print("Ingresar gasto: ")
    gasto = float(input("Ingresar gasto:\n"))
    print(gasto)
    dinero_recibido = int(input())

    vuelto = (dinero_recibido - gasto)

    pesos = int(vuelto)
    centavos = int((vuelto - pesos) * 100)
    if centavos==50
        centavos = 60

    print("\nVuelto\n")
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)
