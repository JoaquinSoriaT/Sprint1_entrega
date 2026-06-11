from validaciones import validar_cadena, validar_numero_rango,cartel


def mostrar_usuario_simple(
    usuario: dict, titulo: str
) -> None:
    """
    Descripción: Muestra en consola los datos básicos de un usuario específico
    junto con un título personalizado.
    Parámetros:
        usuario: Diccionario con los datos del usuario.
        titulo: Encabezado para la visualización.
    """
    print("-----------------------------")
    print(titulo)
    print(f"Nombre = {usuario['nombre']}")
    print(f"Apellido = {usuario['apellido']}")
    print(f"Edad = {usuario['edad']}")
    print("-----------------------------")


def mostrar_todos_usuarios_simple(lista: list, titulo: str) -> None:
    """
    Descripción: Recorre e imprime los datos básicos de todos los usuarios
    dentro de la lista provista.
    Parámetros:
        lista: Lista de usuarios a mostrar.
        titulo: Encabezado común para cada usuario.
    """
    for i in range(len(lista)):
        mostrar_usuario_simple(lista[i], titulo)
        print("-----------------------------")


def promediar_lista(lista: list) -> float:
    """
    Descripción: Calcula el promedio numérico de los elementos de una lista.
    Parámetros:
        lista: Lista unidimensional con valores numéricos.
    Retorno: Promedio obtenido de la suma de los elementos.
    """
    promedio = 0
    if len(lista) > 0:
        acumulador = 0
        for i in range(len(lista)):
            acumulador += lista[i]
        promedio = acumulador / len(lista)
    return promedio


def promedio_edad_usuarios(lista: list) -> None:
    """
    Descripción: Extrae las edades de los usuarios, calcula su promedio
    e imprime el resultado en pantalla.
    Parámetros:
        lista: Lista bidimensional de usuarios.
    """
    if len(lista) == 0:
        cartel("No hay usuarios")
    else:
        edades = []
        for i in range(len(lista)):
            edades.append(lista[i]["edad"])
        promedio = promediar_lista(edades)
    print("-----------------------------")
    print(f"El promedio de edad de los usuarios es {promedio}")
    print("-----------------------------")


def buscar_indice_menor(lista: list, clave: str) -> int:
    """
    Descripción: Determina el índice del elemento con el menor valor numérico
    en un atributo específico de la lista.
    Parámetros:
        lista: Lista bidimensional a evaluar.
        indice_atributo: Índice del valor numérico a comparar.
    Retorno: Índice del elemento con el valor mínimo hallado.
    """
    indice_menor = -1
    if len(lista) > 0:
        indice_menor = 0
        for i in range(len(lista)):
            if (lista[i][clave] <
                    lista[indice_menor][clave]):
                indice_menor = i
    return indice_menor


def buscar_indice_mayor(lista: list, clave: str) -> int:
    """
    Descripción: Determina el índice del elemento con el mayor valor numérico
    en un atributo específico de la lista.
    Parámetros:
        lista: Lista bidimensional a evaluar.
        indice_atributo: Índice del valor numérico a comparar.
    Retorno: Índice del elemento con el valor máximo hallado.
    """
    indice_mayor = -1
    if len(lista) > 0:
        indice_mayor = 0
        for i in range(len(lista)):
            if (lista[i][clave] >
                lista[indice_mayor][clave]):
                indice_mayor = i
    return indice_mayor


def buscar_usuario_mas_joven(lista: list) -> None:
    """
    Descripción: Identifica y expone en consola los datos del usuario
    con la menor edad en la lista.
    Parámetros:
        lista: Lista bidimensional de usuarios.
    """
    indice = buscar_indice_menor(lista, "edad")
    if indice == -1:
        cartel("No hay usuarios")
    else:
        mostrar_usuario_simple(lista[indice], "El usuario mas joven")


def buscar_usuario_mas_viejo(lista: list) -> None:
    """
    Descripción: Identifica y expone en consola los datos del usuario
    con la mayor edad en la lista.
    Parámetros:
        lista: Lista bidimensional de usuarios.
    """
    indice = buscar_indice_mayor(lista, "edad")
    if indice == -1:
        cartel("No hay usuarios")
    else:
        mostrar_usuario_simple(lista[indice], "El usuario de mayor edad")


