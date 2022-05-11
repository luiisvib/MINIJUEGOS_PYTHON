

word = "IDEAL"

cont = 0
while cont < 6:

    p = input("Introduce palabra: ").upper()

    while len(p) != 5:
        print("Longitud incorrecta, 5 letras")
        p = input("Introduce palabra: ").upper()

    # posib, w_comp, fin = ["" for i in range(5)] ???
    posib = ["","","","",""]  # VAR AUX para estudiar letras posibles de la palabra introducida(AMARILLAS)
    w_comp = ["","","","",""] # VAR AUX para estudiar letras posibles de la palabra oculta
    fin = ["","","","",""]    # VAR AUX para estudiar letras CORRECTAS (VERDES)


    ## COMPROBACION DE LAS LETRAS CORRECTAS E INCORRECTAS:
    for i in range(5):
        
        if p[i] == word[i]:
            fin[i] = p[i]
        
        elif p[i] not in word:
            fin[i] = "0"
            w_comp[i] = word[i]
                
        else:
            posib[i] = p[i]
            w_comp[i] = word[i]

    for i in range(5):
        if posib[i] in w_comp and posib[i] != "":
            fin[i] = "1"
            w_comp.remove(posib[i])
        elif posib[i] not in w_comp:
            fin[i] = "0"

    # print("Salida:", fin)

    for i in range(5):
        if fin[i] == "0":
            print("\033[;30;47m"+" "+ p[i] +" "+'\033[0;m', end="")
        elif fin[i] == "1":
            print("\033[;30;43m"+" "+ p[i] +" "+'\033[0;m', end="")
        else:
            print("\033[;30;42m"+" "+ p[i] +" "+'\033[0;m', end="")

    print("\n")

    cont += 1

    if p == word:
        print ("¡¡ENHORABUENA, HAS ADIVINADO LA PALABRA!!")
        break

if cont == 6 and p != word:
    print("Más suerte la próxima vez...")
    print("La palabra era", word)