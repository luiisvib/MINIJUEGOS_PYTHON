from datetime import datetime

# print(datetime.now().strftime('%Y-%m-%d %H:%M'))

def guardar_conexion():
    try:
        f=open('./ratagotchi/tiempo.txt','wt')
        f.write(datetime.now().strftime('%d %H:%M'))
    finally:
        f.close()


def refresh():
    try:
        f=open('./ratagotchi/tiempo.txt','rt')
        tiempo=f.read()
        print(tiempo[3:8])
    except FileNotFoundError as e:
        print('No se puede abrir el archivo:', e)
    finally:
        f.close()

    ultima_conexion = (int(tiempo[3:5]) * 60) + int(tiempo[6:8])
    print(ultima_conexion)

    presente = datetime.now().strftime('%d %H:%M')
    actual_conexion = (int(presente[3:5]) * 60) + int(presente[6:8])
    print(actual_conexion)

    transcurrido = actual_conexion - ultima_conexion
    print(transcurrido)
    return transcurrido

# refresh()

# try:
#     f = open("new.txt", "wt")

#     print(f.read())
#     f.write('jajaja')
# finally:
#     f.close()


# with open("new.txt", "rt") as reader:  ## with emplea close() automatico
#     print(reader.read())

    # try:
    #     # f=open('tiempo.txt','wt')
    #     # f.write(datetime.now().strftime('%d %H:%M'))
    #     # f.close()

    #     f=open('tiempo.txt','rt')
    #     tiempo=f.read()
    #     print(tiempo[3:8])
    #     f.close()
    # except FileNotFoundError as e:
    #     print('No se puede abrir el archivo:', e)