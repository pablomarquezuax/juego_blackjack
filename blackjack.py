import random

# Diccionario "Cartas" que contiene el codigo de unicode de cada carta de la baraja de poker (excepto los jokers) 
cartas = { 
    chr(0x1F0B2): 2,
    chr(0x1F0B3): 3,
    chr(0x1F0B4): 4,
    chr(0x1F0B5): 5,
    chr(0x1F0B6): 6,
    chr(0x1F0B7): 7,
    chr(0x1F0B8): 8,
    chr(0x1F0B9): 9,
    chr(0x1F0BA): 10,
    chr(0x1F0BB): 10,
    chr(0x1F0BD): 10,
    chr(0x1F0BE): 10,
    chr(0x1F0C2): 2,
    chr(0x1F0C3): 3,
    chr(0x1F0C4): 4,
    chr(0x1F0C5): 5,
    chr(0x1F0C6): 6,
    chr(0x1F0C7): 7,
    chr(0x1F0C8): 8,
    chr(0x1F0C9): 9,
    chr(0x1F0CA): 10,
    chr(0x1F0CB): 10,
    chr(0x1F0CD): 10,
    chr(0x1F0CE): 10,
    chr(0x1F0A2): 2,
    chr(0x1F0A3): 3,
    chr(0x1F0A4): 4,
    chr(0x1F0A5): 5,
    chr(0x1F0A6): 6,
    chr(0x1F0A7): 7,
    chr(0x1F0A8): 8,
    chr(0x1F0A9): 9,
    chr(0x1F0AA): 10,
    chr(0x1F0AB): 10,
    chr(0x1F0AD): 10,
    chr(0x1F0AE): 10,
    chr(0x1F0D2): 2,
    chr(0x1F0D3): 3,
    chr(0x1F0D4): 4,
    chr(0x1F0D5): 5,
    chr(0x1F0D6): 6,
    chr(0x1F0D7): 7,
    chr(0x1F0D8): 8,
    chr(0x1F0D9): 9,
    chr(0x1F0DA): 10,
    chr(0x1F0DB): 10,
    chr(0x1F0DD): 10,
    chr(0x1F0DE): 10,
    chr(0x1F0B1): 11,
    chr(0x1F0C1): 11,
    chr(0x1F0A1): 11,
    chr(0x1F0D1): 11
}


# Creando una lista (lista_cartas) con las claves del diccionario anteriormente creado (cartas)
lista_cartas = list(cartas.keys())


# Jugador elige dos cartas
carta_jugador1 = random.choice(lista_cartas)
carta_jugador2 = random.choice(lista_cartas)


# Sumar valores de las cartas del jugador para sacar su puntuación
puntuacion_jugador = cartas[carta_jugador1] + cartas[carta_jugador2]


# Print de las cartas que le han tocado al jugador y de su puntuación (suma de los valores)
print(f"Cartas del jugador: {carta_jugador1} y {carta_jugador2}")
print(f"Puntuación del jugador: {puntuacion_jugador}")


# Banca elige dos cartas
carta_banca1 = random.choice(lista_cartas)
carta_banca2 = random.choice(lista_cartas)


# Sumar valores de las cartas de la banca para sacar su puntuación
puntuacion_banca = cartas[carta_banca1] + cartas[carta_banca2]


# Print de las cartas que le han tocado a la banca y de su puntuación (suma de los valores)
print(f"Cartas de la banca: {carta_banca1} y {carta_banca2}")
print(f"Puntuación de la banca: {puntuacion_banca}")


# Calcular las diferencias entre las puntuaciones de ambos y 21 (Black Jack)
diferencia_jugador = 21 - puntuacion_jugador
diferencia_banca = 21 - puntuacion_banca


# A través de este if, el jugador puede saber el resultado del juego, puesto que le dice si ha empatado, ganado, hecho blackjack o perdido contra la banca.
if diferencia_jugador == 0:
    print("Enhorabuena! Has conseguido Black Jack!")

elif diferencia_jugador < 0:
    print("Te has pasado!")

elif diferencia_jugador < diferencia_banca:
    print ("Has ganado a la banca!")

elif diferencia_jugador > diferencia_banca:
    print ("Lo siento, has perdido! Te ha ganado la banca!")

else:
    print("Habeis empatado!")