import os
import random
from time import sleep
import buscaminas
import Wordle 
import SIMON_DICE
import ratagotchi
import tic_tac_toe

def borrarPantalla():
   if os.name == "posix":
       os.system ("clear")
   elif os.name == "ce" or os.name == "nt" or os.name == "dos":
       os.system ("cls")
borrarPantalla()

salir =False
while salir == False:
    print("""


                ███╗   ███╗██╗███╗   ██╗██╗     ██╗██╗   ██╗███████╗ ██████╗  ██████╗ ███████╗
                ████╗ ████║██║████╗  ██║██║     ██║██║   ██║██╔════╝██╔════╝ ██╔═══██╗██╔════╝
                ██╔████╔██║██║██╔██╗ ██║██║     ██║██║   ██║█████╗  ██║  ███╗██║   ██║███████╗
                ██║╚██╔╝██║██║██║╚██╗██║██║██   ██║██║   ██║██╔══╝  ██║   ██║██║   ██║╚════██║
                ██║ ╚═╝ ██║██║██║ ╚████║██║╚█████╔╝╚██████╔╝███████╗╚██████╔╝╚██████╔╝███████║
                ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝ ╚════╝  ╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝ ╚══════╝    
                                                                                                                                                     
""")

    print("""
        MENU:

            1- BUSCAMINAS
            2- WORDLE
            3- SIMON DICE
            4- RATAGOCHI
            5- TIC TAC TOE

            0- SALIR
""")

    elegir_menu = input("Dime el juego al que quieres jugar ")
    borrarPantalla()
    if elegir_menu =="1":
        buscaminas.menuPartida()
    elif elegir_menu=="2":
        Wordle.juego_wordle()
        sleep(3)
    elif elegir_menu=="3":
        SIMON_DICE.juego_simondice()
        sleep(3)
    elif elegir_menu=="4":
        ratagotchi.juego_ratagochi()
    elif elegir_menu=="5":
        tic_tac_toe.juego_TICTACTOE()
        
    
    elif elegir_menu=="0":
        salir=True
    else:
        print("\nAsegurate de que has escrito bien la acción a realizar. ")
    sleep(3)
    borrarPantalla()

print("""

            HAS SALIDO DEL PROGRAMA
            ¡ESPERO QUE TE LO HAYAS PASADO BIEN!

""")
