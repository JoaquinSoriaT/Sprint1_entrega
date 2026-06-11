import random
from LIFE.eventos import gestionar_eventos, validar_evento_preguntas
from LIFE.validaciones import validar_numero_rango, cartel
from LIFE.final import mostrar_pantalla_abandono, mostrar_pantalla_victoria, mostrar_pantalla_derrota
from LIFE.ranking import guardar_puntaje
from LIFE.mapa_visual import mostrar_mapa


def ejecutar_partida(tablero: list, nombre: str, apellido: str) -> None:
    """
    Descripción: Controla el bucle principal de la partida, gestiona los
                 turnos, las tiradas de dado y las condiciones de final.
    Parámetros:
        tablero: Lista que representa el mapa del juego.
    """
    casillero = 0
    puntos = 10000
    correctas = 0
    falladas = 0
    turno_actual = 1
    abandono = False

    while casillero < len(tablero) and puntos > 0:
        mostrar_interfaz_turno(casillero, puntos, correctas, falladas)

        opcion = validar_numero_rango(
            1, 2, "Ingresa una opción: ",
            "Error, ingresa una opción válida: "
        )
        if opcion == 1:
            resultado_turno = tener_turno(
                casillero, tablero, turno_actual
            )
            estado = actualizar_estado_jugador(
                resultado_turno, tablero, puntos,
                correctas, falladas
            )
            casillero = estado[0]
            puntos = estado[1]
            correctas = estado[2]
            falladas = estado[3]
            turno_actual += 1
            
        else:
            cartel("Abandonaste la partida")
            abandono = True
            break

    ejecutar_final(puntos, abandono, correctas, falladas, nombre, apellido)


def lanzar_dado() -> list:
    """
    Descripción: Genera un número aleatorio del 1 al 6 y obtiene su diseño
                 en arte ASCII de un dado.
    Retorno: Una lista con el formato [entero_dado, tupla_lineas_arte].
    """
    dado = random.randint(1, 6)
    arte_dado = mostrar_dado()
    arte_seleccionado = arte_dado[dado]
    resultado_lanzamiento = [dado, arte_seleccionado]
    return resultado_lanzamiento


def actualizar_casillero(casillero_actual: int, tablero: list) -> list:
    """
    Descripción: Invoca el lanzamiento visual del dado, calcula la nueva
                 posición del jugador sumando el resultado obtenido y
                 valida que no se exceda el límite físico del tablero.
    Parámetros:
        casillero_actual: Entero con la posición antes de tirar.
        tablero: Lista que representa el mapa del juego.
    Retorno: Una lista con el formato [nuevo_casillero, dado, arte].
    """
    lanzamiento = lanzar_dado()
    dado = lanzamiento[0]
    arte_seleccionado = lanzamiento[1]

    nuevo_casillero = casillero_actual + dado
    if nuevo_casillero > len(tablero):
        nuevo_casillero = len(tablero)

    datos_movimiento = [nuevo_casillero, dado, arte_seleccionado]
    return datos_movimiento


def determinar_evento(nuevo_casillero: int, tablero: list,nombres: list,mensaje_final:str) -> list:
    """
    Descripción: Determina el tipo de evento y su nombre correspondiente
                 según la posición actual en el tablero.
    Parámetros:
        nuevo_casillero: Posición obtenida después de avanzar.
        tablero: Lista que representa el mapa del juego.
        nombres: Lista con los nombres de los eventos.
        mensaje_final: Mensaje cuando se alcanza la meta.
    Retorno: Una lista con el formato [tipo_evento, nombre_evento].
    """
    if nuevo_casillero < len(tablero):
        tipo_evento = tablero[nuevo_casillero]
        nombre_evento = nombres[tipo_evento]
    else:
        tipo_evento = 0
        nombre_evento = mensaje_final

    return [tipo_evento, nombre_evento]


def tener_turno(
    casillero_actual: int, tablero: list, numero_turno: int
) -> list:
    """
    Descripción: Coordina el flujo completo del turno: calcula el
                 movimiento, obtiene el evento, lo muestra en la caja
                 y devuelve el resultado del turno.
    Parámetros:
        casillero_actual: Posición actual del jugador.
        tablero: Lista que representa el mapa del juego.
        numero_turno: Número del turno actual.
    Retorno: Una lista con [nuevo_casillero, puntaje].
    """
    datos_movimiento = actualizar_casillero(casillero_actual, tablero)
    nuevo_casillero = datos_movimiento[0]
    dado = datos_movimiento[1]
    arte = datos_movimiento[2]

    nombres = ["Desafio", "Pregunta", "Bonificación", "Impuesto"]
    mensaje_final = "Meta Alcanzada"
    datos_evento = determinar_evento(nuevo_casillero, tablero,nombres,mensaje_final)
    tipo_evento = datos_evento[0]
    nombre_evento = datos_evento[1]

    mostrar_turno(numero_turno, arte, dado, nuevo_casillero, nombre_evento)
    mostrar_mapa(tablero,nuevo_casillero)

    if nuevo_casillero < len(tablero):
        puntaje = gestionar_eventos(tipo_evento)
        resultado_turno = [nuevo_casillero, puntaje]
    else:
        resultado_turno = [nuevo_casillero, 0]

    return resultado_turno


