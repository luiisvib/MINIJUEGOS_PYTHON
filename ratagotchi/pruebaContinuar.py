
class Paco:
    def __init__(self, nombre, vida=0, hambre=50, higiene=100, felicidad=100):
        self.nombre = nombre
        self.vida = vida
        self.hambre = hambre
        self.higiene = higiene
        self.felicidad = felicidad

    def __str__(self):
        return 'Nombre: {}\nVida: {}\nHambre: {}\nHigiene: {}\nFelicidad: {}'.format(self.nombre, self.vida, self.hambre, self.higiene, self.felicidad)


lista = ['paco' + '\n', str(3) + '\n', str(4) + '\n', str(5) + '\n', str(6) + '\n']
with open('./ratagotchi/caca.txt','wt') as writer:
        writer.writelines(lista)  

nuevo = []
# with open('./ratagotchi/caca.txt','rt') as reader:
#     nuevo.append(reader.read())
#     # print(nuevo)
#     for linea in reader:
#         nombre, vida, hambre, higiene, felicidad = linea.rstrip("\\n").split(",")
#         nuevo.append((nombre, int(vida), int(hambre), int(higiene), int(felicidad)))
            
# print(nuevo)

datos = open('./ratagotchi/caca.txt','rt')
linea = datos.readlines()

for i in range(len(linea)):
    nuevo.append(linea[i][:-1])
datos.close()
print(nuevo)
nomb=nuevo[0]
vid=int(nuevo[1])
hamb=int(nuevo[2])
hig=int(nuevo[3])
feli=int(nuevo[4])
print(type(feli))