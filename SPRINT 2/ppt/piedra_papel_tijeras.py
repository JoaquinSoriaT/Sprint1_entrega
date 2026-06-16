
import random


#  ARTE ASCII PARA CADA OPCIÓN

ARTE = {
    "piedra": r"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    "papel": r"""   
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    "tijeras": r"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
}



#  DATOS DEL JUEGO  (lista de diccionarios)

OPCIONES = [
    {"id": "1", "nombre": "piedra",  "emoji": "🪨"},
    {"id": "2", "nombre": "papel",   "emoji": "📄"},
    {"id": "3", "nombre": "tijeras", "emoji": "✂️"},
]

# Reglas: clave GANA contra valor
REGLAS = {
    "piedra":  "tijeras",   # piedra gana a tijeras
    "papel":   "piedra",    # papel gana a piedra
    "tijeras": "papel",     # tijeras gana a papel
}

# Historial de rondas (lista de listas: [ronda, jugador, pc, resultado])
historial_partida = []



#  FUNCIONES AUXILIARES

def mostrar_menu_opciones() -> None:
    """Muestra el menú de elección al jugador."""
    print("\n  ¿Qué elegís?")
    for op in OPCIONES:
        print(f"    [{op['id']}] {op['nombre'].capitalize()} {op['emoji']}")
    print("    [0] Abandonar partida")


def obtener_eleccion_jugador() -> str | None:
    """
    Solicita y valida la elección del jugador.
    Retorna el nombre de la elección o None si quiere salir.
    """
    ids_validos = {op["id"]: op["nombre"] for op in OPCIONES}

    while True:
        mostrar_menu_opciones()
        entrada = input("\n Tu elección: ").strip()

        if entrada == "0":
            return None
        if entrada in ids_validos:
            return ids_validos[entrada]

        print(" Opción inválida. Ingresá 1, 2, 3 o 0 para salir.")


def eleccion_pc() -> str:
    """Devuelve una elección aleatoria de la PC."""
    return random.choice([op["nombre"] for op in OPCIONES])


def determinar_resultado(jugador: str, pc: str) -> str:
    """
    Compara las elecciones y retorna 'gana', 'pierde' o 'empate'.
    """
    if jugador == pc:
        return "empate"
    if REGLAS[jugador] == pc:
        return "gana"
    return "pierde"


def mostrar_ronda(ronda: int, jugador: str, pc: str, resultado: str) -> None:
    """Imprime el arte ASCII y el veredicto de la ronda."""
    print(f"\n{'─'*52}")
    print(f"  Ronda {ronda}")
    print(f"{'─'*52}")

    # Arte del jugador y la PC lado a lado (columnas simples)
    print(f"\n  TÚ elegiste: {jugador.upper()}")
    print(ARTE[jugador])
    print(f" PC eligió: {pc.upper()}")
    print(ARTE[pc])

    # Veredicto
    if resultado == "gana":
        print("¡GANASTE esta ronda!")
    elif resultado == "pierde":
        print("Perdiste esta ronda.")
    else:
        print("¡EMPATE!")


def mostrar_marcador(ganadas: int, perdidas: int, empates: int, ronda: int) -> None:
    """Muestra el marcador actual."""
    print(f"\n  📊 Marcador (luego de {ronda} ronda/s):")
    print(f"     ✅ Ganadas : {ganadas}")
    print(f"     ❌ Perdidas: {perdidas}")
    print(f"     🤝 Empates : {empates}")


def mostrar_historial(historial: list) -> None:
    """Muestra el historial de rondas en formato tabla."""
    if not historial:
        print("\n  No hay rondas registradas.")
        return

    print(f"\n  {'─'*54}")
    print(f"  {'Ronda':^6} | {'Tu elección':^12} | {'PC eligió':^12} | {'Resultado':^10}")
    print(f"  {'─'*54}")
    for fila in historial:
        ronda_n, jug, pc_e, res = fila
        res_str = {"gana": "✅ Ganaste", "pierde": "❌ Perdiste", "empate": "🤝 Empate"}[res]
        print(f"  {ronda_n:^6} | {jug.capitalize():^12} | {pc_e.capitalize():^12} | {res_str:^10}")
    print(f"  {'─'*54}")



