import pymongo
from pymongo import MongoClient
from mongoengine import *
import os
from  validators import validar_dorsal,validar_entero, num

connect('db_equipo', host='localhost', port=27017)


POSICIONES = (('POR', 'PORTERO'),
        ('DEF', 'DEFENSAS'),
        ('LT', 'LATERALES'),
        ('MED', 'MEDIO CAMPISTAS'),
        ('DEL', 'DELANTEROS'))

class Jugador(Document):
	nombre= StringField(required=True,max_length=40)
	dorsal= IntField(unique=True)
	posicion= StringField(max_length=5, choices=POSICIONES)
	valoracion= IntField(default=0)

	def __str__(self):
		return "|| %s || Dorsal: %s || Juegan en la posición %s ||" % (self.nombre,self.dorsal, self.posicion)

def menu():
	print("------MENÚ PRINCIPAL-----------" )
	print("[1] Crear jugador ")
	print("[2] Mostrar cantidad de Jugdrs.")
	print("[3] Buscar Jogador")
	print("[4] Eliminar jugador")
	print("[5] Ver lista de jugadores")
	print("[6] Asignar valoraciones")
	print("[0] Salir")

def pos():
	print("----------POSICIONES----------------")
	print("[1] PORTERO ")
	print("[2] DEFENSA CENTRAL")
	print("[3] LATERAL")
	print("[4] MEDIO CAMPISTA")
	print("[5] DELANTERO")
	posicion = num()
	return posicion


def valoraciones():
	print("----------VALORACIONES----------------")
	print("[1] GOL (+3)")
	print("[2] QUITE DE BALÓN(+2)")
	print("[3] BUEN PASE(+2)")
	print("[4] AUTO GOL(-2)")
	print("[5] DESPEJE(+2)")
	posicion = num()
	return posicion


def asignar_posicion(valor):
	if valor == 1:
		pos1 = "POR"
		return pos1
	if valor == 2:
		pos1 = "DEF"
		return pos1
	if valor == 3:
		pos1 = "LT"
		return pos1
	if valor == 4:
		pos1 = "MED"
		return pos1
	if valor == 5:
		pos1 = "DEL"
		return pos1
	else:
		print("Escoja de nuevo")

def mensaje():
	input("Presione enter tecla para continuar....")
	os.system('cls')

def clear():
	os.system('cls')

def crearJugador():
	print("----------CREAR JUGADOR ---------------------")
	nombre1 = input("Ingrese nombre: ")
	dorsal1 = validar_dorsal()
	pos0 = pos()
	pos1 = asignar_posicion(pos0)
	
	
	total_jugadores = Jugador.objects().count()
	total_jugadores_por = Jugador.objects(posicion='POR').count()
	total_jugadores_def = Jugador.objects(posicion='DEF').count()
	total_jugadores_lt = Jugador.objects(posicion='LT').count()
	total_jugadores_med = Jugador.objects(posicion='MED').count()
	total_jugadores_del = Jugador.objects(posicion='DEL').count()

	nuevojugador = Jugador (
		nombre=nombre1,
		dorsal=dorsal1,
		posicion=pos1 )

	if total_jugadores <11:

		if pos1 == 'POR':
			
			if total_jugadores_por <1:
				nuevojugador.save()
				print("-----------------------------------------------------")
				print("Jugador {}, con dorsal {} y posición {} fue guardado!".format(nuevojugador.nombre, nuevojugador.dorsal, nuevojugador.posicion))
				print("-----------------------------------------------------")
				mensaje()
			else:
				print("-----------------------------------------------------")
				print("Cupos llenos para porteros :(")
				print("-----------------------------------------------------")
				mensaje()

		if pos1 == 'DEF':
			
			if total_jugadores_def <2:
				nuevojugador.save()
				print("-----------------------------------------------------")
				print("Jugador {}, con dorsal {} y posición {} fue guardado!".format(nuevojugador.nombre, nuevojugador.dorsal, nuevojugador.posicion))
				print("-----------------------------------------------------")
				mensaje()

			else:
				print("-----------------------------------------------------")
				print("Cupos llenos para defensas centrales :(")
				print("-----------------------------------------------------")
				mensaje()

		if pos1 == 'LT':
			
			if total_jugadores_lt <2:
				nuevojugador.save()
				print("-----------------------------------------------------")
				print("Jugador {}, con dorsal {} y posición {} fue guardado!".format(nuevojugador.nombre, nuevojugador.dorsal, nuevojugador.posicion))
				print("-----------------------------------------------------")
				mensaje()

			else:
				print("-----------------------------------------------------")
				print("Cupos llenos para laterales  :(")
				print("-----------------------------------------------------")
				mensaje()

		if pos1 == 'MED':
			
			if total_jugadores_med <4:
				nuevojugador.save()
				print("-----------------------------------------------------")
				print("Jugador {}, con dorsal {} y posición {} fue guardado!".format(nuevojugador.nombre, nuevojugador.dorsal, nuevojugador.posicion))
				print("-----------------------------------------------------")
				mensaje()

			else:
				print("-----------------------------------------------------")
				print("Cupos llenos para mediocentros  :(")
				print("-----------------------------------------------------")
				mensaje()

		if pos1 == 'DEL':
			
			if total_jugadores_del <2:
				nuevojugador.save()
				print("-----------------------------------------------------")
				print("Jugador {}, con dorsal {} y posición {} fue guardado!".format(nuevojugador.nombre, nuevojugador.dorsal, nuevojugador.posicion))
				print("-----------------------------------------------------")
				mensaje()

			else:
				print("-----------------------------------------------------")
				print("Cupos llenos para delanteros  :(")
				print("-----------------------------------------------------")
				mensaje()

	else:
		print("-----------------------------------------------------")
		print("Cupos llenos en el equipo :(")
		print("-----------------------------------------------------")
		mensaje()

