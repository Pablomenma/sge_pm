#Crea un programa que implemente el clásico juego de piedra, papel, tijeras, lagarto y spock.
#Las normas de este juego son:
#Piedra aplasta a lagarto
#Lagarto envenena a Spock
#Spock rompe las tijeras
#Tijeras decapitan al lagarto
#Lagarto come al papel
#Papel  desautoriza a Spock
#Spock vaporiza la piedra
#Piedra rompe a tijeras
#Tijeras cortan papel
#Papel envuelve a piedra
#ganara  el primero que gane cinco manos 


from random import *

eleciones = ["piedra", "papel", "tijeras", "lagarto", "spock"]

enemigo_victorias = 0
player_victorias = 0
while(not (enemigo_victorias == 5 or player_victorias == 5)):
    player_eleccion = input("Elije piedra, papel tijeras, lagarto o spock: ")
    enemigo_eleccion = choice(eleciones)
    match (enemigo_eleccion):
        case "piedra":
            print("Ele enemigo elije " + enemigo_eleccion)
            if player_eleccion == "papel" or player_eleccion ==  "spock":
                print("victoria")
                player_victorias = player_victorias + 1
            elif player_eleccion == "tijeras" or player_eleccion ==  "lagarto":
                print("derrota")
                enemigo_victorias = enemigo_victorias + 1
            else:
                print("empate")
        case "papel":
            print("Ele enemigo elije " + enemigo_eleccion)
            if player_eleccion == "tijeras" or player_eleccion ==  "lagarto":
                print("victoria")
                player_victorias = player_victorias + 1
            elif player_eleccion == "piedra" or player_eleccion ==  "spock":
                print("derrota")
                enemigo_victorias = enemigo_victorias + 1
            else:
                print("empate")
        case "tijeras":
            print("Ele enemigo elije " + enemigo_eleccion)
            if player_eleccion == "piedra" or player_eleccion ==  "spock":
                print("victoria")
                player_victorias = player_victorias + 1
            elif player_eleccion == "papel" or player_eleccion ==  "lagarto":
                print("derrota")
                enemigo_victorias = enemigo_victorias + 1
            else:
                print("empate")
        case "lagarto":
            print("Ele enemigo elije " + enemigo_eleccion)
            if player_eleccion == "tijeras" or player_eleccion ==  "piedra":
                print("victoria")
                player_victorias = player_victorias + 1
            elif player_eleccion == "papel" or player_eleccion ==  "spock":
                print("derrota")
                enemigo_victorias = enemigo_victorias + 1
            else:
                print("empate")
        case "spock":
            print("Ele enemigo elije " + enemigo_eleccion)
            if player_eleccion == "papel" or player_eleccion ==  "lagarto":
                print("victoria")
                player_victorias = player_victorias + 1
            elif player_eleccion == "tijeras" or player_eleccion ==  "piedra":
                print("derrota")
                enemigo_victorias = enemigo_victorias + 1
            else:
                print("empate")
    print("Victorias de player " + str(player_victorias))
    print("Victorias de enemigo: " + str(enemigo_victorias))
        
if(enemigo_victorias == 5):
    print("Enemigo gana")
else:
    print("Player gana")
