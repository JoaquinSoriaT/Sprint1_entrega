from LIFE.validaciones import validar_numero_rango,cartel
from LIFE.tablero import (
    ejecutar_partida_larga,
    ejecutar_partida_rapida,
    ejecutar_partida_personalizada,
)
from LIFE.tiradas import ejecutar_partida
from LIFE.final import mostrar_pantalla_abandono
from LIFE.ranking import ejecutar_ranking


def ejecutar_menu_life(nombre: str, apellido: str):
    """
    Descripción: Controla el bucle principal del menú del juego.
    Muestra las opciones, valida la entrada del usuario y deriva
    el flujo hacia el tipo de partida seleccionado o el ranking.
    """
    flag = True
    while flag == True:
        mostrar_menu_juego()
        opcion = validar_numero_rango(
            1,
            5,
            "Ingresa una opcion: ",
            "Error,ingresa una opcion valida: ",
        )
        if opcion == 1 or opcion == 2 or opcion == 3:
            validar_tipo_partida(opcion, nombre, apellido)
        elif opcion == 4:
            ejecutar_ranking()
        else:
            flag = False
            mostrar_pantalla_abandono("Hasta luego")


def validar_tipo_partida(opcion: int,nombre: str, apellido: str):
    """
    Descripción: Recibe la opción del menú principal, inicializa el
    tablero correspondiente (rápido, largo o personalizado) mediante
    la función adecuada y lo deriva al menú de confirmación.
    Parámetros:
        opcion: Entero que representa la variante de juego elegida.
    """
    if opcion == 1:
        tablero = ejecutar_partida_rapida()
    elif opcion == 2:
        tablero = ejecutar_partida_larga()
    else:
        tablero = ejecutar_partida_personalizada()
    ejecutar_menu_jugar_partida(tablero, nombre, apellido)


def ejecutar_menu_jugar_partida(tablero: list, nombre: str, apellido: str):
    """
    Descripción: Muestra la advertencia de confirmación para iniciar
    la partida. Si el usuario confirma, da inicio al ciclo de juego
    pasándole el tablero generado.
    Parámetros:
        tablero: Lista de enteros que representa las casillas.
    """
    mostrar_comenzar()
    opcion = validar_numero_rango(
        1,
        2,
        "Ingresa una opcion: ",
        "Error,ingresa una opcion valida: ",
    )
    if opcion == 1:
        ejecutar_partida(tablero, nombre, apellido)
    else:
        cartel("Volver al menu")


def mostrar_menu_juego() -> None:
    """
    Descripción: Muestra en consola las opciones del menú de juego
                 acumulando el texto en una variable antes de imprimir.
    """
    mensaje = "\n"
    mensaje += "╔════════════════════════════════════════╗\n"
    mensaje += "║           JUEGO DE LA VIDA             ║\n"
    mensaje += "╠════════════════════════════════════════╣\n"
    mensaje += "║  ∧＿∧      [1]  Partida rápida         ║\n"
    mensaje += "║ (´･ω･)     [2]  Partida larga          ║\n"
    mensaje += "║ /ヽ)ヽ)    [3]  Partida personalizada  ║\n"
    mensaje += "║(￣￣￣￣)  [4]  Ranking                ║\n"
    mensaje += "║日 []￣￣[] [5]  Salir                  ║\n"
    mensaje += "║                                        ║\n"
    mensaje += "╚════════════════════════════════════════╝\n"
    print(mensaje)


def mostrar_comenzar() -> None:
    """
    Descripción: Muestra las opciones para iniciar o regresar junto con
    una advertencia de confirmación acumulando todo en una variable.
    """
    mensaje = "¿Estás seguro que quieres comenzar?\n"
    mensaje += "1. Comenzar\n"
    mensaje += "2. Volver al menú\n"
    print(mensaje)




