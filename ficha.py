def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)
    nombre = input("Ingrese nombre completo: ")
    email = input("Ingrese email: ")
    nota1 = int(input("Ingrese nota 1: "))
    nota2 = int(input("Ingrese nota 2: "))
    nota3 = int(input("Ingrese nota 3: "))
    print("""=====================
FICHA DEL ALUMNO
=====================""")
    nombre = nombre.strip()
    nombre = nombre.title()
    men_nombre = f"Nombre: {nombre}"
    print(men_nombre)
    email = email.lower()
    men_email = f"Email: {email}"
    print(men_email)
    nombrecarac = len(nombre)
    mennombrecarac = f"Caracteres en nombre: {nombrecarac}"
    print(mennombrecarac)
    pos_espacio = nombre.find(" ")
    iniciales = nombre[0] + nombre[pos_espacio + 1]
    nombre_lower = nombre.lower()
    meniniciales = f"-Iniciales: {iniciales}"
    print(meniniciales)
    nombre_usuario = nombre_lower[pos_espacio + 1:] + "." + nombre_lower[:pos_espacio]
    menusuario = f"Usuario: {nombre_usuario}"
    print(menusuario)
    email_valido = "@" in email
    menemail_valido = f"E-mail valido: {email_valido}"
    print(menemail_valido)
    pos_arroba = email.find("@")
    dominio = email[pos_arroba + 1:]
    mendominio = f"Dominio: {dominio}"
    print(mendominio)
    nombre_archivo = nombre_lower.replace(" ", "_")
    menrchivo = f"Nombre para archivo: {nombre_archivo}"
    print(menrchivo)
    cant_a = nombre.count("a")
    mencant_a = f"Cantidad de a: {cant_a}"
    print(mencant_a)
    codigo = nombre[ : :-1]
    mencodigo = f"Codigo secreto: {codigo}"
    print(mencodigo.upper())
    mennota1 = f"Nota 1: {nota1}"
    mennota2 = f"Nota 2: {nota2}"
    mennota3 = f"Nota 3: {nota3}"
    print(mennota1)
    print(mennota2)
    print(mennota3)
    suma = nota1 + nota2 + nota3
    mensuma = f"Suma: {suma}"
    print(mensuma)
    promedio_float = float((nota1 + nota2 + nota3) / 3)
    menpromedio = f"Promedio: {promedio_float}"
    print(menpromedio)
    promedio_int = int((nota1 + nota2 + nota3) / 3)
    menpromedioint = f"Promedio: {promedio_int}"
    print(menpromedioint)
    print("========================")
