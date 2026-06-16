import random

PALABRAS = [
    "python", "programacion", "computadora", "teclado", "monitor",
    "algoritmo", "variable", "funcion", "bucle", "lista",
    "diccionario", "modulo", "clase", "objeto", "herencia",
    "elefante", "jirafa", "cocodrilo", "mariposa", "pingüino",
    "aventura", "misterio", "fantasia", "universo", "galaxia"
]

AHORCADO = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""
]

MAX_ERRORES = len(AHORCADO) - 1


def limpiar_pantalla()-> None:
    """
    Limpia la pantalla imprimiendo varias líneas en blanco.
    """
    print("\n" * 3)

def mostrar_letras(lista: list, mensaje_vacio: str) -> str:
    """
    Convierte una lista de letras usadas en una cadena legible 
    para mostrar al usuario. 
    Si la lista está vacía, muestra un mensaje indicando que no 
    se han usado letras.
    Parámetros:
        lista: Lista de letras usadas.
        mensaje_vacio: Mensaje a mostrar si la lista está vacía.
    Retorno: Cadena con las letras usadas o el mensaje de vacío.
    
    """
    if len(lista) == 0:
        mensaje = mensaje_vacio
    else:
        mensaje = ", ".join(lista)
    return mensaje

def mostrar_estado(palabra_oculta: list, letras_usadas: list, errores: int) -> None:
    """
    Muestra el estado actual del juego, incluyendo el dibujo del ahorcado,
    la palabra oculta, las letras usadas y el número de errores.
    Parámetros:
        palabra_oculta: Lista de caracteres que representa la palabra oculta 
        con guiones bajos.
        letras_usadas: Lista de letras que el jugador ha usado hasta el momento.
        errores: Número de errores cometidos por el jugador.
    """
    print(AHORCADO[errores])
    print(f"\nPalabra: {' '.join(palabra_oculta)}")
    print(f"Letras usadas: {mostrar_letras(letras_usadas, 'Ninguna')}")
    print(f"Errores: {errores}/{MAX_ERRORES}")

def validar_letra(string: str)-> bool:
    """
    Valida que el input del usuario sea una letra minúscula del alfabeto.
    Parámetros:
        string: Cadena ingresada por el usuario.
    Retorno: True si la cadena es una letra válida, False en caso contrario.
    """
    if len(string) == 1 and (string >= "a" and string <= "z"):
        return True
    return False


def jugar_ahorcado() -> bool:
    """
    Función principal que ejecuta el juego del ahorcado. Selecciona una palabra
    aleatoria, inicializa el estado del juego y maneja el ciclo de juego hasta que
    el jugador gane o pierda.
    Retorno: True si el jugador gana, False si pierde.
    """
    palabra = random.choice(PALABRAS)
    palabra_oculta = ["_"] * len(palabra)
    letras_usadas = list()
    errores = 0

    print("========================================" +
    "\n       ¡BIENVENIDO AL AHORCADO!" +
    "\n========================================")

    while errores < MAX_ERRORES:
        limpiar_pantalla()
        mostrar_estado(palabra_oculta, letras_usadas, errores)

        letra = input("\nIngresá una letra: ").lower()

        while validar_letra(letra) == False or letra in letras_usadas:
            letra = input("Ingresá una letra válida que no hayas usado: ").lower()

        if letra not in palabra:
            letras_usadas.append(letra)

        if letra in palabra:
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    palabra_oculta[i] = letra
            print(f"¡Bien! La letra '{letra}' está en la palabra.")
        else:
            errores += 1
            print(f"La letra '{letra}' no está en la palabra.")

        if "_" not in palabra_oculta:
            limpiar_pantalla()
            mostrar_estado(palabra_oculta, letras_usadas, errores)
            print("\n¡GANASTE! La palabra era:", palabra.upper())
            return True

    limpiar_pantalla()
    mostrar_estado(["*"] * len(palabra), letras_usadas, errores)
    print(f"\n¡PERDISTE! La palabra era: {palabra.upper()}")
    return False


def ejecutar_ahorcado()-> int:
    """
    Función principal que inicia el juego del ahorcado y maneja la opción 
    de jugar de nuevo.
    Retorno: El puntaje final del jugador.
    """
    bandera = True
    puntaje = 0
    while bandera == True:
        victoria = jugar_ahorcado()
        if victoria:
            puntaje += 1
        print(f"\nPuntaje actual: {puntaje}")
        otra = input("\n¿Querés jugar de nuevo? (s/n): ").strip().lower()
        if otra != "s":
            print("\n¡Hasta la próxima! 👋\n")
            bandera = False
            return puntaje