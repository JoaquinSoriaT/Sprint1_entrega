import random
from LIFE.validaciones import validar_respuesta_pregunta
from LIFE.preguntas import preguntas
from LIFE.historia import eventos_bonificacion, eventos_impuesto, eventos_neutro

def gestionar_eventos(casillero: int) -> int:
    """
    Descripción: Ejecuta el evento correspondiente según el tipo de casillero.
    Parámetros:
        casillero: Número entero que representa el tipo de evento.
    Retorno: Balance de puntos obtenidos o perdidos.
    """
    if casillero == 1:
        balance = ejecutar_evento_pregunta()
    elif casillero == 2:
        evento = random.choice(eventos_bonificacion)
        balance = mostrar_evento(3000, "¡BONIFICACIÓN!", evento)        
    elif casillero == 3:
        evento = random.choice(eventos_impuesto)
        balance = mostrar_evento(-3000, "¡IMPUESTO!", evento)
    else:
        balance = asignar_puntos_desafio(3000)
    return balance


def asignar_puntos_desafio(puntos_suma: int) -> int:
    """
    Descripción: Asigna los puntos y muestra el cartel del evento desafío.
                 Cara = gana puntos_suma.
                 Cruz = pierde puntos_suma.
    Parámetros:
        puntos_suma: Cantidad de puntos en juego.
    Retorno: Balance de puntos (puntos_suma o -puntos_suma).
    """
    mostrar_desafio()
    print()
    input(" Presione ENTER para tirar la moneda ")
    print()
    balance = 0
    moneda = random.choice(["cara", "cruz"])
    if moneda == "cara":
        balance += puntos_suma
        mostrar_evento(balance,"Desafio", "Cara")
    else:
        balance -= puntos_suma
        mostrar_evento(balance, "Desafio", "Cruz")
    return balance




def validar_evento_preguntas(
    resultados: list, tablero: list, contador: int, correcta: bool
) -> int:
    """
    Descripción: Analiza el resultado del turno y el tablero para determinar
                 si corresponde incrementar el contador de estadísticas.
    Parámetros:
        resultados: Lista con [casillero, puntos_obtenidos].
        tablero: Lista que representa el mapa del juego.
        contador: Contador actual (correctas o falladas).
        correcta: True si se cuentan aciertos, False para errores.
    Retorno: El contador de estadística actualizado.
    """
    puntos = resultados[1]
    casillero = resultados[0]

    if casillero < len(tablero) and tablero[casillero] == 1:
        if correcta is True and puntos > 0:
            contador += 1
        elif correcta is False and puntos < 0:
            contador += 1
    return contador


def ejecutar_evento_pregunta() -> int:
    """
    Descripción: Selecciona una pregunta aleatoria, invoca su impresión,
                 valida la respuesta del usuario y computa el balance
                 de puntos.
    Retorno: Balance de puntos ganados o perdidos en la pregunta.
    """
    pregunta = random.choice(preguntas)
    mostrar_pregunta_en_pantalla(pregunta)

    respuesta = validar_respuesta_pregunta()
    balance = calcular_balance_pregunta(respuesta, pregunta)
    return balance


def calcular_balance_pregunta(respuesta: str, pregunta: dict) -> int:
    """
    Descripción: Evalúa si la respuesta es correcta y retorna el balance
                 correspondiente, mostrando el cartel adecuado.
    Parámetros:
        respuesta: Letra elegida por el usuario (a, b o c).
        pregunta: Diccionario con los datos de la pregunta.
    Retorno: Balance de puntos (5000 o -5000).
    """
    if respuesta == pregunta["respuesta_correcta"]:
        puntos = 5000
        cartel_respuesta_correcta(puntos)
    else:
        respuesta_correcta = pregunta[
            f"respuesta_{pregunta['respuesta_correcta']}"
        ]
        puntos = -5000
        cartel_respuesta_incorrecta(puntos, respuesta_correcta)
    return puntos


