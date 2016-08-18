#!/usr/bin/python
# -*- coding: latin-1 -*-

def iniciar_programa():
	n = 31
	alfabeto = ['0','1']
	obtener_cadenas(alfabeto, n)


def obtener_cadenas(alfabeto, n):
	archivo = open("cadenas.txt", "w")
	seguir = True
	cadena_tamporal = []
	i = 0
	tamanio = len(alfabeto) - 1

	archivo.write("∑ = { ε")
	for x in xrange(0,n):
		print "vamos en ", x+1
		i = 0
		seguir = True
		cadena_tamporal.append(0)
		while i < len(cadena_tamporal):
			cadena_tamporal[i] = 0
			i = i + 1

		while seguir:
			i = len(cadena_tamporal) - 1
			escribe_palabra(archivo, cadena_tamporal, alfabeto)
			while i > -1:
				cadena_tamporal[i] = cadena_tamporal[i] + 1
				if cadena_tamporal[i] > tamanio:
					cadena_tamporal[i] = 0
					i = i - 1
				else:
					break

			if i == -1:
				seguir = False
	archivo.write(" }")

def escribe_palabra(archivo, cadena_tamporal, alfabeto):
	archivo.write(", ")
	for x in cadena_tamporal:
	 	archivo.write(alfabeto[x])
