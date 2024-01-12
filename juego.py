"Módulo con la función del juego"


import random


#Función que contiene el desarrollo del juego
def gameOfStones():
    piedras_iniciales=random.randint(20,40)
    print(f"Se juega con: {piedras_iniciales} piedras")

    while True:
        #Player 1 movimientos
        piedrasfuera=random.choice([2,3,5])
        print(f"P1 quita {piedrasfuera} piedras")
        piedras_iniciales-=piedrasfuera
        print(piedras_iniciales)
        
        if piedras_iniciales <= 1:
            print("Enhorabuena P1, ganaste el juego")
            break
        #Player 2 movimientos
        piedrasfuera=0
        if (piedras_iniciales-2) % 7 == 0 or (piedras_iniciales-2) % 8 == 0:
            piedrasfuera=2
        if (piedras_iniciales-3) % 7 == 0 or (piedras_iniciales-3) % 8 == 0:
            piedrasfuera=3
        if (piedras_iniciales-5) % 7 == 0 or (piedras_iniciales-5) % 8 == 0:
            piedrasfuera=5
        else:
            piedrasfuera=random.choice([2,3,5])
        print(f"P2 quita {piedrasfuera} piedras")
        piedras_iniciales-=piedrasfuera
        print(piedras_iniciales)

        if piedras_iniciales <= 1:
            print("Enhorabuena P2, ganaste el juego")
            break