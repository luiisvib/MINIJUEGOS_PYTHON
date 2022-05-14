import os
import time
import random

os.system("cls")
f = open("palabraswordle.txt", "rt", encoding="utf-8")
b = f.read().split("\n")

fich_wordle = open("palabraswordle.txt", "rt", encoding="utf-8")
palabras_fich = fich_wordle.read().split("\n")


word = palabras_fich[random.randint(0, len(palabras_fich)-1)].upper()  # << Palabra secreta a adivinar
##print(word)
fich_wordle.close()


s = open('palabras05.txt', 'rt', encoding = "utf-8")
lines = s.readlines()

fich_diccionario = open('palabras05.txt', 'rt', encoding = "utf-8")
lines = fich_diccionario.readlines()



# lista con todas las palabras en español con 5 letras para comprobacion
list_palab05 = []
for i in range(len(lines)):
    list_palab05.append(lines[i][:-1].upper())
fich_diccionario.close()


# lista 5x6 vacia donde se añadirán las palabras/intentos introducidos por el usuario
p_usuario = [["   " for col in range(5)] for row in range(6)]

# lista con las letras para el teclado
t = [" Q "," W "," E "," R "," T "," Y "," U "," I "," O "," P "," A "," S "," D "," F "," G "," H "," J "," K "," L "," Ñ "," Z "," X "," C "," V "," B "," N "," M "]


def tablero(l):

    tabla = """
                    ╔═════╦═════╦═════╦═════╦═════╗
                    ║ """+ l[0][0] +""" ║ """+ l[0][1] +""" ║ """+ l[0][2] +""" ║ """+ l[0][3] +""" ║ """+ l[0][4] +""" ║
                    ╠═════╬═════╬═════╬═════╬═════╣
                    ║ """+ l[1][0] +""" ║ """+ l[1][1] +""" ║ """+ l[1][2] +""" ║ """+ l[1][3] +""" ║ """+ l[1][4] +""" ║
                    ╠═════╬═════╬═════╬═════╬═════╣
                    ║ """+ l[2][0] +""" ║ """+ l[2][1] +""" ║ """+ l[2][2] +""" ║ """+ l[2][3] +""" ║ """+ l[2][4] +""" ║
                    ╠═════╬═════╬═════╬═════╬═════╣
                    ║ """+ l[3][0] +""" ║ """+ l[3][1] +""" ║ """+ l[3][2] +""" ║ """+ l[3][3] +""" ║ """+ l[3][4] +""" ║
                    ╠═════╬═════╬═════╬═════╬═════╣
                    ║ """+ l[4][0] +""" ║ """+ l[4][1] +""" ║ """+ l[4][2] +""" ║ """+ l[4][3] +""" ║ """+ l[4][4] +""" ║
                    ╠═════╬═════╬═════╬═════╬═════╣
                    ║ """+ l[5][0] +""" ║ """+ l[5][1] +""" ║ """+ l[5][2] +""" ║ """+ l[5][3] +""" ║ """+ l[5][4] +""" ║
                    ╚═════╩═════╩═════╩═════╩═════╝
            """
    print(tabla)



def teclado(t, pal, p_fin):

    try: 
        for i in range(len(pal)):
            for j in range(len(t)):
                if pal[i] == t[j].strip():
                    t[j] = p_fin[i]
                    
                if p_fin[i][7] == "2" and t[j] == "\033[;30;43m"+" "+ pal[i] +" "+'\033[0;m':
                    t[j] = "\033[;30;42m"+" "+ pal[i] +" "+'\033[0;m'

    except Exception:
        pass


    teclado = """
        ╔═════╦═════╦═════╦═════╦═════╦═════╦═════╦═════╦═════╦═════╗
        ║ """+ t[0] +""" ║ """+ t[1] +""" ║ """+ t[2] +""" ║ """+ t[3] +""" ║ """+ t[4] +""" ║ """+ t[5] +""" ║ """+ t[6] +""" ║ """+ t[7] +""" ║ """+ t[8] +""" ║ """+ t[9] +""" ║ 
        ╠═════╬═════╬═════╬═════╬═════╬═════╬═════╬═════╬═════╬═════╣
        ║ """+ t[10] +""" ║ """+ t[11] +""" ║ """+ t[12] +""" ║ """+ t[13] +""" ║ """+ t[14] +""" ║ """+ t[15] +""" ║ """+ t[16] +""" ║ """+ t[17] +""" ║ """+ t[18] +""" ║ """+ t[19] +""" ║ 
        ╚═════╩═════╬═════╬═════╬═════╬═════╬═════╬═════╬═════╬═════╝
                    ║ """+ t[20] +""" ║ """+ t[21] +""" ║ """+ t[22] +""" ║ """+ t[23] +""" ║ """+ t[24] +""" ║ """+ t[25] +""" ║ """+ t[26] +""" ║
                    ╚═════╩═════╩═════╩═════╩═════╩═════╩═════╝
        """
    print(teclado)


cont = 0

tablero(p_usuario)
teclado(t, p_usuario, 0)


while cont < 6:

    p = input("Introduce palabra: ").upper()

    while len(p) != 5:
        print("Longitud incorrecta, 5 letras")
        p = input("Introduce palabra: ").upper()

    while p not in list_palab05:
        print("La palabra introducida no existe")
        p = input("Introduce palabra: ").upper()
        print(p)


    aux_p_usu = ["","","","",""]  # VAR AUX para estudiar letras posibles de la palabra introducida(AMARILLAS)
    aux_word = ["","","","",""] # VAR AUX para estudiar letras posibles de la palabra secreta
    p_fin = ["","","","",""]    # VAR para introducir las letras de la palabra introducida con sus colores correspondientes
    

    ## COMPROBACION DE LAS LETRAS CORRECTAS E INCORRECTAS:
    for i in range(5):
        
        if p[i] == word[i]:
            p_fin[i] = "\033[;30;42m"+" "+ p[i] +" "+'\033[0;m'  ## LETRA en VERDE
        
        elif p[i] not in word:
            p_fin[i] = "\033[;30;47m"+" "+ p[i] +" "+'\033[0;m'  ## LETRA en BLANCO
            aux_word[i] = word[i]
                
        else:
            aux_p_usu[i] = p[i]
            aux_word[i] = word[i]


    ## Estudio de las letras que, a priori, no son correctas o incorrectas: 
    # si están en distinta posición (AMARILLO) o se ha dado el caso de que la letra está en la palabra pero ya está en la posición correcta (BLANCO)
    for i in range(5):
        if aux_p_usu[i] in aux_word and aux_p_usu[i] != "":
            p_fin[i] = "\033[;30;43m"+" "+ p[i] +" "+'\033[0;m'  ## LETRA en AMARILLO
            aux_word.remove(aux_p_usu[i])
        elif aux_p_usu[i] not in aux_word:
            p_fin[i] = "\033[;30;47m"+" "+ p[i] +" "+'\033[0;m'  ## LETRA en BLANCO

    p_usuario[cont] = p_fin

    os.system("cls")
    
    tablero(p_usuario)
    teclado(t, p, p_fin)
    cont += 1

    if p == word:
        print ("¡¡ENHORABUENA, HAS ADIVINADO LA PALABRA!!")
        time.sleep(5)
        break

if cont == 6 and p != word:
    print("Más suerte la próxima vez...")
    print("La palabra era", word)
    time.sleep(5)
