from validaciones import *


def eliminar_usuario(lista: list) -> None:
    """
    Descripción: Busca un usuario en la lista por su mail y lo elimina
    si es encontrado. Si no existe, muestra un mensaje de error.
    Parámetros:
        lista: Lista que contiene a los usuarios registrados.
    """
    encontrado = False
    mail = validar_cadena("Mail: ", "ERROR,ingresa un mail valido: ")
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
        print("ERROR,usuario no encontrado")
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
        "Mail: ", "ERROR,ingresa un mail valido: "
    )
    password = validar_cadena(
        "Contraseña: ", "Error,ingresa una contraseña valida: "
    )
    rol = validar_cadena(
        "Rol: ", "ERROR,ingresa un rol valido: "
    )
    nombre = validar_cadena(
        "Nombre: ", "ERROR,ingresa un nombre valido: "
    )
    apellido = validar_cadena(
        "Apelido: ", "ERROR,ingresa un apellido valido: "
    )
    edad = validar_numero_rango(
        0, 150, "Edad: ", "ERROR,ingresa una edad valida: "
    )
    nacionalidad = validar_cadena(
        "Nacionalidad: ", "ERROR,ingresa una nacionalidad valida: "
    )
    dni = validar_numero_mayor(
        0, "Dni: ", "ERROR,ingresa un DNI valido: "
    )
    fecha_registro = validar_fecha()
    activo = True
    nuevo_usuario = [
        id, mail, password, rol, nombre, apellido,
        edad, nacionalidad, dni, fecha_registro, activo
    ]
    lista.append(nuevo_usuario)



