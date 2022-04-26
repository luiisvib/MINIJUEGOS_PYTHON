import os
import time
def borrarPantalla():
   if os.name == "posix":
       os.system ("clear")
   elif os.name == "ce" or os.name == "nt" or os.name == "dos":
       os.system ("cls")


listapacman = [[" "," "," "," "," "," "],["5","6","7"]]

for i in listapacman:
    print("-------------------------")
    for x in i:
        print("|",x,end=" ")

    print("|")
class PACMAN():
    def __init__(self):
        pass
