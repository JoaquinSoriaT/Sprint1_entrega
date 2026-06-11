def validar_numero_rango(
    min: int, max: int,
    mensaje: str, mensaje_error: str
) -> int:
    """
    Descripción: Valida que el número ingresado esté dentro del rango indicado.
    Parámetros:
        min: Valor mínimo aceptado.
        max: Valor máximo aceptado.
        mensaje: Mensaje que se muestra al pedir el número.
        mensaje_error: Mensaje que se muestra si el número no es válido.
    Retorno: Número validado dentro del rango.
    """
    opcion = input(mensaje)
    while (validar_que_sea_numero(opcion) == False or
        int(opcion) < min or int(opcion) > max):
        opcion = input(mensaje_error)
    return int(float(opcion))


def validar_cadena(mensaje: str, mensaje_error: str) -> str:
    """
    Descripción: Valida que la cadena ingresada no esté vacía.
    Parámetros:
        mensaje: Mensaje que se muestra al pedir la cadena.
        mensaje_error: Mensaje que se muestra si la cadena está vacía.
    Retorno: Cadena validada no vacía.
    """
    cadena = input(mensaje)
    while len(cadena) == 0:
        cadena = input(mensaje_error)
    return cadena


def validar_numero_mayor(
    marca: float, mensaje: str, mensaje_error: str
) -> float:
    """
    Descripción: Valida que el número ingresado sea mayor a la marca indicada.
    Parámetros:
        marca: Valor mínimo exclusivo aceptado.
        mensaje: Mensaje que se muestra al pedir el número.
        mensaje_error: Mensaje que se muestra si el número no es válido.
    Retorno: Número flotante validado mayor a la marca.
    """
    opcion = input(mensaje)
    while validar_que_sea_numero(opcion) == False or float(opcion) <= marca:
        opcion = input(mensaje_error)
    return float(opcion)


def validar_que_sea_numero(cadena: str) -> bool:
    """
    Descripción: Valida que todos los caracteres de la cadena
    sean dígitos o punto decimal.
    Parámetros:
        cadena: Cadena a validar.
    Retorno: True si la cadena es un número,
    False si contiene caracteres no numéricos.
    """
    if len(cadena) == 0:
        return False
    
    valido = True

    for i in range(len(cadena)):
        if (cadena[i] != "1" and
            cadena[i] != "2" and
            cadena[i] != "3" and
            cadena[i] != "4" and
            cadena[i] != "5" and
            cadena[i] != "6" and
            cadena[i] != "7" and
            cadena[i] != "8" and
            cadena[i] != "9" and
            cadena[i] != "0" and
            cadena[i] != "."):
            valido = False
            break
        
    return valido


def cartel(mensaje: str) -> None:
    """
    Descripción: Muestra un texto centrado o destacado entre líneas 
    separadoras, acumulando todo el diseño en una sola variable.
    Parámetros:
        mensaje: El texto o título que se quiere mostrar dentro del cartel.
    """
    separador = "-----------------------------\n"
    
    contenido = separador
    contenido += f"{mensaje}\n"
    contenido += separador
    print(contenido)


def es_opcion_valida(opcion: str, opciones_validas: list) -> bool:
    """Verifica si la opción está dentro de la lista de opciones válidas."""
    es_valida = False
    for elemento in opciones_validas:
        if opcion == elemento:
            es_valida = True
            break
    return es_valida


def validar_respuesta_pregunta() -> str:
    """
    Descripción: Valida que la respuesta ingresada sea a, b o c.
    Retorno: La respuesta validada (a, b o c).
    """
    opciones_validas = ["a", "b", "c"]
    respuesta = input("Ingresa tu respuesta (a, b o c): ").lower()
    while es_opcion_valida(respuesta, opciones_validas) is False:
        respuesta = input(
            "Error. Ingresa una opción válida (a, b o c): "
        ).lower()
    return respuesta