def calcular_cantidad_usuarios(lista: list) -> None:
    """
    Descripción: Contabiliza la cantidad total de usuarios registrados
    e informa el número por consola.
    Parámetros:
        lista: Lista de usuarios bajo análisis.
    """
    cantidad_usuarios = len(lista)
    print("-----------------------------")
    print(f"Cantidad de usuarios: {cantidad_usuarios}")
    print("-----------------------------")


def encontrar_cadena(
    lista: list, cadena: str,
    clave: str, mensaje_error: str
) -> list:
    """
    Descripción: Busca y retorna todos los elementos de la lista
    que coincidan con la cadena en el índice indicado.
    Parámetros:
        lista: Lista bidimensional a filtrar.
        cadena: Valor a buscar.
        clave: Clave de la cadena de texto a medir.
        mensaje_error: Mensaje a mostrar si no se encuentran resultados.
    Retorno: Lista con los elementos que coinciden con la cadena.
    """
    encontrado = []
    for i in range(len(lista)):
        if lista[i][clave].lower() == cadena.lower():
            encontrado.append(lista[i])
    if len(encontrado) == 0:
        print("-----------------------------")
        print(mensaje_error)
        print("-----------------------------")
    return encontrado


def encontrar_usuario(lista: list) -> None:
    """
    Descripción: Solicita un nombre por pantalla, busca las coincidencias
    en la lista y expone los resultados simples hallados.
    Parámetros:
        lista: Lista bidimensional de usuarios.
    """
    nombre_buscado = validar_cadena(
        "Nombre: ", "ERROR, ingresa un nombre valido: "
    )
    usuarios_encontrados = encontrar_cadena(
        lista, nombre_buscado, "nombre", "Error,nombre no encontrado"
    )
    if len(usuarios_encontrados) > 0:
        mostrar_todos_usuarios_simple(
            usuarios_encontrados,
            f"Usuarios con el nombre {nombre_buscado}"
        )


def buscar_indice_cadena_mas_larga(
    lista: list, clave: str
) -> int:
    """
    Descripción: Evalúa las cadenas de texto de un atributo específico y
    retorna el índice del elemento con mayor longitud.
    Parámetros:
        lista: Lista bidimensional a evaluar.
        clave: Clave de la cadena de texto a medir.
    Retorno: Índice del elemento con la cadena de mayor extensión.
    """
    indice_mayor = -1
    if len(lista) > 0:
        indice_mayor = 0
        for i in range(len(lista)):
            if (len(lista[i][clave]) >
                len(lista[indice_mayor][clave])):
                indice_mayor = i
    return indice_mayor


def buscar_usuario_nombre_mas_largo(lista: list) -> None:
    """
    Descripción: Identifica y despliega en pantalla al usuario que posea
    el nombre con la mayor cantidad de caracteres.
    Parámetros:
        lista: Lista bidimensional de usuarios.
    """
    indice = buscar_indice_cadena_mas_larga(lista, "nombre")
    if indice == -1:
        cartel("No hay usuarios")
    else:
        mostrar_usuario_simple(lista[indice], "Usuario con nombre mas largo")


def contar_usuarios_mayores_que(lista: list) -> None:
    """
    Descripción: Cuenta cuántos usuarios tienen una edad
    mayor a la ingresada por el usuario.
    Parámetros:
        lista: Lista bidimensional de usuarios.
    """
    edad_limite = validar_numero_rango(
        0, 150,
        "Ingresa la edad: ",
        "ERROR, ingresa una edad valida: "
    )

    contador = 0
    usuarios_encontrados = []

    for i in range(len(lista)):
        if lista[i]["edad"] > edad_limite:
            contador += 1
            usuarios_encontrados.append(lista[i])

    print("-----------------------------")
    print(f"Usuarios mayores de {edad_limite}: {contador}")

    if contador > 0:
        ver = input("¿Querés ver los usuarios? (s/n): ").lower()

        while ver != "s" and ver != "n":
            ver = input("RESPUESTA INVALIDA. ¿Querés ver los usuarios? (s/n): ").lower()

        if ver == "s":
            for u in usuarios_encontrados:
                print(f"""
Nombre = {u['nombre']}
Apellido = {u['apellido']}
Mail = {u['mail']}
Edad = {u['edad']}
-----------------------------
""")

    print("-----------------------------")