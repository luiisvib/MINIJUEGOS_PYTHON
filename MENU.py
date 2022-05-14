import os
import random
import time
import buscaminas
def borrarPantalla():
   if os.name == "posix":
       os.system ("clear")
   elif os.name == "ce" or os.name == "nt" or os.name == "dos":
       os.system ("cls")
borrarPantalla()

print("""
        JUEGOS 
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


salir =False
while salir == False:
    elegir_menu = input("Escribe que juego al que quieres jugar: ")
    if elegir_menu =="BUSCAMINAS":
        buscaminas.juegobuscaminas()
    elif elegir_menu=="WORDLE":
        import Wordle 
        time.sleep(3)
    elif elegir_menu=="SIMON DICE":
        import SIMON_DICE
        time.sleep(3)
    elif elegir_menu=="TIC TAC TOE":
        import tic_tac_toe
    elif elegir_menu=="RATAGOCHI":
        import ratagotchi
    elif elegir_menu=="SALIR":
        salir==True
    else:
        print("\nAsegurate de que has escrito bien la acción a realizar y en MAYUSCULAS")

borrarPantalla()
print("holaaa")
