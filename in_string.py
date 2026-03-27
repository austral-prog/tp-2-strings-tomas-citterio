def check_vowels():
    """Lee un nombre y verifica si contiene cada una de las vocales (a, e, i, o, u),
    sin distinguir mayúsculas de minúsculas.
    """
    nombre = input("Ingrese el mombre: ")
    nombremin = nombre.lower()
    a = "a" in nombremin
    mensaje_a = f"Contiene a: {a}"
    print(mensaje_a)
    e = "e" in nombremin
    mensaje_e = f"Contiene e: {e}"
    print(mensaje_e)
    i = "i" in nombremin
    mensaje_i = f"Contiene i: {i}"
    print(mensaje_i)
    o = "o" in nombremin
    mensaje_o = f"Contiene o: {o}"
    print(mensaje_o)
    u = "u" in nombremin
    mensaje_u = f"Contiene u: {u}"
    print(mensaje_u)
