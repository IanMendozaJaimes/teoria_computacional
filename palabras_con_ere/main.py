from automata import obtener_palabras, graficar_automata
from ctypes import *

def main():
    seguir = True
    while seguir:
        try:
            palabras_aceptadas = []
            texto = ""
            archivo = None

            opcion = imprimir_menu()

            if opcion == 1:
                print("\n\nIngrese un texto (dos enter para salir): \n")
                tem = ''
                t = ''
                texto = []
                contador = 0
                while True:
                    t = input()
                    if t == '':
                        break
                    texto.append(t)

                palabras_aceptadas = leer_texto(texto)
            elif opcion == 2:
                texto = input("\n\nIngrese el nombre de un archivo: \n")
                archivo = open(texto, "r")
                palabras_aceptadas = leer_texto(archivo)
                archivo.close()
            elif opcion == 3:
                print("Sera utilizado el archivo heart.txt")
                archivo = open("heart.txt", "r")
                palabras_aceptadas = leer_texto(archivo)
            elif opcion == 4:
                graficar_automata()
            else:
                return 0

            imprimir_palabras_aceptadas(palabras_aceptadas, opcion)

            texto = input("\n\nDesea ingresar otra cosa? [s/n]: ")
            if (texto != 's') and (texto != 'S'):
                seguir = False

        except Exception as e:
            print("Uuups!, parece que tuvimos un problema: ", e)
    return 1


def imprimir_menu():
    seguir = True
    while seguir:
        try:
            opcion = int(input("\n\nIngrese la opcion que desea: \n1.- Ingresar texto \n2.- Ingresar un archivo \n3.- Automatico \n4.- Ver gráfico del automata \n5.- Salir\n"))
            return opcion
        except Exception as e:
            print("Por favor, ingrese un dato valido.")


def leer_texto(texto):
    aceptadas = None
    palabras_aceptadas = []
    contador = 1
    for linea in texto:
        aceptadas = obtener_palabras(linea)
        palabras_aceptadas.append([contador, aceptadas])
        contador += 1

    return palabras_aceptadas


def imprimir_palabras_aceptadas(palabras_aceptadas, seleccion):
    print("\n\n\n")
    if seleccion == 1:
        print("Palabras aceptadas: ", palabras_aceptadas)
    else:
        contador = 0
        for x in palabras_aceptadas:
            if len(x[1]) > 0:
                print("")
                print("Linea ", str(x[0])+',', " palabras aceptadas: ", end=' ')
                for palabra in x[1]:
                    print(palabra[0], '(No. palabra:'+str(palabra[1])+')', end=', ')


main()
