def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    precio = int(input("Ingrese el precio: "))
    descuento = float(input("Ingrese el descuento: "))
    cantidad = int(input("Ingrese cantidad: "))
    precio_descuento = precio - descuento
    total = precio_descuento * cantidad
    mensaje_precio = f"Precio: {precio}"
    print(mensaje_precio)
    mensaje_descuento = f"Descuento: {descuento}"
    print(mensaje_descuento)
    mensaje_precio_descuento = f"Precio descuento: {precio_descuento}"
    print(mensaje_precio_descuento)
    mensaje_total = f"Total: {total}"
    print(mensaje_total)
casting()
