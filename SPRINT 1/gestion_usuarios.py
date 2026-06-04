from interfaz import mostrar_usuario
from validaciones import *


def eliminar_usuario(lista: list) -> None:
    """
    Descripción: Busca un usuario en la lista por su mail y lo elimina
    si es encontrado. Si no existe, muestra un mensaje de error.
    Parámetros:
        lista: Lista que contiene a los usuarios registrados.
    """
    encontrado = False
    mail = validar_cadena("Mail: ", "ERROR, ingresa un mail valido: ")
    for i in range(len(lista)):
        if lista[i][1] == mail:
            encontrado = True
            lista.pop(i)
            print("-----------------------------")
            print("Usuario borrado")
            print("-----------------------------")
            break
    if encontrado == False:
        print("-----------------------------")
        print("ERROR, usuario no encontrado")
        print("-----------------------------")


def registrar_usuario(lista: list) -> None:
    """
    Descripción: Solicita y valida los datos de un nuevo usuario, genera
    su ID de forma automática y lo añade a la lista de usuarios.
    Parámetros:
        lista: Lista donde se almacenará el nuevo usuario.
    """
    id = len(lista) + 1
    mail = validar_cadena(
        "Mail: ", "ERROR, ingresa un mail valido: "
    )
    password = validar_cadena(
        "Contraseña: ", "ERROR, ingresa una contraseña valida: "
    )
    rol = validar_cadena(
        "Rol: ", "ERROR, ingresa un rol valido: "
    )
    nombre = validar_cadena(
        "Nombre: ", "ERROR, ingresa un nombre valido: "
    )
    apellido = validar_cadena(
        "Apellido: ", "ERROR, ingresa un apellido valido: "
    )
    edad = validar_numero_rango(
        0, 150, "Edad: ", "ERROR, ingresa una edad valida: "
    )
    nacionalidad = validar_cadena(
        "Nacionalidad: ", "ERROR, ingresa una nacionalidad valida: "
    )
    dni = validar_numero_mayor(
        0, "Dni: ", "ERROR, ingresa un DNI valido: "
    )
    fecha_registro = validar_fecha()
    activo = True
    nuevo_usuario = [
        id, mail, password, rol, nombre, apellido,
        edad, nacionalidad, dni, fecha_registro, activo
    ]
    lista.append(nuevo_usuario)


def encontrar_usuario_por_dato(
    lista: list,
    sub_indice: int,
    dato: str,
    mensaje_error: str = "ERROR, ingresa un dato valido: "
) -> list:
    """
    Descripción: Busca un usuario en la lista por un dato específico
    (como mail, nombre, etc.) y devuelve su índice si es encontrado.
    Parámetros:
        lista: Lista que contiene a los usuarios registrados.
        dato: El valor del dato a buscar (por ejemplo, el mail).
        sub_indice: El índice en la sublista del usuario donde se encuentra 
        el dato a buscar.
        mensaje_error: Mensaje que se muestra si el dato no es encontrado.
    Retorno: Índice del usuario encontrado o llamada recursiva si no se 
    encuentra.
    """
    for i in range(len(lista)):
        if lista[i][sub_indice] == dato:
            retorno = lista[i]
    retorno = encontrar_usuario_por_dato(lista, sub_indice, input(mensaje_error))
    return retorno


def normalizar_indice(indice):
    """
    Descripción: Convierte un nombre de campo a su índice correspondiente en 
    la sublista del usuario.
    Parámetros:
        indice: El nombre del campo a convertir.
    Retorno: El índice correspondiente en la sublista del usuario o llamada 
    recursiva si el campo no es válido.
    """
    if indice == "Mail":
        retorno = 1
    elif indice == "Contraseña":
        retorno = 2
    elif indice == "Rol":
        retorno = 3
    elif indice == "Nombre":
        retorno = 4
    elif indice == "Apellido":
        retorno = 5
    elif indice == "Edad":
        retorno = 6
    elif indice == "Nacionalidad":
        retorno = 7
    elif indice == "Dni":
        retorno = 8
    else:
        retorno = normalizar_indice(input("ERROR, ingresa un campo valido: "))
    return retorno


def modificar_usuario_especifico(lista: list) -> None:
    """
    Descripción: Permite modificar un dato específico de un usuario 
    encontrado por su mail.
    Parámetros:
        lista: Lista que contiene a los usuarios registrados.
    """
    usuario = encontrar_usuario_por_dato(
        lista, 1, input("Mail del usuario a modificar: "),
        "ERROR, ingresa un mail valido: "
    )

    a_modificar = input(
        "\nQue desea modificar?\n"
        "- Mail\n"
        "- Contraseña\n"
        "- Rol\n"
        "- Nombre\n"
        "- Apellido\n"
        "- Edad\n"
        "- Nacionalidad\n"
        "- Dni\n"
    )

    indice_a_modificar = normalizar_indice(a_modificar)
    usuario[indice_a_modificar] = input(f"Ingrese el nuevo {a_modificar}: ")
    mostrar_usuario(usuario)