#  FUNCIÓN PRINCIPAL DEL JUEGO

# Modificamos la firma de la función para recibir nombre y apellido
def jugar_piedra_papel_tijeras(nombre: str, apellido: str) -> int:
    """
    Módulo principal del juego Piedra, Papel y Tijeras.

    Parámetros
    ----------
    nombre : str
        Nombre del jugador actual.
    apellido : str
        Apellido del jugador actual.

    Retorna
    -------
    int
        Puntaje final = rondas ganadas por el jugador.
    """
    global historial_partida
    historial_partida = []

    print("\n" + "═"*54)
    print("   🪨 📄 ✂️   PIEDRA, PAPEL Y TIJERAS   ✂️ 📄 🪨")
    print("═"*54)

    # Combinamos el nombre completo para mostrarlo en el juego
    nombre_completo = f"{nombre} {apellido}"

    try:
        total_rondas_str = input(f"\n  ¡Hola, {nombre_completo}! ¿Cuántas rondas querés jugar? (1-20): ").strip()
        total_rondas = int(total_rondas_str)
        if not 1 <= total_rondas <= 20:
            raise ValueError
    except ValueError:
        print("  Valor inválido, se jugará a 5 rondas por defecto.")
        total_rondas = 5

    ganadas = perdidas = empates = 0
    ronda_actual = 0

    print(f"\n  ¡Empezamos! Vas a jugar {total_rondas} rondas.")
    print("  (En cualquier momento ingresá 0 para abandonar.)\n")

    for n_ronda in range(1, total_rondas + 1):
        ronda_actual = n_ronda
        print(f"\n  ── RONDA {n_ronda} de {total_rondas} ──")

        eleccion_jug = obtener_eleccion_jugador()

        # El jugador eligió abandonar
        if eleccion_jug is None:
            print(f"\n  👋 {nombre} abandonó la partida en la ronda {n_ronda}.")
            break

        eleccion_maquina = eleccion_pc()
        resultado = determinar_resultado(eleccion_jug, eleccion_maquina)

        # Actualizar contadores
        if resultado == "gana":
            ganadas += 1
        elif resultado == "pierde":
            perdidas += 1
        else:
            empates += 1

        # Guardar en historial
        historial_partida.append([n_ronda, eleccion_jug, eleccion_maquina, resultado])

        mostrar_ronda(n_ronda, eleccion_jug, eleccion_maquina, resultado)
        mostrar_marcador(ganadas, perdidas, empates, n_ronda)

    # ── Resultados finales ──
    print("\n" + "═"*54)
    print("            📋 RESULTADOS FINALES")
    print("═"*54)

    mostrar_historial(historial_partida)

    print(f"\n  Jugador : {nombre_completo}")
    print(f"  Rondas jugadas : {len(historial_partida)}")
    print(f"  ✅ Ganadas      : {ganadas}")
    print(f"  ❌ Perdidas     : {perdidas}")
    print(f"  🤝 Empates      : {empates}")

    # Mensaje final personalizado
    if ganadas > perdidas:
        print(f"\n  🏆 ¡Felicitaciones, {nombre}! Ganaste la partida.")
    elif perdidas > ganadas:
        print(f"\n  😞 La PC ganó esta vez, {nombre}. ¡Mejor suerte la próxima!")
    else:
        print(f"\n  🤝 ¡Empate total, {nombre}! Fue parejo.")

    puntaje_final = ganadas
    print(f"\n  🎯 Tu puntaje final (rondas ganadas): {puntaje_final}")
    print("═"*54 + "\n")

    return puntaje_final