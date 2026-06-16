from validaciones import validar_numero_rango
from gestion_usuarios import *
from usuarios import usuarios
from estadisticas import *
from LIFE.interfaz_life import ejecutar_menu_life
from AHORCADO.ahorcado import ejecutar_ahorcado


def ejecutar_menu_principal() -> None:
    """
    Descripción: Controla el flujo del menú principal del sistema.
    """
    flag = True
    while flag == True:
        mostrar_menu_principal()
        opcion = validar_numero_rango(
            1, 3, "ingresa una opcion: ",
            "Error,ingresa opcion valida: "
        )
        if opcion == 1:
            cartel("Registrar nuevo usuario")
            registrar_usuario(usuarios)
        elif opcion == 2:
            cartel("Iniciar sesion")
            gestionar_login(usuarios)
        else:
            cartel("Hasta luego")
            flag = False


def ejecutar_menu_jugador(lista: list, i: int) -> None:
    """
    Descripción: Controla el flujo del menú de opciones para el jugador.
    Parámetros:
        lista: Lista de diccionarios con los usuarios registrados.
        i: Índice del usuario que inició sesión en la lista.
    """
    usuario = lista[i]
    flag = True
    while flag == True:
        mostrar_menu_jugador()
        opcion = validar_numero_rango(
            1, 5, "ingresa una opcion: ",
            "Error,ingresa opcion valida: "
        )
        if opcion == 1:
            cartel("Ver datos de usuario")
            mostrar_usuario(usuario)
        elif opcion == 2:
            ejecutar_menu_life(usuario["nombre"],usuario["apellido"])
        elif opcion == 3:
            ejecutar_ahorcado()
        elif opcion == 4:
            cartel("4. Ver puntajes")
        else:
            cartel("Sesión cerrada")
            flag = False


def ejecutar_menu_admin(lista: list) -> None:
    """
    Descripción: Controla el flujo del menú de opciones para el administrador.
    Parámetros:
        lista: Lista que contiene a los usuarios registrados.
    """
    flag = True
    while flag == True:
        mostrar_menu_admin()
        opcion = validar_numero_rango(
            1, 4, "ingresa una opcion: ",
            "Error,ingresa opcion valida: "
        )
        if opcion == 1:
            cartel("1. Ver estadisticas")
            ejecutar_menu_estadisticas(lista)
        elif opcion == 2:
            cartel("2. Modificar usuario")
            modificar_usuario(lista)
        elif opcion == 3:
            cartel("3. Eliminar usuario")
            eliminar_usuario(lista)
        else:
            cartel("Sesión cerrada")
            flag = False


def ejecutar_menu_estadisticas(lista: list) -> None:
    """
    Descripción: Controla el flujo del menú de estadísticas del sistema.
    Parámetros:
        lista: Lista que contiene a los usuarios registrados.
    """
    flag = True
    while flag == True:
        mostrar_menu_estadisticas()
        opcion = validar_numero_rango(
            1, 9, "ingresa una opcion: ",
            "Error,ingresa opcion valida: "
        )
        if opcion == 1:
            cartel("1. Promedio de edad")
            promedio_edad_usuarios(lista)
        elif opcion == 2:
            cartel("2. Usuario más joven")
            buscar_usuario_mas_joven(lista)
        elif opcion == 3:
            cartel("3. Cantidad total de usuarios")
            calcular_cantidad_usuarios(lista)
        elif opcion == 4:
            cartel("4. Buscar usuario por nombre")
            encontrar_usuario(lista)
        elif opcion == 5:
            cartel("5. Listado completo de usuarios")
            mostrar_lista_usuarios(lista)
        elif opcion == 6:
            cartel("6. Usuario con nombre más largo")
            buscar_usuario_nombre_mas_largo(lista)
        elif opcion == 7:
            cartel("7. Usuario de mayor edad")
            buscar_usuario_mas_viejo(lista)
        elif opcion == 8:
            cartel("8. Cantidad de usuarios mayores a una edad")
            contar_usuarios_mayores_que(lista)
        else:
            cartel("Volver al menu ADMIN")
            flag = False


def mostrar_lineas(titulo: str, opciones: list[str]) -> None:
    """
    Descripción: Muestra un título y una lista de opciones en consola.
    Parámetros:
        titulo: Título del menú.
        opciones: Lista de strings con las opciones a mostrar.
    """
    print(f"\n=== {titulo} ===")
    for opcion in opciones:
        print(opcion)


def mostrar_menu_principal() -> None:
    """
    Descripción: Muestra en consola las opciones del menú principal.
    """
    mostrar_lineas("MENÚ PRINCIPAL", [
        "1. Registrarse",
        "2. Iniciar sesión",
        "3. Salir"
    ])


def mostrar_menu_jugador() -> None:
    """
    Descripción: Muestra en consola las opciones del menú del jugador.
    """
    mostrar_lineas("BIENVENIDO JUGADOR", [
        "1. Ver datos personales",
        "2. Jugar L.I.F.E",
        "3. Jugar ahorcado",
        "4. Ver puntajes",
        "5. Cerrar sesión"
    ])


def mostrar_menu_admin() -> None:
    """
    Descripción: Muestra en consola las opciones del menú del administrador.
    """
    mostrar_lineas("BIENVENIDO ADMIN", [
        "1. Ver estadísticas",
        "2. Modificar usuario",
        "3. Eliminar usuario",
        "4. Cerrar sesión"
    ])


def mostrar_menu_estadisticas() -> None:
    """
    Descripción: Muestra en consola las opciones del menú de estadísticas.
    """
    mostrar_lineas("ESTADÍSTICAS", [
        "1. Promedio de edad",
        "2. Usuario más joven",
        "3. Cantidad total de usuarios",
        "4. Buscar usuario por nombre",
        "5. Listado completo de usuarios",
        "6. Usuario con nombre más largo",
        "7. Usuario de mayor edad",
        "8. Cantidad de usuarios mayores a una edad",
        "9. Volver"
    ])


def mostrar_usuario(usuario: dict) -> None:
    """
    Descripción: Muestra en consola los datos detallados de un usuario.
    Parámetros:
        usuario: Diccionario con los datos del usuario.
    """
    print(f"""
Nombre = {usuario["nombre"]}
Apellido = {usuario["apellido"]}
Mail = {usuario["mail"]}
Rol = {usuario["rol"]}
Edad = {usuario["edad"]}
Nacionalidad = {usuario["nacionalidad"]}
Dni = {usuario["dni"]}
Fecha de registro = {usuario["fecha_registro"]}
Estado de cuenta activa = {usuario["activo"]}
""")


def mostrar_lista_usuarios(lista: list) -> None:
    """
    Descripción: Recorre e imprime la lista de todos los usuarios registrados.
    Parámetros:
        lista: Lista de usuarios a mostrar.
    """
    for i in range(len(lista)):
        mostrar_usuario(lista[i])
        print("-----------------------------")


def gestionar_login(lista: list) -> None:
    """
    Descripción: Gestiona el inicio de sesión del usuario y redirige
    al menú correspondiente según su rol.
    Parámetros:
        lista: Lista que contiene a los usuarios registrados.
    """
    indice = iniciar_sesion(lista)

    if indice != -1:
        if lista[indice]["rol"] == "jugador":
            ejecutar_menu_jugador(lista, indice)
        else:
            ejecutar_menu_admin(lista)
    else:
        cartel("Usuario no encontrado")


    