def actualizar_estado_jugador(
    resultado_turno: list, tablero: list, puntos_actuales: int,
    correctas: int, falladas: int
) -> list:
    """
    Descripción: Procesa el resultado del turno impactando la nueva
                 posición, acumulando los puntos obtenidos y
                 actualizando las estadísticas.
    Parámetros:
        resultado_turno: Lista con [nuevo_casillero, puntaje_turno].
        tablero: Lista que representa el mapa del juego.
        puntos_actuales: Puntos antes del turno.
        correctas: Cantidad de respuestas correctas hasta el momento.
        falladas: Cantidad de respuestas falladas hasta el momento.
    Retorno: Lista con [nuevo_casillero, nuevos_puntos,
             nuevas_correctas, nuevas_falladas].
    """
    nuevo_casillero = resultado_turno[0]
    puntos_turno = resultado_turno[1]
    nuevos_puntos = puntos_actuales + puntos_turno

    nuevas_correctas = validar_evento_preguntas(
        resultado_turno, tablero, correctas, True
    )
    nuevas_falladas = validar_evento_preguntas(
        resultado_turno, tablero, falladas, False
    )

    nuevo_estado = [
        nuevo_casillero, nuevos_puntos,
        nuevas_correctas, nuevas_falladas
    ]
    return nuevo_estado


def ejecutar_final(
    puntos: int, abandono: bool, correctas: int, falladas: int,nombre: str, apellido: str
) -> None:
    """
    Descripción: Analiza el estado del jugador al terminar el ciclo de
                 juego e invoca la pantalla correspondiente.
    Parámetros:
        puntos: Puntaje final del jugador.
        abandono: True si el jugador abandonó, False en caso contrario.
        correctas: Cantidad de respuestas correctas.
        falladas: Cantidad de respuestas falladas.
        nombre: nombre de usuario
        apellido: apellido de usuario
    """
    if puntos <= 0:
        mostrar_pantalla_derrota(puntos)
    elif abandono is True:
        mostrar_pantalla_abandono("Abandona la partida")
    else:
        mostrar_pantalla_victoria(puntos, correctas, falladas)
        guardar_puntaje(nombre, apellido, puntos)


def mostrar_interfaz_turno(
    casillero_actual: int,
    puntos: int,
    correctas: int,
    falladas: int
) -> None:
    """
    Descripción: Muestra la pantalla de juego dividida a la mitad;
                 el lado izquierdo expone las estadísticas actuales
                 y el derecho las opciones.
    Parámetros:
        casillero_actual: Posición actual del jugador.
        puntos: Puntaje acumulado.
        correctas: Cantidad de preguntas respondidas correctamente.
        falladas: Cantidad de preguntas respondidas incorrectamente.
    """
    mensaje = "=" * 65 + "\n"
    mensaje += "                     TURNO DEL JUGADOR                     \n"
    mensaje += "=" * 65 + "\n"
    mensaje += f" Casillero Actual: {casillero_actual:<5} |  1. Tirar dado\n"
    mensaje += f" Puntos Totales: {puntos:<7} |  2. Salir de la partida\n"
    mensaje += f" Preguntas Correctas: {correctas:<2} |\n"
    mensaje += f" Preguntas Falladas: {falladas:<3} |\n"
    mensaje += "=" * 65

    print(mensaje)
    print()


def mostrar_turno(
    numero_turno: int, arte: tuple, dado: int,
    nuevo_casillero: int, nombre_evento: str
) -> None:
    """
    Descripción: Renderiza la estructura visual de la caja de novedades
                 con el dado y la información del turno.
    Parámetros:
        numero_turno: Número del turno actual.
        arte: Tupla con las líneas del dado ASCII.
        dado: Valor obtenido en el dado.
        nuevo_casillero: Nueva posición del jugador.
        nombre_evento: Nombre del evento del casillero.
    """
    texto_titulo = f"TURNO {numero_turno}"
    texto_sacaste = f"  Sacaste: {dado}"
    texto_avanzas = f"  Avanzás al casillero: {nuevo_casillero}"
    texto_evento = f"  Evento: {nombre_evento}"

    print("\n┌────────────────────────────────────────────────────────┐")
    print(f"│{texto_titulo:^56}│")
    print("├───────────────────────┬────────────────────────────────┤")
    print(f"│      {arte[0]}      │{texto_sacaste:<32}│")
    print(f"│      {arte[1]}      │{texto_avanzas:<32}│")
    print(f"│      {arte[2]}      │{texto_evento:<32}│")
    print(f"│      {arte[3]}      │                                │")
    print(f"│      {arte[4]}      │                                │")
    print("└───────────────────────┴────────────────────────────────┘")
    print()
    input(" Presione ENTER para continuar ")
    print()


def mostrar_dado() -> dict:
    """
    Descripción: Retorna un diccionario con los diseños ASCII de cada
                 cara del dado.
    Retorno: Diccionario con arte ASCII para valores del 1 al 6.
    """
    arte_dado = {
        1: (
            "┌─────────┐",
            "│         │",
            "│    ●    │",
            "│         │",
            "└─────────┘"
        ),
        2: (
            "┌─────────┐",
            "│  ●      │",
            "│         │",
            "│      ●  │",
            "└─────────┘"
        ),
        3: (
            "┌─────────┐",
            "│  ●      │",
            "│    ●    │",
            "│      ●  │",
            "└─────────┘"
        ),
        4: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│         │",
            "│  ●   ●  │",
            "└─────────┘"
        ),
        5: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│    ●    │",
            "│  ●   ●  │",
            "└─────────┘"
        ),
        6: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "└─────────┘"
        )
    }
    return arte_dado

