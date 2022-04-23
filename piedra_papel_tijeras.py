print('Hola bienvenido a Piedra papel y tijeras!!!' + '✊' + '✋' + '🖖')
print('Para ganar necesitas tener 3 puntos')
print('')
print('Vamos alla!!!')
print('')

contador_partida = 1
jugar = True

###################################################################################
#Function which allow to start the game and select an option

def jugar_partida():
    menu = """
    Selecciona el numero que representa tu jugada
    1 - ✊
    2 - ✋
    3 - 🖖
    """
    opcion_jugador = int(input(menu))
    if (opcion_jugador == 1):
        print('Jugador selecciono ✊')
        return True
    elif (opcion_jugador == 2):
        print('Jugador selecciono ✋')
        return True
    elif (opcion_jugador == 3):
        print('Jugador selecciono 🖖')
        return True
    else:
        print('Opcion no valida')
        return False



###################################################################################
# 3 opportunities are defined 

while contador_partida <= 3:
    print('Partida numero ' + str(contador_partida))
    jugar = jugar_partida()
    if (jugar == True or ''):
        print('')
        contador_partida = contador_partida + 1
    else:
        break

