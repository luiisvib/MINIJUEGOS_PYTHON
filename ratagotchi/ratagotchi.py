import os
import time
import rataAccion 
import lavidamisma 


class Ratagotchi:
    def __init__(self, nombre, vida=0, hambre=50, higiene=100, felicidad=100):
        self.nombre = nombre
        self.vida = vida
        self.hambre = hambre
        self.higiene = higiene
        self.felicidad = felicidad

    def __str__(self):
        return 'Nombre: {}\nVida: {}\nHambre: {}\nHigiene: {}\nFelicidad: {}'.format(self.nombre, self.vida, self.hambre, self.higiene, self.felicidad)

    def alimentar(self):
        # rataAccion.rataCome()
        print("""
            (\-.
             / _`> .---------.
     _)     / _)=  |'-------'|
    (      / _/    |O   O   o|
     `-.__(___)_   | o O . o |
                   `---------'
            """)
        print('La rata ' + self.nombre + ' esta comiendo.')
        self.hambre += 20
        if self.hambre == 100:
            self.vida += 20
            self.hambre = 100
        
    def jugar(self):
        # rataAccion.rataJuega()
        print('Jugaste con la rata ' + self.nombre)
        self.felicidad += 20
        if self.felicidad > 100:
            self.felicidad = 100

    def banyar(self):
        # rataAccion.rataDucha()
        print('Has bañado a la rata ' + self.nombre)
        self.higiene += 50
        if self.higiene > 100:
            self.higiene = 100

    def muerte(self):
        if self.vida > 100 or self.hambre <= 0 or self.felicidad <= 0:
            return True
        else: 
            return False

    def cuidados(self, accion):
        # self.vida -= 10
        self.hambre -= 10
        self.felicidad -= 10
        self.higiene -= 10
        if accion == 'alimentar':
            self.alimentar()
        elif accion == 'jugar':
            self.jugar()
        elif accion == 'bañar':
            self.banyar()


def acciones():
    nombre = input('Ponle un nombre a la rata: ')
    rata = Ratagotchi(nombre)
    print('Hola soy', rata.nombre)
    print("""
      __QQ
     (_)_">
    _)     """)
    time.sleep(2)

    while not rata.muerte():
        print('\n'+ str(rata))
        print('\n¿Qué quieres hacer?')
        print('\n1. Alimentar\n2. Jugar\n3. Bañar\n0. Guardar y salir\n')
        opc = int(input('Seleccionar: '))
        if opc == 1:
            rata.cuidados('alimentar')
        elif opc == 2:
            rata.cuidados('jugar')
        elif opc == 3:
            rata.cuidados('bañar')
        elif opc == 0:
            print('Guardado')
            return lavidamisma.guardar_conexion()            
    print(rata.nombre + ' murio.')

def menu():
    while True:
        print('\n1. Nueva rata\n2. Continuar\n3. Salir\n')
        op = int(input('Seleccionar: '))
        if op == 1:
            acciones()
        elif op == 2:
            pass
        elif op == 3:
            print('Chauuu')
            break
menu()