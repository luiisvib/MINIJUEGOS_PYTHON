import os
import time
def borrarPantalla():
   if os.name == "posix":
       os.system ("clear")
   elif os.name == "ce" or os.name == "nt" or os.name == "dos":
       os.system ("cls")

borrarPantalla()

def mostrarPantalla():
    tablero = [
    ["PARKING",130,150,100,900,444,555,900,"A CARCEL"],
    [500,"                                                      ",500],
    [300,"   |DIAMANTE|                                         ",500],
    [300,"                       MONOPOLY                       ",500],
    [600,"                                                      ",360],
    [600,"                                          |SUERTE|    ",460],
    [400,"                                                      ",900],
    ["CARCEL ",320,600,800,100,599,466,666,"SALIDA  "]
    ]

    print("")
    for i in tablero:
        if i == tablero[0]  or i == tablero[1] or i == tablero[7]:
            print("     |"+"-"*69+"|")
        else:
            print("     |------|                                                       |------|")

        print("     ",end="")
        for x in i:
            if i == tablero[0]  or i == tablero[7]:
                if x == i[0] or x == i[8]:
                    print("|",x,end=" ")
                else:
                    print("|",x,end="M ")
                continue
                
            else:
                if x == i[1]:
                    print("|",x,end="")
                else:
                    print("|",x,end="M ")
                    
        print("|")
    print("     |"+"-"*69+"|")
    print("""


    """)
mostrarPantalla()

class jugadores():
    def __init__(self,nombre,ficha):
        self.nombre = nombre
        self.ficha = ficha

    def __str___(self):
        print("Jugador actual: "+self.nombre)
        print("Color de ficha: "+self.ficha)


n_jugadores = int(input("Dime el numero de jugadores: "))

for i in range(n_jugadores):
    print("Dime el nombre del jugador",i+1,":",end=" ")
    nombre_jugador = input("")
