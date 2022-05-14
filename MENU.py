import os
import random
from time import sleep
import buscaminas
import Wordle 
import SIMON_DICE
import ratagotchi

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

            - BUSCAMINAS
            - WORDLE
            - SIMON DICE
            - RATAGOCHI
            - TIC TAC TOE

            - SALIR
""")

    elegir_menu = input("Escribe que juego al que quieres jugar: ")
    borrarPantalla()
    if elegir_menu =="BUSCAMINAS":
        buscaminas.juegobuscaminas()
    elif elegir_menu=="WORDLE":
        Wordle.juego_wordle()
        sleep(3)
    elif elegir_menu=="SIMON DICE":
        SIMON_DICE.juego_simondice()
        sleep(3)
        
    #elif elegir_menu=="TIC TAC TOE":
        
    elif elegir_menu=="RATAGOCHI":
        ratagotchi.juego_ratagochi()
        
    elif elegir_menu=="SALIR":
        salir=True
    else:
        print("\nAsegurate de que has escrito bien la acción a realizar y en MAYUSCULAS")
    sleep(3)
    borrarPantalla()

print("""

            HAS SALIDO DEL PROGRAMA
            ¡ESPERO QUE TE LO HAYAS PASADO BIEN!

""")
