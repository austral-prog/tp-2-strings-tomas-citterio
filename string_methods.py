def string_methods():
    """Demuestra el uso de métodos de string: strip, lstrip, rstrip, upper, lower,
    title, find, replace, count, operador in, slicing con paso, reverso,
    f-strings y strings multilínea.
    """
    nombre = "   Grace Hopper   "
    frase = "Python es un gran lenguaje de programacion"
    multilinea = """Linea 1
Linea 2
Linea 3"""
    nombre_noespacios = nombre.strip()
    mensaje_noespacios = f"Strip: {nombre_noespacios}"
    print(mensaje_noespacios)
    nombre_noespaciosizq = nombre.lstrip()
    mensaje_noespaciosizq = f"Lstrip: {nombre_noespaciosizq}"
    print(mensaje_noespaciosizq)
    nombre_noespaciosder = nombre.rstrip()
    mensaje_noespaciosder = f"Rstrip: {nombre_noespaciosder}"
    print(mensaje_noespaciosder)
    frase_mayus = frase.upper()
    mensaje_mayus = f"Upper: {frase_mayus}"
    print(mensaje_mayus)
    frase_min = frase.lower()
    mensaje_lower = f"Lower: {frase_min}"
    print(mensaje_lower)
    frase_title = frase.title()
    mensaje_title = f"Title: {frase_title}"
    print(mensaje_title)
    frase_find = frase.find("gran")
    mensaje_find = f"Find: {frase_find}"
    print(mensaje_find)
    frase_replace = frase.replace("programacion", "desarrollo")
    mensaje_replace = f"Replace: {frase_replace}"
    print(mensaje_replace)
    frase_count = frase.count("a")
    mensaje_count = f"Count: {frase_count}"
    print(mensaje_count)
    python_in = "python" in frase.lower()
    mensaje_python = f"Python in: {python_in}"
    print(mensaje_python)
    java_in = "java" in frase.lower()
    mensaje_java = f"Java in: {java_in}"
    print(mensaje_java)
    slice_frase = frase[ :6]
    mensaje_slice = f"Slice: {slice_frase}"
    print(mensaje_slice)
    paso_frase = frase[ :6:2]
    mensaje_paso = f"Paso: {paso_frase}"
    print(mensaje_paso)
    python_inverso = "python"[ ::-1]
    mensaje_inverso = f"Reverso: {python_inverso}"
    print(mensaje_inverso)
    combinar = nombre_noespacios + " " + "sabe" + " " + frase[:6]
    mensaje_combinar = f"Formato: {combinar}"
    print(mensaje_combinar)
    print(multilinea)
   
