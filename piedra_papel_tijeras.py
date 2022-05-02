from pickletools import read_uint1
from random import randint
import re


print('Hola bienvenido a Piedra papel y tijeras!!!' + '✊' + '✋' + '🖖')
print('Para ganar necesitas tener 3 puntos')
print('')
print('Vamos alla!!!')
print('')

contador_partida = 1
jugar = True
contador_jugador = 0
contador_maquina = 0
contador_jugador_final = 0
contador_maquina_final = 0


###################################################################################
#Function which allow the machine to select an option

def partida_maquina(opcion_jugador,contador_jugador_final,contador_maquina_final):

    estado_jugador = True

    opcion_maquina = randint(1,3)
    if (opcion_jugador == 1 and opcion_maquina == 1):
        print('Jugador selecciono ✊ y maquina ✊ empate!')
        return 0
     
              
    elif (opcion_jugador == 2 and opcion_maquina == 2):
        print('Jugador selecciono ✋ y maquina ✋ empate!')
        return 0

    elif (opcion_jugador == 3 and opcion_maquina == 3):
        print('Jugador selecciono 🖖 y maquina 🖖 empate!')
        return 0

    elif (opcion_jugador == 1 and opcion_maquina == 2):
        print('Jugador selecciono ✊ y maquina ✋ perdiste!')
        estado_jugador = False
       
    elif (opcion_jugador == 1 and opcion_maquina == 3):
        print('Jugador selecciono ✊ y maquina 🖖 ganaste!')
        estado_jugador = True
        
    elif (opcion_jugador == 2 and opcion_maquina == 1):
        print('Jugador selecciono ✋ y maquina ✊ ganaste!')
        estado_jugador = True

    elif (opcion_jugador == 2 and opcion_maquina == 3):
        print('Jugador selecciono ✋ y maquina 🖖 perdiste!')
        estado_jugador = False
       
    elif (opcion_jugador == 3 and opcion_maquina == 1):
        print('Jugador selecciono 🖖 y maquina ✊ perdiste!')
        estado_jugador = False
        
    elif (opcion_jugador == 3 and opcion_maquina == 2):
        print('Jugador selecciono 🖖 y maquina ✋ ganaste!')
        estado_jugador = True

    if(estado_jugador == True):
        contador_jugador_final += 1
        return 'jugador'

    if(estado_jugador == False):
        contador_maquina_final += 1
        return 'maquina'
    
###################################################################################
#Function which allow to start the game and select an option

def jugar_partida(contador_jugador_final,contador_maquina_final):
    menu = """
    Selecciona el numero que representa tu jugada
    1 - ✊
    2 - ✋
    3 - 🖖
    """
    opcion_jugador = int(input(menu))
    if (opcion_jugador == 1):
        valor = partida_maquina(opcion_jugador,contador_jugador_final,contador_maquina_final)  
        return True,valor
    elif (opcion_jugador == 2):
        valor = partida_maquina(opcion_jugador,contador_jugador_final,contador_maquina_final)
        return True,valor
    elif (opcion_jugador == 3):
        valor = partida_maquina(opcion_jugador,contador_jugador_final,contador_maquina_final)
        return True,valor
    else:
        print('Opcion no valida')
        return False



###################################################################################
# 3 opportunities are defined 

while contador_partida <= 3:
    print('Partida numero ' + str(contador_partida))
    jugar = jugar_partida(contador_jugador_final,contador_maquina_final)
    if (jugar[0] == True or ''):
        print('')
        contador_partida = contador_partida + 1
        if (jugar[1] == 'jugador'):
            contador_jugador +=1
        elif (jugar[1] == 'maquina'):
            contador_maquina +=1
    else:
        break

print('Resultados finales: ')
print('jugador tiene ' + str(contador_jugador))
print('maquina tiene ' + str(contador_maquina))

if(contador_jugador < contador_maquina):
    print('Perdiste!!')
elif(contador_jugador == contador_maquina):
    print('Empate!!')
elif(contador_jugador > contador_maquina):
    print('Ganaste!!')


