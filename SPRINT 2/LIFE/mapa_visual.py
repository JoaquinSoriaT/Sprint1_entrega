def obtener_arte_casilleros(tipo_evento: int) -> str:
    """
    Descripción: Retorna el arte correspondiente según el tipo de casillero.
    Parámetros:
        tipo_evento: 0=desafio, 1=pregunta, 2=bonificacion, 3=impuesto.
    Retorno: arte como string.
    """
    if tipo_evento == 0:
        cuadrado = "🟪"
    elif tipo_evento == 1:
        cuadrado = "❔"
    elif tipo_evento == 2:
        cuadrado = "🟩"
    elif tipo_evento == 3:
        cuadrado = "🟥"
    else:
        cuadrado = "🟪"
    return cuadrado


def dividir_tablero_en_filas(tablero: list, tamaño_fila: int = 15) -> list:
    """
    Descripción: Divide el tablero en sublistas de tamaño_fila elementos.
    Parámetros:
        tablero: Lista completa de casilleros.
        tamaño_fila: Cantidad de casilleros por fila (default 15).
    Retorno: Lista de listas (filas).
    """
    mapa = []
    i = 0
    while i < len(tablero):
        fila = []
        for j in range(tamaño_fila):
            if i >= len(tablero):
                break
            fila.append(tablero[i])
            i += 1
        mapa.append(fila)
    return mapa


def actualizar_posicion_en_fila(fila: list, inicio_fila: int, posicion: int) -> str:
    """
    Descripción: Convierte una fila de casilleros en emojis,
                 reemplazando la posición del jugador por 📍.
    Parámetros:
        fila: Sublista de casilleros.
        inicio_fila: Índice del primer casillero de esta fila.
        posicion: Índice actual del jugador.
    Retorno:  strings con emoji separado por espacio.
    """
    visual = ""
    for i in range(len(fila)):
        if inicio_fila + i  == posicion:
            visual = visual + "🔽 "
        else:
            arte = obtener_arte_casilleros(fila[i])
            visual = visual + arte + " "
    return visual



def generar_mapa(tablero: list, posicion: int) -> list:
    """
    Descripción: Genera la lista de líneas del mapa completo.
    Parámetros:
        tablero: Lista completa de casilleros.
        posicion: Índice actual del jugador.
    Retorno: Lista de strings con cada línea del mapa.
    """
    filas = dividir_tablero_en_filas(tablero, 15)
    mapa = []
    inicio_fila = 0
    for i in range(len(filas)):
        visual = actualizar_posicion_en_fila(filas[i], inicio_fila, posicion)
        mapa.append(visual)
        inicio_fila = inicio_fila + len(filas[i])
    return mapa


def mostrar_mapa(tablero: list, casillero: int):
    lineas = generar_mapa(tablero, casillero)

    print("┌─────────────────────────────────────────────┐")
    print("│            Mapa del tablero                 │")
    print("└─────────────────────────────────────────────┘")
    print()

    for linea in lineas:
        print(" " + linea)
        
    print()
    print("┌─────────────────────────────────────────────┐")
    print("│                 Evento                      │")
    print("├─────────────────────────────────────────────┤")
    print("│  🟪 = Desafío     ( ± 3000 puntos )         │")
    print("│  ❔ = Pregunta    ( ± 5000 puntos )         │")
    print("│  🟩 = Bonificación ( + 3000 puntos )        │")
    print("│  🟥 = Impuesto    ( - 3000 puntos )         │")
    print("│  🔽 = Tu posición actual                    │")
    print("└─────────────────────────────────────────────┘")
    print()
    input("Presione ENTER para continuar")
    print()