def mostrar_evento(puntos:int, titulo:str, evento:str) -> int:
    """
    Descripción: Muestra un cartel genérico para eventos.
    Parámetros:
        puntos: Cantidad de puntos (positivo, negativo o cero).
        titulo: Título del evento.
        evento: Texto descriptivo del evento.
    Retorno: Los mismos puntos recibidos.
    """
    if puntos >= 0:
        signo = ("+") 
    else:
        signo = ("")
    print("╔════════════════════════════════════════╗")
    print(f"                {titulo}                 ")
    print(f"{evento:^38}                ")
    print(f"{f'{signo} {puntos} puntos':^38}               ")
    print("╚════════════════════════════════════════╝")
    print()
    return puntos


def mostrar_desafio() -> None:
    """
    Descripción: Muestra el cartel explicativo del casillero Desafío.
    """
    print("┌────────────────────────────────────────────────────────────────────────────────────┐")
    print("│                ______________                   │  🎲 EVENTO DESAFÍO 🎲            │")
    print("│    __,.,---'''''              '''''---..._      │                                  │")
    print("│ ,-'             .....:::''::.:            '`-.  │  Tirarás una moneda:             │")
    print("│'           ...:::.....       '                │ │                                  │")
    print("││           ''':::'''''       .               ,  │  • CARA  → + 3000 puntos         │")
    print("│|'-.._           ''''':::..::':          __,,-   │  • CRUZ  → - 3000 puntos         │")
    print("│ '-.._''`---.....______________.....---''__,,-   │                                  │")
    print("│      ''`---.....______________.....---''        │                                  │")
    print("└────────────────────────────────────────────────────────────────────────────────────┘")


def mostrar_pregunta_en_pantalla(pregunta_dict: dict) -> None:
    """
    Descripción: Recibe un diccionario de pregunta y muestra en consola
                 su enunciado junto con las opciones de respuesta
                 bien formateadas.
    Parámetros:
        pregunta_dict: Diccionario con la pregunta y sus opciones.
    """
    mensaje = "========================================\n"
    mensaje += "            CASILLERO PREGUNTA          \n"
    mensaje += "========================================\n"
    mensaje += f"{pregunta_dict['pregunta']}\n\n"
    mensaje += f"a) {pregunta_dict['respuesta_a']}\n"
    mensaje += f"b) {pregunta_dict['respuesta_b']}\n"
    mensaje += f"c) {pregunta_dict['respuesta_c']}\n"
    mensaje += "========================================="
    print(mensaje)


def cartel_respuesta_correcta(puntos: int) -> None:
    """
    Descripción: Muestra un cartel elegante para respuestas correctas.
    Parámetros:
        puntos: Cantidad de puntos ganados.
    """
    mensaje = "\n"
    mensaje += "╔════════════════════════════════════════╗\n"
    mensaje += "       ✅ RESPUESTA CORRECTA             \n"
    mensaje += f"            + {puntos} puntos              \n"
    mensaje += "╚════════════════════════════════════════╝\n"
    print(mensaje)


def cartel_respuesta_incorrecta(puntos: int, respuesta_correcta: str) -> None:
    """
    Descripción: Muestra un cartel elegante para respuestas incorrectas.
    Parámetros:
        puntos: Cantidad de puntos perdidos.
        respuesta_correcta: Texto de la respuesta correcta.
    """
    mensaje = "\n"
    mensaje += "╔════════════════════════════════════════╗\n"
    mensaje += "      ❌ RESPUESTA INCORRECTA            \n"
    mensaje += f"           {puntos} puntos                 \n"
    mensaje += "╠════════════════════════════════════════╣\n"
    mensaje += "        Respuesta correcta:              \n"
    mensaje += f"           \"{respuesta_correcta}\"      \n"
    mensaje += "╚════════════════════════════════════════╝\n"
    print(mensaje)