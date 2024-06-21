import random

opciones = ["piedra", "papel", "tijeras"]

def obtener_eleccion_usuario():
    while True:
        eleccion = input("Elige piedra, papel o tijeras: ").lower()
        if eleccion in opciones:
            return eleccion
        else:
            print("Eleccion no valida. Intenta de nuevo.")

def obtener_eleccion_computadora():
    return random.choice(opciones)

def determinar_ganador(eleccion_usuario, eleccion_computadora):
    if eleccion_usuario == eleccion_computadora:
        return "Empate"
    elif (eleccion_usuario == "piedra" and eleccion_computadora == "tijeras") or \
        (eleccion_usuario == "papel" and eleccion_computadora == "piedra") or \
        (eleccion_usuario == "tijeras" and eleccion_computadora == "papel"):
        return "¡Ganaste!"
    else:
        return "¡La computadora gana!"

def jugar_piedra_papel_tijeras():
    print("¡Bienvenido a piedra, papel o tijeras!")
    while True:
        eleccion_usuario = obtener_eleccion_usuario()
        eleccion_computadora = obtener_eleccion_computadora()
        print(f"Tú elegiste: {eleccion_usuario}")
        print(f"La computadora eligió: {eleccion_computadora}")
        resultado = determinar_ganador(eleccion_usuario, eleccion_computadora)
        print(resultado)
        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ")
        if jugar_de_nuevo.lower() != "s":
            break
    print("¡Gracias por jugar!")

# Iniciar el juego
jugar_piedra_papel_tijeras()
