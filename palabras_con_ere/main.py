from automata import obtener_palabras
from ctypes import *


#Esto es muy util
#http://shakaran.net/blog/2010/10/como-usar-bibliotecas-de-c-en-python/

#grafico = cdll.LoadLibrary('./grafico.so')
#print(grafico.multiplicar(2,3))


def main():
    #texto = "¡Es cierto! Siempre he sido nervioso, muy nervioso, terriblemente nervioso. ¿Pero por qué afirman ustedes que estoy loco? La enfermedad había agudizado mis sentidos, en vez de destruirlos o embotarlos. Y mi oído era el más agudo de todos. Oía todo lo que puede oírse en la tierra y en el cielo. Muchas cosas ere oí en el infierno. ¿Cómo puedo estar loco, entonces? Escuchen… y observen con cuánta cordura, con cuánta tranquilidad les cuento mi historia. quiere"
    #texto = 'It is impossible to say how first the idea entered my brain; but once conceived, it haunted me day and night. Object there was none. Passion there was none. I loved the old man. He had never wronged me. He had never given me insult. For his gold I had no desire. I think it was his eye! yes, it was this! He had the eye of a vulture --a pale blue eye, with a film over it. Whenever it fell upon me, my blood ran cold; and so by degrees --very gradually --I made up my mind to take the life of the old man, and thus rid myself of the eye forever.'
    seguir = True
    while seguir:
        try:
            alfabeto = [97, 122]
            palabras_aceptadas = []
            texto = ""
            archivo = None

            opcion = imprimir_menu()

            if opcion == 1:
                texto = input("\n\nIngrese un texto: \n")
                palabras_aceptadas = leer_texto(alfabeto, texto)
            elif opcion == 2:
                texto = input("\n\nIngrese el nombre de un archivo: \n")
                print(texto)
                archivo = open(texto, "r")
                palabras_aceptadas = leer_archivo(alfabeto, archivo)
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
            opcion = int(input("\n\nIngrese la opción que desea: \n1.- Ingresar texto \n2.- Ingresar un archivo \n3.- Salir \n"))
            return opcion
        except Exception as e:
            print("Por favor, ingrese un dato valido.")


def leer_texto(alfabeto, texto):
    texto += " "
    aceptadas = obtener_palabras(alfabeto, texto)
    return aceptadas


def leer_archivo(alfabeto, archivo):
    aceptadas = None
    palabras_aceptadas = []
    contador = 1
    for linea in archivo:
        print(linea)
        aceptadas = obtener_palabras(alfabeto, linea)
        palabras_aceptadas.append([contador, aceptadas])
        contador += 1

    archivo.close()
    return palabras_aceptadas


def imprimir_palabras_aceptadas(palabras_aceptadas, seleccion):
    print("\n\n\n")
    if seleccion == 1:
        print("Palabras aceptadas: ", palabras_aceptadas)
    else:
        contador = 0
        for x in palabras_aceptadas:
            if len(x[1]) > 0:
                print("Linea ", x[0], " palabras aceptadas: ", x[1])


main()
