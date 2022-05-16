import time
import os
import random

def juego_simondice():
    def borrarPantalla():
        if os.name == "posix":
            os.system ("clear")
        elif os.name == "ce" or os.name == "nt" or os.name == "dos":
            os.system ("cls")

    global contador
    def apagar_tablero():
        global tabla
        tabla = [
                ["                ","                 "],
                ["|-------------| "," |-------------| "],
                ["|             | "," |             | "],
                ["|      1      | "," |      2      | "],
                ["|             | "," |             | "],
                ["|-------------| "," |-------------| "],
                ["                ","                 "],
                ["                ","                 "],
                ["|-------------| "," |-------------| "],
                ["|             | "," |             | "],
                ["|      3      | "," |      4      | "],
                ["|             | "," |             | "],
                ["|-------------| "," |-------------| "],
                ["                ","                 "],
            ]

    apagar_tablero()
    def tiempo(x):
        if x==1:
            time.sleep(0.7)
        if x==2:
            time.sleep(0.5)
        if x ==3:
            time.sleep(0.3)
        if x ==4:
            time.sleep(0.1)
        
    def iluminar_cuadrado1():
        fila = 0
        for i in tabla:
            fila = fila+1
            if fila == 8:
                break
            else:
                i[0] = "\033[41m" + i[0] + "\033[0m"

    def iluminar_cuadrado2():
        fila = 0
        for i in tabla:
            fila = fila+1
            if fila == 8:
                break
            else:
                i[1] = "\033[42m" + i[1] + "\033[0m"

    def iluminar_cuadrado3():
        fila = 0
        for i in tabla:
            fila = fila+1
            if fila < 8:
                continue
            else:
                i[0] = "\033[44m" + i[0] + "\033[0m"

    def iluminar_cuadrado4():
        fila = 0
        for i in tabla:
            fila = fila+1
            if fila < 8:
                continue
            else:
                i[1] = "\033[45m" + i[1] + "\033[0m"

    def mostrar_tablero():
        for i in tabla:
            for x in i:
                print("\t",x,end="")
            print("")
    contador_principiante = 0
    contador_profesional = 0
    contador_avanzado = 0
    contador_experto = 0
    contador=0
    def jugar():
        borrarPantalla()
        global contador
        global modo
        print("""

                    Niveles de Dificultad:
                    1- Principiate
                    2- Profesional
                    3- Avanzado
                    4- Experto

                                
                                """)

        dificultad = int(input("Elige el nivel de dificultad: "))
        borrarPantalla()
        def mostrar_pantalla():
            for i in tabla:
                for x in i:
                    print("\t",x,end="")
                print("")
            tiempo(dificultad)
            borrarPantalla()
            apagar_tablero()


        salir = False
        contador = 0
        numeros = ""
        borrarPantalla()
        while salir == False:
            contador += 1
            aleatorio = random.randrange(1,5)
            aleatoriostr = str(aleatorio)
            numeros += aleatoriostr
            for i in numeros:
                if i == "1":
                    iluminar_cuadrado1()
                if i == "2":
                    iluminar_cuadrado2()
                if i == "3":
                    iluminar_cuadrado3()
                if i == "4":
                    iluminar_cuadrado4()
                mostrar_pantalla()
                mostrar_tablero()
                tiempo(dificultad)
                borrarPantalla()
            mostrar_tablero()
            adivinar = input("Dime la secuencia de numeros: ")
            if adivinar == numeros:
                print("Has acertado, ¡CONTINUA!")
                time.sleep(1)
                borrarPantalla()
                
            else:
                print("\n¡Has perdido!\n")
                if dificultad ==1:
                    modo = "Principiante"
                elif dificultad ==2:
                    modo = "Profesional"
                elif dificultad ==3:
                    modo = "Avanzado"
                elif dificultad ==4:
                    modo = "Experto"

                print("Has llegado hasta el nivel",contador,"en modo",modo,"\n\n")
                salir = True

        

    salir_menu = False
    while salir_menu == False:
        time.sleep(1.5)
        borrarPantalla()
        if contador > contador_principiante and modo=="Principiante":
            contador_principiante = contador

        elif contador > contador_profesional and modo=="Profesional":
            contador_profesional = contador

        elif contador > contador_avanzado and modo=="Avanzado":
            contador_avanzado = contador

        elif contador > contador_experto and modo=="Experto":
            contador_experto = contador


        print("""  
         _______. __  .___  ___.   ______   .__   __.     _______   __    ______  _______ 
        /       ||  | |   \/   |  /  __  \  |  \ |  |    |       \ |  |  /      ||   ____|
       |   (----`|  | |  \  /  | |  |  |  | |   \|  |    |  .--.  ||  | |  ,----'|  |__   
        \   \    |  | |  |\/|  | |  |  |  | |  . `  |    |  |  |  ||  | |  |     |   __|  
    .----)   |   |  | |  |  |  | |  `--'  | |  |\   |    |  '--'  ||  | |  `----.|  |____ 
    |_______/    |__| |__|  |__|  \______/  |__| \__|    |_______/ |__|  \______||_______|

                                     Records niveles :
                                    
                                        Principiante: """,contador_principiante,"""
                                        Profesional: """,contador_profesional,"""
                                        Avanzado: """,contador_avanzado,"""
                                        Experto: """,contador_experto)
        print("\n")
        iniciar_juego = input("Pulsa enter para empezar el juego o pulsa x para salir ")
        if iniciar_juego =="x":
            return
        else:
            jugar()
            borrarPantalla()

