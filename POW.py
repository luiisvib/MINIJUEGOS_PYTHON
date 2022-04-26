#!/usr/bin/python3
import os
import time
os.system("clear")

salud = 100
felicidad = 100
comida = 100
saludstr= str(salud)
felicidadstr = str(felicidad)
comidastr = str(comida)

movimiento = ["""

                                       """+"""     Salud = """+saludstr +"""%""" +"""
                     ************      """+"""     Felicidad = """+felicidadstr+"""%"""  +"""
                    *            *     """+"""     Comida = """+comidastr+"""%"""  +"""
                   *     *  *     *
                   *              *
                   *     `--´     *
                   *              *
                   ****************
    """,
            """

                     ************      """+"""     Salud = """+saludstr +"""%""" +"""
                    *            *     """+"""     Felicidad = """+felicidadstr +"""%""" +"""
                   *     *  *     *    """+"""     Comida = """+comidastr+"""%"""  +"""
                   *              *
                   *     `--´     *
                   *              *
                   ****************

    """,
            """
                     ************   
                    *            *     """+"""     Salud = """+saludstr +"""%""" +"""
                   *     *  *     *    """+"""     Felicidad = """+felicidadstr +"""%""" +"""
                   *              *    """+"""     Comida = """+comidastr+"""%"""  +"""
                   *     `--´     *
                   *              *
                   ****************


    """
]

def inicio():
    salir = False
    contador = 0
    while salir == False:
        contador +=1
        for i in movimiento:
            print(i)
            if contador < 5:
                print("""
                       ¡Buenas!
               Estas en el Juego del POW""")
            else:
                if contador == 10:
                    return
                else:
                    print("""
    Tienes que cuidarme, alimentarme y hacerme felizzz""")
            time.sleep(0.2)
            os.system("clear")

def menu():
    print("""
    Tienes que jugar a diferentes minijuegos""")
    time.sleep(2)

inicio()
menu()