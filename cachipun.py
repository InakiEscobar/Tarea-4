def piedra_papel_tijera():
    import random
    opciones = ["piedra", "papel", "tijera"]
    decision = input("Elije piedra, papel o tijera: ")
    computador = random.choice(opciones)
    print(f"La computadora eligió: {computador}")
    if decision == computador:
        return "Es un empate"
    elif (decision == "piedra" and computador == "tijeras") or \
         (decision == "tijeras" and computador == "papel") or \
         (decision == "papel" and computador == "piedra"):
        return "¡Ganaste!"
    else:
        return "Perdiste :("

resultado = piedra_papel_tijera()
print(resultado) 
