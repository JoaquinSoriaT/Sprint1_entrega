def mostrar_pantalla_abandono(mensaje: str) -> None:
    """
    Descripción: Muestra el texto de abandono y el arte ASCII del
                 monigote corriendo debajo de forma prolija.
    """
    print("\n")
    print("=========================================")
    print(f"           {mensaje}            ")
    print("=========================================")
    print("     __O   ")
    print("    / /\\_, ")
    print("  ___/\\   ")
    print("      /   ")
    
    input(" Presione ENTER para salir ")


def mostrar_pantalla_victoria(puntos: int, correctas: int, falladas: int) -> None:
    """
    Descripción: Muestra el gatito ASCII festejando con los mensajes 
                 originales de victoria y el puntaje final.
    """
    gato_ascii = [
        "　　　　　  γ⌒ヽ",
        "　　　　__/　　/",
        "　   γ￣＿_） （　  Λ,,Λ",
        "　（ 　 ＿__）　）(´･ω ･`)",
        "　（　　＿__） ﾉ ﾍ　　　 |>",
        "　 乂＿__)_ノ　　  しー Ｊ"
    ]
    print("\n")
    for linea in gato_ascii:
        print("       " + linea)
    
    print("\n=======================================================")
    print("                  ¡FELICITACIONES!                     ")
    print("=======================================================")
    print(" Llegaste al casillero final de la meta.               ")
    print(f" Puntaje Final: {puntos} puntos.                      ")
    print(f" Preguntas acertadas: {correctas}.                      ")
    print(f" Preguntas falladas: {falladas}.                      ")
    print("=======================================================\n")
    
    input(" Presione ENTER para salir ")


def mostrar_pantalla_derrota(puntos: int) -> None:
    """
    Descripción: Muestra el gatito ASCII triste con los mensajes 
                 originales de derrota y el puntaje final.
    """
    gato_ascii = [
        "　 　/　　 /　　/　 /",
        "　 　＿n＿",
        "　 ／//|ヾ＼　/　/",
        "　   ⌒⌒|⌒⌒",
        "/　　  |∧_∧　/　 /",
        "　　　 |･ω･`)",
        "　/　 Oと　 )　/　/",
        "　　　 しーＪ｡｡｡｡｡"
    ]
    
    print("\n")
    for linea in gato_ascii:
        print("             " + linea)
    
    print("\n=======================================================")
    print("                     ¡GAME OVER!                        ")
    print("=======================================================")
    print(" No lograste llegar a la meta.                         ")
    print(f" Puntaje Final: {puntos} puntos.                      ")
    print("=======================================================\n")
    
    input(" Presione ENTER para salir ")