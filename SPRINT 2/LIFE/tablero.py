import random
from LIFE.validaciones import validar_numero_rango


def crear_tablero_vacio(cantidad: int) -> list:
    """
    Descripción: Crea una lista que representa un tablero de juego con una
    cantidad determinada de casilleros inicializados en 0.
    Parámetros:
        cantidad: La cantidad de casilleros que tendrá la lista.
    Retorno: Una lista con la longitud indicada llena de ceros.
    """
    casilleros = []
    
    if cantidad > 0:
        casilleros = [0] * cantidad
    return casilleros


def asignar_casilleros_evento(
    tablero: list, cantidad: int, valor_evento: int
) -> None:
    """
    Descripción: Recorre el tablero y asigna un valor de evento específico
    en posiciones aleatorias, pisando únicamente los casilleros que estén en 0.
    Parámetros:
        tablero: Lista que representa las casillas del juego.
        cantidad: Cuántos casilleros se van a ocupar con este evento.
        valor_evento: El número que representa el evento.
    """
    casilleros_ocupados = 0
    while casilleros_ocupados < cantidad:
        indice_aleatorio = random.randint(0, len(tablero) - 1)
        if tablero[indice_aleatorio] == 0:
            tablero[indice_aleatorio] = valor_evento
            casilleros_ocupados += 1


def generar_tablero(
    partida: str,
    cantidad: int,
    preguntas: int,
    bonificacion: int,
    impuesto: int,
) -> list:
    """
    Descripción: Crea el tablero base, asigna de forma aleatoria los
    casilleros especiales calculando los neutros sobrantes y muestra
    la información final de la configuración de la partida.
    Parámetros:
        partida: Cadena de texto con el tipo de juego ("Rapida", "Larga").
        cantidad: Entero con la cantidad total de casilleros del mapa.
        preguntas: Cantidad de casilleros destinados a preguntas.
        bonificacion: Cantidad de casilleros destinados a sumas de puntos.
        impuesto: Cantidad de casilleros destinados a restas de puntos.
    Retorno: Lista de enteros que representa el tablero completo y cargado.
    """
    tablero = crear_tablero_vacio(cantidad)
    asignar_casilleros_evento(tablero, preguntas, 1)
    asignar_casilleros_evento(tablero, bonificacion, 2)
    asignar_casilleros_evento(tablero, impuesto, 3)

    neutro = cantidad - (preguntas + bonificacion + impuesto)
    mostrar_informacion_partida(partida, cantidad, preguntas, bonificacion, impuesto, neutro)
    return tablero


def ejecutar_partida_rapida():
    """
    Descripción: Inicializa los parámetros de una partida rápida
    y delega la construcción del tablero y reporte a la función genérica.
    Retorno: Lista de enteros que representa el tablero rápido cargado.
    """
    tablero_completo = generar_tablero("Rapida", 20, 5, 5, 5)
    return tablero_completo


def ejecutar_partida_larga():
    """
    Descripción: Inicializa los parámetros de una partida larga
    y delega la construcción del tablero y reporte a la función genérica.
    Retorno: Lista de enteros que representa el tablero largo cargado.
    """
    tablero_completo = generar_tablero("Larga", 50, 20, 10, 10)
    return tablero_completo


def ejecutar_partida_personalizada():
    """
    Descripción: Solicita al usuario la configuración interactiva de los
    casilleros validando dinámicamente los topes para que no se superen.
    Retorno: Lista de enteros que representa el tablero personalizado.
    """
    cantidad = validar_numero_rango(
        10,
        100,
        "Ingresa cuantos casilleros tendra la partida: \n",
        "Error, casilleros fuera de rango: \n",
    )

    casilleros_libres = cantidad
    preguntas = validar_numero_rango(
        0,
        casilleros_libres,
        "Cuántos casilleros de preguntas ❔: \n",
        "Error, casilleros fuera de rango: \n",
    )
    casilleros_libres -= preguntas

    bonificacion = validar_numero_rango(
        0,
        casilleros_libres,
        "¿Cuántos casilleros de bonificacion 🟩 : \n",
        "Error, casilleros fuera de rango: \n",
    )
    casilleros_libres -= bonificacion

    impuesto = validar_numero_rango(
        0,
        casilleros_libres,
        "¿Cuántos casilleros de impuestos 🟥 : \n",
        "Error, casilleros fuera de rango: \n",
    )

    tablero_generado = generar_tablero(
        "Personalizada", cantidad, preguntas, bonificacion, impuesto
    )
    return tablero_generado


def mostrar_informacion_partida(
    partida: str,
    cantidad: int,
    preguntas: int,
    bonificacion: int,
    impuesto: int,
    neutro: int
) -> None:
    """
    Descripción: Muestra en consola el desglose completo de la configuración
                 de la partida.
    Parámetros:
        partida: Tipo de partida ("Rapida", "Larga", "Personalizada").
        cantidad: Total de casilleros del tablero.
        preguntas: Cantidad de casilleros destinados a preguntas.
        bonificacion: Cantidad de casilleros destinados a bonificación.
        impuesto: Cantidad de casilleros destinados a impuesto.
        neutro: Cantidad de casilleros neutros.
    """
    print()
    print("=========================================")
    print("        INFORMACIÓN DE LA PARTIDA")
    print("=========================================")
    print(f"  Partida: {partida}")
    print(f"  Casilleros totales: {cantidad}")
    print(f"  ❔ Pregunta: {preguntas}")
    print(f"  🟩 Bonificación: {bonificacion}")
    print(f"  🟥 Impuesto: {impuesto}")
    print(f"  🟪 Neutro: {neutro}")
    print("=========================================")
    print()