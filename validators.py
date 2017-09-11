def validar_dorsal():
    """ Solicita un valor entero y lo devuelve.
        Mientras el valor ingresado no sea entero, vuelve a solicitarlo. """
    while True:
        var = input("Ingrese dorsal: ")
        try:
            valor = int(var)
            return valor
        except ValueError:
            print("Sólo se aceptan números...")

def validar_entero():
    """ Solicita un valor entero y lo devuelve.
        Mientras el valor ingresado no sea entero, vuelve a solicitarlo. """
    while True:
        var = input("Ingrese dorsal del jugador : ")
        try:
            valor = int(var)
            return valor
        except ValueError:
            print("Sólo se aceptan números...")

def num():
    """ Solicita un valor entero y lo devuelve.
        Mientras el valor ingresado no sea entero, vuelve a solicitarlo. """
    while True:
        var = input("Ingrese número de acuerdo a la posición que desea: ")
        try:
            valor = int(var)
            if valor <=5:	
            	return valor
            else:
            	print("opción no válida")
        except ValueError:
            print("Sólo se aceptan números...")
