from validaciones import validar_cadena, validar_numero_rango
from gestion_usuarios import *
from usuarios import usuarios
from estadisticas import *


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
            iniciar_sesion(usuarios)
        else:
            cartel("Hasta luego")
            flag = False


def ejecutar_menu_jugador(lista: list, i: int) -> None:
    """
    Descripción: Controla el flujo del menú de opciones para el jugador.
    Parámetros:
        lista: Lista que contiene a los usuarios registrados.
        i: Índice del usuario que inició sesión.
    """
    flag = True
    while flag == True:
        mostrar_menu_jugador()
        opcion = validar_numero_rango(
            1, 5, "ingresa una opcion: ",
            "Error,ingresa opcion valida: "
        )
        if opcion == 1:
            cartel("Ver datos de usuario")
            usuario = lista[i]
            mostrar_usuario(usuario)
        elif opcion == 2:
            cartel("2. Jugar juego 1")
        elif opcion == 3:
            cartel("3. Jugar juego 2")
        elif opcion == 4:
            cartel("4. Ver puntajes")
        else:
            cartel("Sesión cerrada")
            flag = False
            ejecutar_menu_principal()


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
        elif opcion == 3:
            cartel("3. Eliminar usuario")
            eliminar_usuario(lista)
        else:
            cartel("Sesión cerrada")
            flag = False
            ejecutar_menu_principal()


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
            1, 7, "ingresa una opcion: ",
            "Error,ingresa opcion valida: "
        )
        if opcion == 1:
            cartel("1. Promedio de edad")
            promedio_edad_usuarios(lista)
        elif opcion == 2:
            cartel("2. Usuario más joven")
            buscar_usuario_mas_joven(lista)
        elif opcion == 3:
            cartel("4. Cantidad total de usuarios")
            calcular_cantidad_usuarios(lista)
        elif opcion == 4:
            cartel("6. Buscar usuario por nombre")
            encontrar_usuario(lista)
        elif opcion == 5:
            cartel("7. Listado completo de usuarios")
            mostrar_lista_usuarios(lista)
        elif opcion == 6:
            cartel("8. Usuario con nombre más largo")
            buscar_usuario_nombre_mas_largo(lista)
        else:
            cartel("Volver al menu ADMIN")
            flag = False
            ejecutar_menu_admin(lista)


def mostrar_menu_principal() -> None:
    """
    Descripción: Muestra en consola las opciones del menú principal.
    """
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Salir")


def mostrar_menu_jugador() -> None:
    """
    Descripción: Muestra en consola las opciones del menú del jugador.
    """
    print("\n=== BIENVENIDO JUGADOR ===")
    print("1. Ver datos personales")
    print("2. Jugar juego 1")
    print("3. Jugar juego 2")
    print("4. Ver puntajes")
    print("5. Cerrar sesión")


def mostrar_menu_admin() -> None:
    """
    Descripción: Muestra en consola las opciones del menú del administrador.
    """
    print("\n=== BIENVENIDO ADMIN ===")
    print("1. Ver estadísticas")
    print("2. Modificar usuario")
    print("3. Eliminar usuario")
    print("4. Cerrar sesión")


def mostrar_menu_estadisticas() -> None:
    """
    Descripción: Muestra en consola las opciones del menú de estadísticas.
    """
    print("\n=== ESTADÍSTICAS ===")
    print("1. Promedio de edad")
    print("2. Usuario más joven")
    print("3. Cantidad total de usuarios")
    print("4. Buscar usuario por nombre")
    print("5. Listado completo de usuarios")
    print("6. Usuario con nombre más largo")
    print("7. Volver")


def mostrar_usuario(lista: list) -> None:
    """
    Descripción: Muestra en consola los datos detallados de un usuario.
    Parámetros:
        lista: Lista con los datos del usuario.
    """
    print(f" Nombre = {lista[4]}")
    print(f" Apellido = {lista[5]}")
    print(f" Mail = {lista[1]}")
    print(f" Rol = {lista[3]}")
    print(f" Edad = {lista[6]}")
    print(f" Nacionalidad = {lista[7]}")
    print(f" Dni = {lista[8]}")
    print(f" Fecha de registro = {lista[9]}")
    print(f" EStado de cuenta activa = {lista[10]}")


def mostrar_lista_usuarios(lista: list) -> None:
    """
    Descripción: Recorre e imprime la lista de todos los usuarios registrados.
    Parámetros:
        lista: Lista de usuarios a mostrar.
    """
    for i in range(len(lista)):
        mostrar_usuario(lista[i])
        print("-----------------------------")


def cartel(mensaje: str) -> None:
    """
    Descripción: Muestra un mensaje con separadores para mayor visibilidad.
    Parámetros:
        mensaje: Mensaje a mostrar.
    """
    print("-----------------------------")
    print(mensaje)
    print("-----------------------------")


def iniciar_sesion(lista: list) -> None:
    """
    Descripción: Gestiona el login de usuarios comprobando mail y contraseña.
    Parámetros:
        lista: Lista que contiene a los usuarios registrados.
    """
    mail = validar_cadena(
        "Mail: ", "ERROR,ingresa un mail valido: "
    )
    contraseña = validar_cadena(
        "Contraseña: ", "ERROR,ingresa una contraseña valida "
    )
    encontrado = False
    for i in range(len(lista)):
        if lista[i][1] == mail and lista[i][2] == contraseña:
            encontrado = True
            if lista[i][3] == "jugador":
                ejecutar_menu_jugador(lista, i)
            else:
                ejecutar_menu_admin(lista)
            break
    if encontrado == False:
        print("-----------------------------")
        print("Usuario no encontrado")
        print("-----------------------------")


# def modificar_usuario(lista:list):
#     encontrado = False
#     mail = validar_cadena("Mail: " , "ERROR,ingresa mail valido: ")
#     for i in range(len(lista)):
#         if lista[i][1] == mail:
#             encontrado = True
#     if encontrado == True:
#         cartel("Usuario encontrado")
#     else:
#         cartel("Usuario no encontrao")

    
