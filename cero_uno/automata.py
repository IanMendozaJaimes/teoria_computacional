#FAIL

import threading #para los hilos
import time

letra_global = ''
estado_global = [0]
c = threading.Condition()

class proceso_automata(threading.Thread):
    def __init__(self, estado):
        threading.Thread.__init__(self)
        self.estado = estado

    def run(self):
        global letra_global
        global estado_global
        while True:
            c.acquire()
            self.estado = automata(self.estado, letra_global)
            if self.estado == 3:
                estado_global[0] = 2
                break
            elif self.estado == -1:
                break

            time.sleep(0.1)
            c.notify_all()
            c.release()




def evaluar_cadena(cadena):
    estado = [0]
    hilos = []
    for letra in cadena:
        letra_global = letra
        estado = automata(estado[0], letra)
        if len(estado) > 1:
            h = proceso_automata(estado[1])
            hilos.append(h)
            h.start()
            h.join()

        time.sleep(0.2)

    #print(estado_global)
    if estado_global[0] == 2:
        return True
    else:
        return False


def automata(estado, letra):
    if estado == 0:
        return estado_cero(letra)
    elif estado == 1:
        return estado_uno(letra)
    elif estado == 2:
        return estado_dos(letra)
    else:
        return [-1]


def estado_cero(letra):
    estados = []
    if letra == '0' or letra == '1':
        estados.append(0)
        estados.append(1)
        return estados
    else:
        return [-1]


def estado_uno(letra):
    estados = []
    if letra == '1':
        estados.append(2)
        return estados
    else:
        return [-1]

def estado_dos(letra=''):
    if letra != '':
        return [-1]
    else:
        return [3]
