import os
import random
import time
import buscaminas
import Wordle

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

            1- Buscaminas
            2- Wordle
            3- Simon Dice
            4- Ratagochi
            5- 
""")

elegir_menu = input("Escribe que juego al que quieres jugar: ")
if elegir_menu =="Buscaminas":
    buscaminas.juegobuscaminas()
elif elegir_menu=="Wordle":
    Wordle.juegoWordle()
borrarPantalla()
print("holaaa")
