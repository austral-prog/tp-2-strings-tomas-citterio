def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """
    base = int(input("Base: "))
    altura = int(input("Altura: "))
    mensaje_base = f"Base: {base}"
    print(mensaje_base)
    mensaje_altura = f"Altura: {altura}"
    print(mensaje_altura)
    area = f"Area: {base * altura}"
    print(area)
    perimetro = f"Perimetro: {(base + altura) * 2}"
    print(perimetro)
rectangle()
