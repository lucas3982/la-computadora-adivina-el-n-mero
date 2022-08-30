#la computadora va adivinar el número

import random


def adivina_el_número_computadora(x):
    print("Bienvenido(a) al juego, que lo disfruten!!")

    print(f"Selecciona un número entre 1 y {x} para que la computadora lo adivine...")

    limite_inferior =1
    limite_superior = x

    respuesta =""
    while respuesta != "c":
        #generar una predicción
        if limite_inferior != limite_superior: #[1, 10]
            predicción = random.randint(limite_inferior, limite_superior)
        else:
            predicción = limite_inferior #tambien podria ser limite superior

        #obtener una respuesta del usuario

        respuesta = input(f"Mi predicción es {predicción}. Si es muy alta, ingresa (A). Si es muy baja, ingresa (B). Si es correcto, ingresa (C)").lower()

        if respuesta == "a":
            limite_superior = predicción -1

        elif respuesta == "b":
            limite_inferior = predicción +1

    print(f"Sii, la computadora adivinó tu número: {predicción}")    

adivina_el_número_computadora(10)

    