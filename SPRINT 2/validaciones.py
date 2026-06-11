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
        int(float(opcion)) < min or int(float(opcion)) > max):
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
    valido = True
    
    if len(cadena) == 0:
        valido = False
    
    for i in range(len(cadena)):
        if (cadena[i] != "1" and cadena[i] != "2" and cadena[i] != "3" and
            cadena[i] != "4" and cadena[i] != "5" and cadena[i] != "6" and
            cadena[i] != "7" and cadena[i] != "8" and cadena[i] != "9" and
            cadena[i] != "0" and cadena[i] != "."):
            valido = False
            break
    
    return valido


def validar_fecha() -> str:
    """
    Descripción: Solicita y valida de forma secuencial los datos del año,
    mes y día para estructurar una fecha en formato de cadena.
    Retorno: Cadena de caracteres que representa la fecha armada.
    """
    year = validar_numero_mayor(
        0,
        "Ingresa el año de nacimiento: ",
        "Error, ingresa un año valido: "
    )

    mes = validar_numero_rango(
        1, 12,
        "Ingresa el mes de nacimiento: ",
        "Error, ingresa un mes valido: "
    )

    dia = validar_numero_rango(
        1, 31,
        "Ingresa el dia de nacimiento: ",
        "Error, ingresa un dia valido: "
    )

    fecha = f"{int(year)}-{mes}-{dia}"
    return fecha


def validar_mail(mensaje: str, mensaje_error: str) -> str:
    """
    Descripción: Valida que el mail tenga '@'.
    Parámetros:
        mensaje: Texto de solicitud.
        mensaje_error: Texto de error.
    Retorno: Mail validado.
    """
    mail = input(mensaje)
    valido = False
    
    while valido == False:
        for i in range(len(mail)):
            if mail[i] == "@":
                valido = True
                break

        if valido == False:
            mail = input(mensaje_error)
    return mail


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