from validaciones import *

def iniciar_sesion(lista: list) -> int:
    """
    Descripción: Gestiona el login de usuarios comprobando mail y contraseña.
    Parámetros:
        lista: Lista que contiene a los usuarios registrados.
    Retorno:
        Índice del usuario si las credenciales son correctas.
        Retorna -1 si no encuentra coincidencias.
    """
    mail = validar_cadena(
        "Mail: ",
        "ERROR,ingresa un mail valido: "
    )

    contraseña = validar_cadena(
        "Contraseña: ",
        "ERROR,ingresa una contraseña valida "
    )
    indice = -1

    for i in range(len(lista)):
        if lista[i]["mail"] == mail and lista[i]["password"] == contraseña:
            indice = i

    return indice


def modificar_usuario(lista: list) -> None:
    """
    Descripción: Busca un usuario por su mail y permite modificar
    sus datos personales básicos si es encontrado.
    Parámetros:
        lista: Lista que contiene a los usuarios registrados.
    """
    mail = validar_cadena(
        "Mail del usuario: ",
        "ERROR, ingresa un mail valido: "
    )

    encontrado = False

    for i in range(len(lista)):
        if lista[i]["mail"] == mail:
            encontrado = True

            lista[i]["nombre"] = validar_cadena(
                "Nuevo nombre: ",
                "ERROR, ingresa un nombre valido: "
            )

            lista[i]["apellido"] = validar_cadena(
                "Nuevo apellido: ",
                "ERROR, ingresa un apellido valido: "
            )

            lista[i]["edad"] = validar_numero_rango(
                0, 150,
                "Nueva edad: ",
                "ERROR, ingresa una edad valida: "
            )

            cartel("Usuario modificado")
            break

    if encontrado == False:
        cartel("Usuario no encontrado")

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
        if lista[i]["mail"] == mail:
            encontrado = True
            lista.pop(i)
            cartel("Usuario borrado")
            break
    if encontrado == False:
        cartel("ERROR,usuario no encontrado")


def validar_rol() -> str:
    """
    Descripción: Valida que el rol ingresado sea 'admin' o 'jugador'.
    Retorno: Rol validado ('admin' o 'jugador').
    """
    rol = validar_cadena("Rol (admin/jugador): ", "ERROR, ingresa un rol valido: ")
    while rol != "admin" and rol != "jugador":
        rol = validar_cadena("ERROR, ingrese 'admin' o 'jugador': ")
    return rol


def registrar_usuario(lista: list) -> None:
    """
    Descripción: Solicita y valida los datos de un nuevo usuario, genera
    su ID de forma automática y lo añade a la lista de usuarios.
    Parámetros:
        lista: Lista donde se almacenará el nuevo usuario.
    """
    if len(lista) == 0:
        id = 1
    else:
        id = len(lista) + 1
        
    mail = validar_mail(
        "Mail: ", "ERROR,ingresa un mail valido: "
    )
    password = validar_cadena(
        "Contraseña: ", "Error,ingresa una contraseña valida: "
    )
    rol = validar_rol()
    nombre = validar_cadena(
        "Nombre: ", "ERROR,ingresa un nombre valido: "
    )
    apellido = validar_cadena(
        "Apellido: ", "ERROR,ingresa un apellido valido: "
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
    nuevo_usuario = {
        "id": id,
        "mail": mail,
        "password": password,
        "rol": rol,
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "nacionalidad": nacionalidad,
        "dni": dni,
        "fecha_registro": fecha_registro,
        "activo": activo
    }
    lista.append(nuevo_usuario)