def cantidadJugadores():
	total_jugadores = Jugador.objects().count()
	total_jugadores_por = Jugador.objects(posicion='POR').count()
	total_jugadores_def = Jugador.objects(posicion='DEF').count()
	total_jugadores_lt = Jugador.objects(posicion='LT').count()
	total_jugadores_med = Jugador.objects(posicion='MED').count()
	total_jugadores_del = Jugador.objects(posicion='DEL').count()
	print("----------LISTA DE POSICIONES---------------------")
	print("Total jugadores      {}".format(total_jugadores))
	print("Total porteros       {}".format(total_jugadores_por))
	print("Total centrales      {}".format(total_jugadores_def))
	print("Total laterales      {}".format(total_jugadores_lt))
	print("Total mediocentros   {}".format(total_jugadores_med))
	print("Total delanteros     {}".format(total_jugadores_del))
	mensaje()


def buscarJador():
	print("------BUSCAR JUGADOR " )
	dorsal_buscado= validar_entero()
	jugador = Jugador.objects(dorsal=dorsal_buscado)
	if jugador:
		print("-----------------------------------------")
		print("Enontrado {}".format(jugador))
		print("-----------------------------------------")
		mensaje()
	else:
		print("-----------------------------------------")
		print("jugador con dorsal {} No enontrado".format(dorsal_buscado))
		print("-----------------------------------------")
		mensaje()

def eliminarJugador():
	print("------ELIMINAR JUGADOR " )
	dorsal_buscado= validar_entero()
	jugador = Jugador.objects(dorsal=dorsal_buscado)

	if jugador:
		print("-----------------------------------------")
		print("Enontrado {}".format(jugador))
		print("-----------------------------------------")
		opc = input("¿Seguro quiere elminar? 1-Si  2-N0: ")
		if opc == "1":
			Jugador.objects(dorsal=dorsal_buscado).delete()
			print("--------------------------------------")
			print("Jugador eliminado con éxito")
			print("--------------------------------------")
			mensaje()
	else:
		print("-----------------------------------------")
		print("jugador con dorsal {} No enontrado".format(dorsal_buscado))
		print("-----------------------------------------")
		mensaje()

def listJugadores():
	print("------------------------Lista de jugadores------------------------")
	for j in Jugador.objects:
		print("------------------------------------------------------------------")
		print("|| Nombre: {} || Dorsal:  {} || Posición {} || Valoración {}".format(j.nombre, j.dorsal, j.posicion, j.valoracion))
	print("------------------------------------------------------------------")
	mensaje()


def asignar_valoraciones(): 	
	print("------ASIGNAR VALORACIONES----------------- " )
	dorsal_buscado= validar_entero()
	jugador = Jugador.objects(dorsal=dorsal_buscado)
	if jugador:
		print("-----------------------------------------")
		print("Enontrado {},su valoración actual es de {} ".format(jugador.nombre,jugador.nombre))
		print("-----------------------------------------")
		mensaje()
	else:
		print("-----------------------------------------")
		print("jugador con dorsal {} No enontrado".format(dorsal_buscado))
		print("-----------------------------------------")
		mensaje()


while True:
	clear()
	menu()
	opc= input("escoja opcion: ")
	if opc == "1":
		clear()
		crearJugador()
	if opc == "2":
		clear()	
		cantidadJugadores()
	if opc == "3":
		clear()
		buscarJador()
	if opc == "4":
		clear()
		eliminarJugador()
	if opc == "5":
		clear()
		listJugadores()
	if opc == "6":
		clear()
		asignar_valoraciones()
	if opc == "0":
		clear()
		break


		