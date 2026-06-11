import os
from LIFE.validaciones import cartel


def obtener_ruta_csv() -> str:
    """Retorna la ruta completa del archivo score.csv dentro del paquete LIFE."""
    directorio = os.path.dirname(__file__)
    return os.path.join(directorio, "score.csv")
# os.getcwd()


def guardar_puntaje(nombre: str, apellido: str, puntaje: int) -> None:
    """
    Descripción: Guarda el puntaje del jugador en el archivo score.csv.
    Parámetros:
        nombre: Nombre del jugador.
        apellido: Apellido del jugador.
        puntaje: Puntaje obtenido en la partida.
    """
    ruta = obtener_ruta_csv()
    with open(ruta, "a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre},{apellido},{puntaje}\n")


def obtener_puntajes() -> list:
    """
    Descripción: Lee el archivo score.csv y extrae los datos.
    Retorno: Lista de listas [[nombre, apellido, puntaje], ...].
    """
    jugadores = []
    score_csv = obtener_ruta_csv()
    with open(score_csv, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.rstrip("\n")
            if len(linea) > 0:
                partes = linea.split(",")
                nombre = partes[0]
                apellido = partes[1]
                puntaje = int(partes[2])
                jugadores.append([nombre, apellido, puntaje])

    return jugadores


def ordenamiento_jugadores(jugadores: list) -> None:
    """
    Descripción: Ordena la lista de jugadores por puntaje de mayor a menor.
    Parámetros:
        jugadores: Lista de listas [[nombre, apellido, puntaje], ...].
    """
    for i in range(0, len(jugadores) - 1):
        for j in range(i + 1, len(jugadores)):
            if jugadores[i][2] < jugadores[j][2]:
                aux = jugadores[i]
                jugadores[i] = jugadores[j]
                jugadores[j] = aux


def rankear_jugadores(jugadores: list, limite: int) -> list:
    """
    Descripción: Genera las líneas del ranking con número, nombre, apellido
                 y puntaje.
    Parámetros:
        jugadores: Lista de listas [[nombre, apellido, puntaje], ...]
                   ordenada de mayor a menor.
        limite: Cantidad máxima de jugadores a mostrar.
    Retorno: Lista de strings con formato "número nombre apellido =
             puntaje puntos".
    """
    filas = []
    i = 0

    while i < len(jugadores) and i < limite:
        nombre = jugadores[i][0]
        apellido = jugadores[i][1]
        puntaje = jugadores[i][2]
        numero = f"{i + 1}. "

        fila = f"{numero:<3} {nombre} {apellido} = {puntaje} puntos"
        filas.append(fila)
        i += 1

    return filas


def ejecutar_ranking() -> None:
    """
    Descripción: Función principal que coordina la obtención, ordenamiento
                 y visualización del ranking.
    """
    jugadores = obtener_puntajes()

    if len(jugadores) > 0:
        ordenamiento_jugadores(jugadores)
        mostrar_ranking(jugadores)
    else:
        cartel("no hay puntajes")


def mostrar_medalla() -> None:
    """
    Descripción: Muestra el arte de la medalla (trofeo) dentro de un recuadro.
    """
    print("""
╔════════════════════════════════════╗
║                                    ║
║          _______________           ║
║         |@@@@|     |####|          ║
║         |@@@@|     |####|          ║
║         |@@@@|     |####|          ║
║         \@@@@|     |####/          ║
║          \@@@|     |###/           ║
║           `@@|_____|##'            ║
║                (O)                 ║
║             .-''''-.               ║
║           .'  * * *  `.            ║
║          :  *       *  :           ║
║         : ~  R A N K  ~ :          ║
║         : ~  L I F E  ~ :          ║
║          :  *       *  :           ║
║           `.  * * *  .'            ║
║             `-.....-'              ║
║                                    ║
╚════════════════════════════════════╝
    """)
    input("Presione ENTER para ver el ranking ")
    print()


def mostrar_ranking(personas: list) -> None:
    """
    Descripción: Muestra el ranking con el arte de la medalla y los
                 puntajes dentro de un recuadro.
    Parámetros:
        personas: Lista de listas [[nombre, apellido, puntaje], ...]
                  ordenada de mayor a menor.
    """
    rank = rankear_jugadores(personas, 15)
    mostrar_medalla()
    print("╔════════════════════════════════════════╗")

    for player in rank:
        print(f"║  {player:<37} ║")

    print("╚════════════════════════════════════════╝")
    print()
    input("Presione ENTER para salir")