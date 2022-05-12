import os
import time
import rataAccion 
import lavidamisma 


class Ratagotchi:
    def __init__(self, nombre, vida=100, hambre=50, higiene=100, felicidad=100):
        self.nombre = nombre
        self.vida = vida
        self.hambre = hambre
        self.higiene = higiene
        self.felicidad = felicidad

    def __str__(self):
        return 'Nombre: {}\nVida: {}\nHambre: {}\nHigiene: {}\nFelicidad: {}'.format(self.nombre, self.vida, self.hambre, self.higiene, self.felicidad)

    def alimentar(self):
        rataAccion.rataCome()
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
        if self.hambre >= 100:
            self.vida += 20
            self.hambre = 100
        
    def jugar(self):
        rataAccion.rataJuega()
        print("""
               _   _
              (q\_/p)
               (. .)
              =\_t_/=   __
               /   \   (
              ((   ))   )
              /\) (/\  /
              \  Y  /-'
               nn^nn
        """)
        print('Jugaste con la rata ' + self.nombre)
        self.felicidad += 20
        if self.felicidad > 100:
            self.felicidad = 100
        elif self.felicidad <= 0:
            self.felicidad = 0

    def banyar(self):
        rataAccion.rataDucha()
        print(  """
           ,------|
          []      |             
          ¡¡      |
                  |
                  |     
         ()()     |
         (..)     |
         /\/\     |
        c\db/o   _|_

  """)
        print('Has bañado a la rata ' + self.nombre)
        self.higiene += 50
        if self.higiene > 100:
            self.higiene = 100
        elif self.higiene <= 0:
            self.higiene = 0
    def muerte(self):
        if self.vida <= 0 or self.hambre <= 0 or self.felicidad <= 0:
            return True
        else: 
            return False

    def cuidados(self, accion):
        self.vida -= 10
        self.hambre -= 10
        self.felicidad -= 10
        self.higiene -= 10
        if accion == 'alimentar':
            self.alimentar()
        elif accion == 'jugar':
            self.jugar()
        elif accion == 'bañar':
            self.banyar()
  

def new_rata():
    nombre = input('Ponle un nombre a la rata: ')
    rata = Ratagotchi(nombre)
    acciones(rata)

def guardar(rata):
    estado = [rata.nombre +'\n', str(rata.vida) +'\n', str(rata.hambre) +'\n', str(rata.higiene) +'\n', str(rata.felicidad) +'\n']
    with open('./ratagotchi/estado.txt','wt') as writer:
        writer.writelines(estado)  

def continuar():
    status = []
    try:
        datos = open('./ratagotchi/estado.txt','rt')
        linea = datos.readlines()
        for i in range(len(linea)):
            status.append(linea[i][:-1])
    except FileNotFoundError as e:
        print('No se puede abrir el archivo:', e)
    finally:    
        datos.close()

    name=status[0]
    life=int(status[1])
    hungry=int(status[2])
    hygiene=int(status[3])
    happiness=int(status[4])

    rata = Ratagotchi(name,life,hungry,hygiene,happiness)
    acciones(rata)
    

def acciones(rata):    
    print('Hola soy', rata.nombre)
    print("""
      __QQ
     (_)_">
    _)     """)
    time.sleep(2)
    try:
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
                guardar(rata)
                return lavidamisma.guardar_conexion() 
        print('\n'+ str(rata))           
        print(rata.nombre + ' murio.')
        print("""
              ,-=-.  
             /  +  \ 
             | ~~~ |  
             |R.I.P|  
        \wvV,|_____|vwv/,
        """)
    except ValueError as e:
        print('Seleccione una opción valida.')
        acciones(rata)

def menu():
    try:
        while True:
            print('''    
     _____          _______         _____   ____  _______  _____  _    _  _____ 
    |  __ \     /\ |__   __| /\    / ____| / __ \|__   __|/ ____|| |  | ||_   _|
    | |__) |   /  \   | |   /  \  | |  __ | |  | |  | |  | |     | |__| |  | |  
    |  _  /   / /\ \  | |  / /\ \ | | |_ || |  | |  | |  | |     |  __  |  | |  
    | | \ \  / ____ \ | | / ____ \| |__| || |__| |  | |  | |____ | |  | | _| |_ 
    |_|  \_\/_/    \_\|_|/_/    \_ \_____| \____/   |_|   \_____||_|  |_||_____|                                                                            
                                                                                                                                                                                    
            ''')
            print('\n1. Nueva rata\n2. Continuar\n3. Salir\n')
            op = int(input('Seleccionar: '))
            if op == 1:
                new_rata()
            elif op == 2:
                continuar()
            elif op == 3:
                print('Chauuu')
                break
    except ValueError as e:
        print('Hubo un error de valor:', e)
menu()